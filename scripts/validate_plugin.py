#!/usr/bin/env python3
"""Checks the plugin before a release. Run from the repository root.

Fails when:
  - a manifest is not valid JSON
  - the version differs between plugin.json and marketplace.json
  - CHANGELOG.md has no entry for the current version
  - a skill, agent or command is missing its frontmatter
  - any plugin file names an MCP tool that is not in scripts/mcp-tools.txt
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "brand-kit-os"
errors = []


def load_json(path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path.relative_to(ROOT)}: not valid JSON ({exc})")
        return None


# 1. Manifests parse and agree on the version.
marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
manifest = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
load_json(PLUGIN / ".mcp.json")
load_json(PLUGIN / "hooks" / "hooks.json")

version = None
if marketplace and manifest:
    version = manifest.get("version")
    found = {
        "plugin.json": version,
        "marketplace.json metadata.version": marketplace.get("metadata", {}).get("version"),
    }
    for entry in marketplace.get("plugins", []):
        if entry.get("name") == manifest.get("name"):
            found["marketplace.json plugins[].version"] = entry.get("version")
    if len(set(found.values())) != 1:
        errors.append(f"version mismatch: {found}")
    if not version or not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.]+)?", version):
        errors.append(f"plugin.json version is not semantic: {version!r}")

# 2. The changelog has an entry for this version.
changelog = ROOT / "CHANGELOG.md"
if version and (not changelog.exists() or f"## {version}" not in changelog.read_text()):
    errors.append(f"CHANGELOG.md has no '## {version}' entry")

# 3. Frontmatter.
def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    block = text.split("---\n", 2)[1]
    return dict(
        line.split(":", 1) for line in block.splitlines() if ":" in line
    )

for skill in sorted((PLUGIN / "skills").glob("*/SKILL.md")):
    fm = frontmatter(skill)
    rel = skill.relative_to(ROOT)
    if not fm or "name" not in fm or "description" not in fm:
        errors.append(f"{rel}: needs name and description frontmatter")
    elif fm["name"].strip() != skill.parent.name:
        errors.append(f"{rel}: name '{fm['name'].strip()}' does not match its folder")

for kind in ("agents", "commands"):
    for path in sorted((PLUGIN / kind).glob("*.md")):
        fm = frontmatter(path)
        if not fm or "description" not in fm:
            errors.append(f"{path.relative_to(ROOT)}: needs description frontmatter")

# 4. Every tool named in the plugin exists on the server.
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
token = re.compile(rf"`((?:{VERBS})_[a-z0-9_]+)`")
# Backticked words that look like tools but are argument values or fields.
NOT_TOOLS = {"create_upload_url", "draft_text", "scrape_inferred"}

for path in sorted(PLUGIN.rglob("*")):
    if path.suffix not in {".md", ".sh"} or not path.is_file():
        continue
    for number, line in enumerate(path.read_text().splitlines(), 1):
        for name in token.findall(line):
            if name not in allowed and name not in NOT_TOOLS:
                errors.append(
                    f"{path.relative_to(ROOT)}:{number}: `{name}` is not a "
                    "Brand Kit OS MCP tool (see scripts/mcp-tools.txt)"
                )

if errors:
    print("Plugin check failed:\n")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

print(f"Plugin check passed (version {version}, {len(allowed)} known tools).")
