# Changelog

All notable changes to the Brand Kit OS plugin are recorded here. Versions follow [semantic versioning](https://semver.org). The version in `plugin.json` is what Claude uses to decide whether an installed copy needs updating, so every release bumps it.

## 0.4.1 (2026-11-12)

### Fixed
- Skills, agents, commands and the data model reference now use the tool names of the Brand Kit OS MCP server, version 3. The plugin still pointed at the old per-section tools (`get_brand_kit_expression`, `upsert_brand_kit_core` and others), which the server no longer exposes. Reads now go through `get_brand_kit` with `sections`, and writes through `update_brand_kit` and the `manage_*` tools.
- Command headings used the wrong namespace (`/brand-kit:`). They now read `/brand-kit-os:`.
- Removed a checklist item that referred to a topic-scout agent this plugin does not ship.

### Changed
- Content generation, review and quality assurance now run `check_draft`, so drafts are tested against the kit's anti-slop rules, negative directory and writing constraints.
- Content generation can load its context in one call with `get_brand_context_for_agent`.
- Platform-specific voice now comes from `platform_expressions` instead of the removed `content_categories` field.
- The data model reference documents the write rules: preview first, confirmation, provenance, the review queue, and archive instead of delete.
- The README no longer says the Leafpad plugin includes this one. The two are separate plugins with separate releases.

### Added
- `CHANGELOG.md` and `RELEASING.md` (versioning, release steps and how new features are gated: server-side flags, plus a Labs plugin listed in this same marketplace).
- `scripts/validate_plugin.py` and a GitHub Actions check. It fails a pull request if the manifests disagree on the version, if the changelog has no entry for it, or if any file names an MCP tool that is not in `scripts/mcp-tools.txt`.

## 0.4.0

- Sign-in by default: no API key needed.
