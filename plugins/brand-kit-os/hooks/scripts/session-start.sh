#!/usr/bin/env bash
# Brand Kit OS session-start hook.
# SessionStart hooks can only run commands, so this can't call MCP tools itself.
# It injects an instruction into context; Claude does the loading on its first turn.
# No network. Must stay cheap: it runs in every session.

set -euo pipefail

cat <<'MSG'
BRAND KIT OS: plugin active.
Before your first content, copy, or brand-related task this session, call the
brand-kit-os `list_brand_kits` tool.
- Exactly one kit: call `get_brand_kit_expression` and `get_brand_kit_governance`
  for it and follow that tone, voice, and constraints for the rest of the session.
- Several kits: ask the user which one to use before loading anything.
- Tool missing or call fails: carry on without brand context and do not mention
  it unless the user asks about their brand kit.
Do not announce this setup step.
MSG
exit 0
