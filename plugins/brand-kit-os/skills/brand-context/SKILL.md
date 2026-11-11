---
name: brand-context
description: Load Brand Kit OS context (summary, expression, governance, audience, products) at the right level of detail for the current task. Activates when the user asks about their brand or starts any content-creation task.
---

# Brand Context — Skill

## Purpose
Guide Claude on **when** and **how** to load specific sections of a Brand Kit OS brand kit so that every response is grounded in real brand data.

## When to activate
- The user asks about their brand, voice, audience, products, or guidelines.
- The user starts a content-creation task (blog post, email, social caption, ad copy, landing page, etc.).
- The user asks Claude to review or critique existing content for brand alignment.

## Loading strategy

| User intent | Tool(s) to call | Why |
|---|---|---|
| Quick context / "What's my brand about?" | `get_brand_kit_summary` | Returns a compact overview (~500 tokens). |
| Content creation (any format) | `get_brand_kit_expression` + `get_brand_kit_governance` | Voice rules + constraints are the minimum for on-brand writing. |
| Audience-targeted content | Above + `get_brand_kit_audience` | Adds persona details for targeting. |
| Product-focused content | Above + `get_brand_kit_products` | Adds product catalog, USPs, differentiators. |
| Full brand deep-dive | `get_brand_kit` | Returns everything. Use sparingly — large payload. |
| Knowledge file reference | `list_knowledge_files` → `get_knowledge_file` | When user references a specific doc or style guide. |

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
- Authentication error (401): Tell the user the Brand Kit OS connection needs signing in. In Claude Code they run `/mcp`, select brand-kit-os and choose Authenticate; in Claude Desktop or Cowork they click Connect when prompted.
- Access error (403): Tell the user the server could not authorise their account. This is not a plan limit: every plan, including free, can connect. Ask them to contact Brand Kit OS support.
- Rate limit (429): Wait 60 seconds and retry, or inform the user.
- Not found (404): The brand kit ID may be incorrect. Call `list_brand_kits` to find valid IDs.
## Rules
1. **Always start light.** Call `get_brand_kit_summary` first unless the task clearly needs deeper data.
2. **Layer on demand.** If the user's request expands, load the next relevant section — don't re-fetch the full kit.
3. **Cite the source.** When applying a brand rule, mention it briefly (e.g., "Per your governance guidelines…").
4. **Respect multiple kits.** If `list_brand_kits` returns more than one, ask the user which kit to use before loading data.
