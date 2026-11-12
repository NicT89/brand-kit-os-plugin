# Releasing the Brand Kit OS plugin

This repository is a Claude plugin marketplace. People install it by adding `NicT89/brand-kit-os-plugin` in Claude, which reads the default branch. That makes two things true:

- **Merging to `main` is releasing.** There is no separate deploy step.
- **Users only get an update when the version changes.** Claude compares the `version` in `plugin.json` with the installed copy. If you merge without bumping it, nobody receives the change.

Reference: [Claude plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) and the [plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference).

## Version control

1. **Never commit to `main` directly.** Work on a branch and open a pull request.
2. **One version, three places.** `plugins/brand-kit-os/.claude-plugin/plugin.json`, and both `version` fields in `.claude-plugin/marketplace.json`, must match. The check fails if they do not.
3. **Semantic versioning.**
   - Patch (0.4.0 to 0.4.1): fixes, wording, tool-name corrections.
   - Minor (0.4.1 to 0.5.0): a new skill, agent or command.
   - Major: a change that breaks existing use, such as removing a command.
4. **Changelog.** Every version gets an entry in `CHANGELOG.md` saying what changed in plain language.
5. **Tag after merge.** Tag the merge commit `brand-kit-os--v<version>` (for example `brand-kit-os--v0.4.1`). This is the tag format Claude's plugin tooling uses, and it gives you a commit to roll back to.

### Rolling back

Revert the merge on a branch, bump the patch version, and merge. A rollback is a new release: users will not move back to an older version number.

## Feature flags

A plugin has no on/off switches of its own: if a skill file is in the released plugin, every user has it. So new work is gated in one of three ways, depending on what is being gated.

| What you are gating | How | Who gets it |
|---|---|---|
| A capability that runs on the server (a new MCP tool, a new enrichment) | Flag it in the Brand Kit OS server, per account | Accounts with the flag |
| An experimental skill, agent or command | Ship it in a separate `brand-kit-os-labs` plugin in this same marketplace | People who choose to install Labs |
| A pre-release of the whole plugin | A `beta` branch that testers add as its own marketplace | Testers only |

Rules that make this work:

- **Skills must degrade gracefully.** Every skill names the MCP tools it needs. If one is missing from the session (because the server flag is off for that account), the skill says what it could not do and carries on. It never invents data.
- **Labs graduates by moving.** When an experimental skill is ready, move its folder from the Labs plugin into `plugins/brand-kit-os/` and bump the minor version of both.
- **Labs is created with its first skill.** An empty plugin would appear in the marketplace with nothing in it, so the Labs plugin is added in the same pull request as the first experimental skill.
- **Channels need distinct versions.** If `beta` and `main` carry the same version number, Claude treats them as identical. Use a pre-release version on `beta` (for example `0.5.0-beta.1`).

## Release checklist

- [ ] Branch and pull request, not a direct commit
- [ ] Version bumped in all three places
- [ ] `CHANGELOG.md` entry written
- [ ] `python3 scripts/validate_plugin.py` passes
- [ ] If the MCP server gained or lost tools, `scripts/mcp-tools.txt` is updated to match
- [ ] Installed from the branch and tried in Claude before merging
- [ ] After merge: tag `brand-kit-os--v<version>`

## When the MCP server changes

`scripts/mcp-tools.txt` is the list of tool names the plugin is allowed to mention. When the server adds, renames or removes a tool:

1. Update `scripts/mcp-tools.txt`.
2. Run the check. It lists every file that still names a tool that is gone.
3. Fix those files and release.

`get_agent_briefing` with `include: ["tool_map"]` returns the server's live map of tools per section, which is the source of truth.
