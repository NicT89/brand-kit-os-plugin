---
name: brand-context
description: >
  Load and manage Brand Kit OS brand context for conversations. This skill should be used when
  the user asks to "load my brand kit", "connect my brand", "use my brand voice",
  "get my brand context", "show my brand guidelines", "what brands do I have",
  "pull my brand data", "fetch brand info", or any request involving retrieving
  brand identity, voice, audience, or messaging data from Brand Kit OS.
  Also triggers when the user references their brand kit by name or asks Claude
  to write content that should align with their brand.
version: 0.1.0
---

# Brand Context Loader

Fetch and structure brand kit data from Brand Kit OS so Claude can produce on-brand content.

## Available MCP Tools

The Brand Kit OS MCP server exposes these tools. Use them to retrieve specific sections of a user's brand kit:

| Tool | Purpose | When to use |
|------|---------|-------------|
| `list_brand_kits` | List all brand kits the user can access | When you need to find which brand kits exist or let the user choose one |
| `get_brand_kit` | Fetch the complete brand kit with all sections | When the user wants full context loaded or you need comprehensive brand data |
| `get_brand_kit_core` | Mission, vision, brand story, promises | When writing about the company's purpose or positioning |
| `get_brand_kit_personality` | Traits, values, principles, moods | When you need to match the brand's character in content |
| `get_brand_kit_expression` | Tone of voice, verbal style, archetypes, visual style | When writing any content -- this is the most commonly needed section |
| `get_brand_kit_products` | Products and services | When referencing offerings, features, pricing, or differentiators |
| `get_brand_kit_audience` | Target audience personas | When tailoring content to specific reader segments |
| `get_brand_kit_governance` | Constraints, taboo topics, compliance notes, claims to avoid | When you need to ensure content stays within brand guardrails |
| `get_brand_kit_personas` | AI persona configurations | When the user wants Claude to adopt a specific brand persona |
| `list_knowledge_files` | Knowledge files attached to a brand kit | When you need supplementary brand reference material |
| `get_knowledge_file` | Specific knowledge file metadata | When retrieving a particular reference document |

## Loading Strategy

### Essentials Load (default for session start)

Pull the minimum context needed for on-brand writing:

1. Call `get_brand_kit_expression` -- tone, verbal style, voice archetypes
2. Call `get_brand_kit_governance` -- constraints, taboo topics, required disclaimers
3. Call `get_brand_kit_core` -- mission and positioning for context

This gives Claude enough to write on-brand without consuming excessive context.

### Full Load (on user request)

When the user says "load my full brand kit" or needs comprehensive context:

1. Call `get_brand_kit` -- returns everything in one call
2. Parse the response to understand all brand dimensions

### On-Demand Loading

For specific tasks, pull only what is needed:

- Writing a blog post? Load expression + audience + products
- Creating ad copy? Load expression + products + CTAs (from governance)
- Drafting a pitch? Load core + products + audience
- Checking compliance? Load governance

## Handling Multiple Brand Kits

If `list_brand_kits` returns more than one kit:

1. Present the list to the user with names and descriptions
2. Ask which brand kit to use for this session
3. Store the selected brand_kit_id for subsequent calls

If only one kit exists, use it automatically.

## Structuring Brand Context for Writing

After fetching brand data, organize it into a working reference. The key sections Claude should internalize:

**Voice directives** -- tone descriptors, formality level, humor level, reading level. These govern HOW to write.

**Do/Don't phrases** -- specific language patterns to use or avoid. Apply these as hard rules.

**Constraints** -- taboo topics and claims to avoid are non-negotiable. Never violate these regardless of the writing task.

**Audience awareness** -- persona pain points, goals, and values shape WHAT to write about and which angles to emphasize.

**Product knowledge** -- features, benefits, and differentiators provide factual content to weave into writing.

## Error Handling

If an MCP tool call fails:
- Authentication error (401): Tell the user their API key may be invalid or expired. Direct them to Brand Kit OS Settings to generate a new key.
- Subscription error (403): Tell the user MCP access requires a Base or Premium plan.
- Rate limit (429): Wait 60 seconds and retry, or inform the user.
- Not found (404): The brand kit ID may be incorrect. Call `list_brand_kits` to find valid IDs.
