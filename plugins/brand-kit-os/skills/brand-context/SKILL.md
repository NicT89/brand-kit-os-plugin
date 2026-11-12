---
name: brand-context
description: Load Brand Kit OS context (summary, expression, governance, audience, products) at the right level of detail for the current task. Activates when the user asks about their brand or starts any content-creation task.
---

# Brand Context: Skill

## Purpose
Guide Claude on **when** and **how** to load specific parts of a Brand Kit OS brand kit so that every response is grounded in real brand data.

## When to activate
- The user asks about their brand, voice, audience, products, or guidelines.
- The user starts a content-creation task (blog post, email, social caption, ad copy, landing page, and so on).
- The user asks Claude to review or critique existing content for brand alignment.

## Picking the kit
1. Call `get_agent_briefing` with no arguments to list the kits this user can access. Never guess a `brand_kit_id`.
2. One kit: use it. Several kits: ask the user which one before loading anything.
3. Call `get_agent_briefing` again with the chosen `brand_kit_id` for section health and the recommended next step.

## Loading strategy

Every read goes through `get_brand_kit`. Ask only for the sections the task needs.

| User intent | Call | Why |
|---|---|---|
| Quick context ("What's my brand about?") | `get_brand_kit` with no `sections` | Returns the compact summary plus `available_sections`. |
| Content creation (any format) | `get_brand_context_for_agent` with `task_type: "content_generation"` and the target `platform` | One call returns voice, governance, examples, audience and the knowledge-file index for that platform. |
| Voice and rules only | `get_brand_kit` with `sections: ["expression", "governance", "anti_slop_rules"]` | The minimum for on-brand writing when the bundle is more than the task needs. |
| Platform-specific voice | `get_brand_kit` with `sections: ["platform_expressions"]` and `platform` | Expression merged with that platform's overrides. |
| Audience-targeted content | Add `sections: ["audience"]` (use `fields` to keep it small) | Persona details for targeting. |
| Product-focused content | Add `sections: ["products"]` | Product catalog, USPs, differentiators. |
| AI persona work | `get_brand_kit` with `sections: ["ai_personas"]` and `view: "index"`, then the full persona you need | The index is a slim list; load one persona in full. |
| Competitive or sales work | `sections: ["competitors"]`, `["objections"]`, `["attack_angles"]`, `["customer_quotes"]` | Load only the ones the task uses. |
| Full brand deep-dive | `get_brand_kit` with `sections: ["all"]` | Returns everything. Large payload: use sparingly. |
| Knowledge file reference | `get_brand_kit` with `sections: ["knowledge_files"]`, then `get_knowledge_file` with the `file_id` | The index shows each file's relevance hint; open only the file that matches. |
| Kit health or gaps | `audit_brand_kit` | Scores every section and lists what to fix. |

See `references/data-model.md` for every section, its fields and the tool that writes it.

## Rules
1. **Start light.** Load the summary or the task bundle first. Go deeper only when the task needs it.
2. **Layer on demand.** If the request expands, load the next relevant section. Do not re-fetch the whole kit.
3. **Cite the source.** When applying a brand rule, mention it briefly (for example, "Per your governance guidelines...").
4. **Respect multiple kits.** If the user has more than one kit, confirm which one before loading data.
5. **Degrade gracefully.** If a tool named here is missing from the session, say what you could not load and carry on with what you have. Do not invent brand data.

## Connection errors
- **401 / needs sign-in:** Brand Kit OS is not signed in. In Claude Code the user runs `/mcp`, selects `brand-kit-os` and chooses Authenticate; in Claude Desktop or Cowork they click Connect.
- **403:** not a plan limit; every plan, including free, can connect. Have the user sign in again once; if it persists, ask them to contact Brand Kit OS support.
- **Calls keep failing:** run `doctor` before retrying. It reports whether the connection is healthy and who can fix each error.
