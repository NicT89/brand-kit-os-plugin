#!/usr/bin/env bash
# Brand Kit OS session-start hook.
# SessionStart hooks can only run commands, so this can't call MCP tools itself.
# It injects an instruction into context; Claude does the bootstrap on its first turn.
# No network. Must stay cheap: it runs in every session.

set -euo pipefail

cat <<'MSG'
BRAND KIT OS: plugin active.
Before your first brand or content task this session, call the brand-kit-os
`get_agent_briefing` tool with no arguments to list the user's brand kits.
- Exactly one kit: call `get_agent_briefing` again with its brand_kit_id and use the
  section health and recommended_next_steps it returns.
- Several kits: ask the user which one to use, then call
  `get_agent_briefing({ brand_kit_id })` before any other brand-kit-os tool.
- Tool missing or call fails: carry on without brand context and do not mention it
  unless the user asks about their brand kit.
Do not announce this setup step.
MSG
exit 0
