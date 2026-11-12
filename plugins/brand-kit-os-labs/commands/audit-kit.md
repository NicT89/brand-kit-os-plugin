---
description: Audit your brand kit and get an ordered list of what to fix
argument-hint: [brand kit name]
---

# /brand-kit-os-labs:audit-kit

Use the `kit-audit` skill on the brand kit named in `$ARGUMENTS`. If no kit is named, list the user's kits with `get_agent_briefing` and ask which one.

Report the top gaps in dependency order and route each to its fix. Do not write to the kit without the user's approval.
