# Brand Kit OS Plugin for Claude

Connect your Brand Kit OS brand kits to Claude. This plugin gives Claude real-time access to your brand identity, voice, audience, messaging, and guidelines so every piece of content it creates is on-brand.

## What it does

- **Auto-loads brand context** when you start a session, so Claude already knows your brand voice
- **Enforces brand voice** across all content creation (emails, blog posts, social media, ads, proposals)
- **Reviews content** for brand compliance and suggests improvements
- **Pulls specific brand data** on demand (products, audience personas, SEO keywords, etc.)

## Setup

### 1. Get your API key

1. Log in to [Brand Kit OS](https://brandkitos.com)
2. Go to **Settings** and select the **API Keys** tab
3. Click **Create API Key** and copy the key (it starts with `bk_`)
4. Save the key securely. It is only shown once.

**Note:** MCP access requires a Base or Premium subscription.

### 2. Install the plugin

In Claude Code, add this marketplace and install the plugin:

```
/plugin marketplace add NicT89/brand-kit-os-plugin
/plugin install brand-kit-os@brand-kit-os
```

When prompted, paste your API key. It is stored securely and used only to connect to Brand Kit OS.

### 3. Restart Claude

After installing, restart Claude. The plugin will connect to your Brand Kit OS account and load your brand context before your first brand-related task.

### Updating

Run `/plugin marketplace update brand-kit-os` to pull the latest version.

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| MCP Server | brand-kit-os | Connects to the Brand Kit OS API to read and update your brand kits |
| Skill | brand-context | Loads and manages brand kit data throughout conversations |
| Skill | brand-voice-enforcement | Applies brand guidelines to content creation and reviews |
| Agent | content-generation | Writes brand-aligned emails, proposals, posts, ads, and landing pages |
| Agent | brand-review | Reviews existing content against your brand standards |
| Agent | audience-adaptation | Tailors content to a specific audience persona |
| Agent | quality-assurance | Final compliance check before content is delivered |
| Command | /create-content | Generate brand-aligned content for a content type, audience, and topic |
| Command | /enforce-voice | Load your brand guidelines and apply them to a request |
| Hook | SessionStart | Tells Claude to load your brand context before the first brand-related task |

## Available MCP Tools

Once connected, Claude can use the full Brand Kit OS tool set, starting with:

| Tool | Description |
|------|-------------|
| `get_agent_briefing` | Start here: lists your brand kits, or gives one kit's health and recommended next steps |
| `list_brand_kits` | List all brand kits you have access to |
| `get_brand_kit_expression` | Tone of voice, verbal style, and archetypes |
| `get_brand_kit_governance` | Constraints, taboo topics, and compliance |
| `get_brand_kit_audience` | Target audience personas |
| `get_brand_kit_products` | Products and services |

See the [developer documentation](https://brandkitos.com/documentation) for the complete list.

## Publishing to Leafpad

For blog publishing, topic research, and content calendars on Leafpad, install the companion plugin instead: [brand-kit-os-plugin-leafpad](https://github.com/NicT89/brand-kit-os-plugin-leafpad). It includes everything in this plugin plus the Leafpad workflows.

## Usage Examples

**Auto-loaded context**: Just start writing. Claude will use your brand voice automatically.

**Load full context**: Say "load my full brand kit" to pull all brand data.

**Write on-brand**: "Write a blog post about [topic]" and Claude will apply your voice, tone, and constraints.

**Review content**: "Is this email on-brand?" and Claude will score it against your guidelines.

**Switch brands**: If you have multiple brand kits, say "use [brand name]" to switch.

## Troubleshooting

- **"Invalid API key" error**: Your key may have expired. Generate a new one in Brand Kit OS Settings.
- **"Subscription required" error**: MCP access requires a paid plan (Base or Premium).
- **No brand data loading**: Check your API key with `/plugin` (reconfigure the plugin to re-enter it), then restart Claude.
- **Rate limiting**: The API allows 100 requests per minute. If you hit this limit, wait a moment and try again.

## Support

- Documentation: [brandkitos.com/documentation](https://brandkitos.com/documentation)
- Partner API Reference: [brandkitos.com/documentation/reference/partner-api](https://brandkitos.com/documentation/reference/partner-api)
