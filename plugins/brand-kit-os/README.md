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

### 2. Set your environment variable

Add your API key as an environment variable named `BRAND_KIT_OS_API_KEY`.

**macOS/Linux** (add to `~/.zshrc` or `~/.bashrc`):
```bash
export BRAND_KIT_OS_API_KEY="bk_your_key_here"
```

**Windows** (PowerShell):
```powershell
[System.Environment]::SetEnvironmentVariable("BRAND_KIT_OS_API_KEY", "bk_your_key_here", "User")
```

### 3. Install the plugin

Install the `brand-kit-os.plugin` file in Claude Desktop or Cowork. The plugin will automatically configure the MCP server connection using your API key.

### 4. Restart Claude

After installing and setting the environment variable, restart Claude. The plugin will connect to your Brand Kit OS account and load your brand context on session start.

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| MCP Server | brand-kit-os | Connects to the Brand Kit OS API (11 tools for reading brand data) |
| Skill | brand-context | Loads and manages brand kit data throughout conversations |
| Skill | brand-voice-enforcement | Applies brand guidelines to content creation and reviews |
| Hook | SessionStart | Auto-loads essential brand context when a session begins |

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

- **"Invalid API key" error**: Your key may have expired. Generate a new one in Brand Kit OS Settings.
- **"Subscription required" error**: MCP access requires a paid plan (Base or Premium).
- **No brand data loading**: Make sure the `BRAND_KIT_OS_API_KEY` environment variable is set and Claude has been restarted.
- **Rate limiting**: The API allows 100 requests per minute. If you hit this limit, wait a moment and try again.

## Support

- Documentation: [brandkitos.com/documentation](https://brandkitos.com/documentation)
- Partner API Reference: [brandkitos.com/documentation/reference/partner-api](https://brandkitos.com/documentation/reference/partner-api)
