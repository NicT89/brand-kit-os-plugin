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

Run `/plugin marketplace update brand-kit-os` to pull the latest version.

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| MCP Server | brand-kit-os | Connects to the Brand Kit OS API (11 tools for reading brand data) |
| Skill | brand-context | Loads and manages brand kit data throughout conversations |
| Skill | brand-voice-enforcement | Applies brand guidelines to content creation and reviews |
| Hook | SessionStart | Tells Claude to load your brand context before the first brand-related task |

## Available MCP Tools

Once connected, Claude can use these tools:

| Tool | Description |
|------|-------------|
| `list_brand_kits` | List all brand kits you have access to |
| `get_brand_kit` | Get complete brand kit with all sections |
| `get_brand_kit_core` | Mission, vision, and brand story |
| `get_brand_kit_personality` | Traits, values, and principles |
| `get_brand_kit_expression` | Tone of voice, verbal style, and archetypes |
| `get_brand_kit_products` | Products and services |
| `get_brand_kit_audience` | Target audience personas |
| `get_brand_kit_governance` | Constraints, taboo topics, and compliance |
| `get_brand_kit_personas` | AI persona configurations |
| `list_knowledge_files` | Knowledge files for a brand kit |
| `get_knowledge_file` | Specific knowledge file details |

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
