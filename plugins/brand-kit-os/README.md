# Brand Kit OS Plugin for Claude

Connect your Brand Kit OS brand kits to Claude. This plugin gives Claude real-time access to your brand identity, voice, audience, messaging, and guidelines so every piece of content it creates is on-brand.

## What it does

- **Auto-loads brand context** when you start a session, so Claude already knows your brand voice
- **Enforces brand voice** across all content creation (emails, blog posts, social media, ads, proposals)
- **Reviews content** for brand compliance and suggests improvements
- **Pulls specific brand data** on demand (products, audience personas, SEO keywords, etc.)

## Setup

You need a Brand Kit OS account. The free plan works; no API key is needed.

### 1. Install the plugin

**Claude Desktop or Cowork:** open **Customize**, then **Plugins**. Click **Add**,
choose **Add marketplace**, then **Add from a repository**, and enter
`NicT89/brand-kit-os-plugin`. Install the **brand-kit-os** plugin it lists.

**Claude Code:** run these two commands.

```
/plugin marketplace add NicT89/brand-kit-os-plugin
/plugin install brand-kit-os@brand-kit-os
```

### 2. Sign in

The first time Claude uses Brand Kit OS it asks you to sign in. In Claude
Desktop or Cowork, click **Connect** when it appears. In Claude Code, run `/mcp`,
select **brand-kit-os** and choose **Authenticate**. Sign in to Brand Kit OS in
the browser window that opens and approve the connection.

The connection renews itself, so you only sign in once.

### Updating

Run `/plugin marketplace update brand-kit-os` to pull the latest version. Releases are listed in [CHANGELOG.md](../../CHANGELOG.md).

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
| `get_brand_kit` | Read any part of a kit. Ask for the sections you need: expression, governance, audience, products, and more |
| `get_brand_context_for_agent` | One call that assembles the context a task needs, such as writing for a given platform |
| `check_draft` | Test a draft against the kit's writing rules before you use it |
| `audit_brand_kit` | Score the kit and list what to fix |
| `update_brand_kit` | Edit the kit. Every change is previewed before it is saved |

See the [developer documentation](https://brandkitos.com/documentation) for the complete list.

## Publishing to Leafpad

Blog publishing, topic research, and content calendars on Leafpad live in a separate plugin: [brand-kit-os-plugin-leafpad](https://github.com/NicT89/brand-kit-os-plugin-leafpad). It is maintained and versioned on its own.

## Usage Examples

**Auto-loaded context**: Just start writing. Claude will use your brand voice automatically.

**Load full context**: Say "load my full brand kit" to pull all brand data.

**Write on-brand**: "Write a blog post about [topic]" and Claude will apply your voice, tone, and constraints.

**Review content**: "Is this email on-brand?" and Claude will score it against your guidelines.

**Switch brands**: If you have multiple brand kits, say "use [brand name]" to switch.

## Troubleshooting

- **Asked to sign in again**: Sign in once more. In Claude Code, `/mcp` then **Authenticate**.
- **No brand data loading**: In Claude Code, run `/mcp` and check that **brand-kit-os** shows as connected. If it does not, choose **Authenticate**.
- **Rate limiting**: The API allows 100 requests per minute. If you hit this limit, wait a moment and try again.

## Support

- Documentation: [brandkitos.com/documentation](https://brandkitos.com/documentation)
- Partner API Reference: [brandkitos.com/documentation/reference/partner-api](https://brandkitos.com/documentation/reference/partner-api)
