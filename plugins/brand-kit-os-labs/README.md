# Brand Kit OS Labs

Experimental skills for Brand Kit OS. Install this alongside the main `brand-kit-os` plugin if you want to try new skills before they are finished. Skills here can change or be removed. When one is ready, it moves into the main plugin.

## Install

Labs is listed in the same marketplace as the main plugin, so there is nothing new to add.

**Claude Desktop or Cowork:** open **Customize**, then **Plugins**, and install **brand-kit-os-labs** from the Brand Kit OS marketplace.

**Claude Code:**

```
/plugin install brand-kit-os-labs@brand-kit-os
```

Labs needs the main `brand-kit-os` plugin installed and signed in. It uses that plugin's connection to your brand kits.

## What is in Labs

| Component | Name | Purpose |
|-----------|------|---------|
| Skill | mission-vision-builder | Creates or rewrites your mission and vision from your brand kit, with options, a recommendation and trade-offs |
| Skill | kit-audit | Audits a brand kit and routes each gap to the skill or tool that fixes it |
| Command | /brand-kit-os-labs:mission-vision | Run the mission and vision builder |
| Command | /brand-kit-os-labs:audit-kit | Run the kit audit |

Nothing is written to your brand kit without your approval. Every change is previewed first.

## Feedback

Labs exists to find out what works. If a skill gives you a weak result, that is useful: tell us what you asked for and what you got.
