#!/usr/bin/env python3
"""Checks every plugin in this marketplace before a release.

Run from the repository root. Fails when:
  - a manifest is not valid JSON
  - a plugin folder is not listed exactly once in marketplace.json (or the
    reverse: a listed plugin has no folder)
  - a plugin's version differs between its plugin.json and its marketplace entry
  - the main plugin's version differs from marketplace.json metadata.version
  - CHANGELOG.md has no entry for a plugin's current version
  - a skill, agent or command is missing its frontmatter
  - any plugin file names an MCP tool that is not in scripts/mcp-tools.txt
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
MAIN = "brand-kit-os"
SEMVER = re.compile(r"\d+\.\d+\.\d+(-[0-9A-Za-z.]+)?")
errors = []


def rel(path):
    return path.relative_to(ROOT)


def load_json(path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{rel(path)}: not valid JSON ({exc})")
        return None


def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    block = text.split("---\n", 2)[1]
    return dict(line.split(":", 1) for line in block.splitlines() if ":" in line)


marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json") or {}
entries = marketplace.get("plugins", [])
changelog_path = ROOT / "CHANGELOG.md"
changelog = changelog_path.read_text() if changelog_path.exists() else ""

allowed = {
    line.strip()
    for line in (ROOT / "scripts" / "mcp-tools.txt").read_text().splitlines()
    if line.strip() and not line.startswith("#")
}
# Tool names start with one of these verbs. Field names (tone_dimensions,
# negative_directory) do not, so they are ignored.
VERBS = (
    "get|list|update|upsert|create|delete|manage|generate|audit|scrape|enrich|"
    "archive|review|check|draft|approve|batch|upload|recompute"
)
# Matches a bare name (`get_brand_kit`) and an inline call (`get_brand_kit({...})`).
token = re.compile(rf"`((?:{VERBS})_[a-z0-9_]+)(?=`|\()")
# Backticked words that look like tools but are argument values or fields.
NOT_TOOLS = {"create_upload_url", "draft_text", "scrape_inferred"}

folders = sorted(p for p in PLUGINS.iterdir() if p.is_dir())
folder_names = {p.name for p in folders}
versions = {}

# Every listed plugin has a folder.
for entry in entries:
    if entry.get("name") not in folder_names:
        errors.append(
            f"marketplace.json lists '{entry.get('name')}' but plugins/ has no such folder"
        )

for plugin in folders:
    name = plugin.name
    manifest = load_json(plugin / ".claude-plugin" / "plugin.json")
    for optional in (plugin / ".mcp.json", plugin / "hooks" / "hooks.json"):
        if optional.exists():
            load_json(optional)
    if manifest is None:
        continue

    # 1. Name, version, and exactly one marketplace entry.
    if manifest.get("name") != name:
        errors.append(f"{name}: plugin.json name is '{manifest.get('name')}'")
    version = manifest.get("version")
    versions[name] = version
    if not version or not SEMVER.fullmatch(version):
        errors.append(f"{name}: plugin.json version is not semantic: {version!r}")
    matches = [entry for entry in entries if entry.get("name") == name]
    if len(matches) != 1:
        errors.append(
            f"marketplace.json must list '{name}' exactly once (found {len(matches)})"
        )
    elif matches[0].get("version") != version:
        errors.append(
            f"{name}: plugin.json says {version}, marketplace.json says "
            f"{matches[0].get('version')}"
        )

    # 2. Changelog entry. The main plugin is headed with the version alone.
    heading = f"## {version}" if name == MAIN else f"## {name} {version}"
    if version and not re.search(rf"^{re.escape(heading)}(\s|$)", changelog, re.M):
        errors.append(f"CHANGELOG.md has no '{heading}' entry")

    # 3. Frontmatter.
    for skill in sorted((plugin / "skills").glob("*/SKILL.md")):
        fm = frontmatter(skill)
        if not fm or "name" not in fm or "description" not in fm:
            errors.append(f"{rel(skill)}: needs name and description frontmatter")
        elif fm["name"].strip() != skill.parent.name:
            errors.append(
                f"{rel(skill)}: name '{fm['name'].strip()}' does not match its folder"
            )
    for kind in ("agents", "commands"):
        for path in sorted((plugin / kind).glob("*.md")):
            fm = frontmatter(path)
            if not fm or "description" not in fm:
                errors.append(f"{rel(path)}: needs description frontmatter")

    # 4. Every tool named in the plugin exists on the server.
    for path in sorted(plugin.rglob("*")):
        if path.suffix not in {".md", ".sh"} or not path.is_file():
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            for tool in token.findall(line):
                if tool not in allowed and tool not in NOT_TOOLS:
                    errors.append(
                        f"{rel(path)}:{number}: `{tool}` is not a Brand Kit OS "
                        "MCP tool (see scripts/mcp-tools.txt)"
                    )

# The marketplace's own version tracks the main plugin.
if MAIN not in versions:
    errors.append(f"plugins/{MAIN} is missing")
elif marketplace.get("metadata", {}).get("version") != versions[MAIN]:
    errors.append(
        f"marketplace.json metadata.version is "
        f"{marketplace.get('metadata', {}).get('version')}, {MAIN} is {versions[MAIN]}"
    )

if errors:
    print("Plugin check failed:\n")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

summary = ", ".join(f"{name} {version}" for name, version in sorted(versions.items()))
print(f"Plugin check passed ({summary}; {len(allowed)} known tools).")
