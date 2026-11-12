# Brand Kit OS: Data Model Reference

How a brand kit is structured, how to read each part, and which tool writes it. Tool names here match the Brand Kit OS MCP server, version 3.

When in doubt, call `get_agent_briefing` with `include: ["tool_map"]`. It returns the live map of which tools read and write each section, and it is the source of truth if this file ever falls behind.

## Reading

All reads go through one tool: `get_brand_kit`.

- No `sections`: returns the compact summary plus `available_sections`.
- `sections: [...]`: returns only those sections.
- `sections: ["all"]`: the whole kit. Large.
- `fields`: optional subset of top-level field names, for sections that support it.
- `filter`: optional list filters (for example knowledge files by category, visual assets by media).
- `platform`: with `platform_expressions`, returns expression merged with that platform's overrides.
- `view: "index"`: with `ai_personas`, returns a slim list.

For a task-shaped bundle, use `get_brand_context_for_agent` (for example `task_type: "content_generation"` with a `platform`).

### Summary (default read)

| Field | Type | Notes |
|-------|------|-------|
| `name`, `tagline`, `description`, `brand_voice`, `mission`, `vision` | string | May be empty |
| `top_personality_traits` | string[] | Up to 3 trait names |
| `top_values` | string[] | Up to 3 value names |
| `tone` | object | Legacy `attributes[]` and `description` |
| `tone_dimensions` | object | 0 to 100 scales: `energy`, `formality`, `warmth`, `confidence`, `complexity`, optional `humor`. Authoritative when it overlaps `tone` |
| `top_constraints` | array | Up to 3 from governance |
| `products` | `{ name, type, usp }[]` | |
| `primary_audiences` | `{ persona_name, persona_type, demographics }[]` | |

## Sections

### Single-row sections (written with `update_brand_kit`)

Pass one object per section to change. Only the fields you send are written. Lists are edited card by card: `{ add, update, archive, restore }`.

| Section | Read | Write | Holds |
|---|---|---|---|
| Basics | default summary | `update_brand_kit` with `basics` | Name, description, long summary, tagline, website URL, social URLs, industry details, OG image |
| Core | `sections: ["core"]` | `update_brand_kit` with `core` | Mission, vision, brand story, brand promises, taglines (each with a use-when), storytelling elements, industry classification |
| Personality | `sections: ["personality"]` | `update_brand_kit` with `personality` | Personality traits (title, description, tags, what the trait must not become, an example), brand values, brand principles, brand moods |
| Expression | `sections: ["expression"]` | `update_brand_kit` with `expression` | Brand voice, tone of voice, `tone_dimensions`, voice archetypes, verbal style slots, visual style slots, preferred terminology, per-platform overrides |
| Governance | `sections: ["governance"]` | `update_brand_kit` with `governance` | Behavioral constraints, negative directory, writing constraints, platform rules, compliance selections, disclosure statements, usage guidelines, drift prevention prompts |
| Visuals | `sections: ["visuals"]` | `update_brand_kit` with `visuals` | Colors with usage guidance, fonts, spacing, logo URLs, optional design tokens |
| SEO | `sections: ["seo"]` | `update_brand_kit` with `seo` | Keywords, tags, suggested keywords |

Notes:
- **Storytelling elements** has keys `origin_story_summary`, `key_milestones`, `recurring_themes`, `brand_metaphors`, `hero_narrative`, `transformation_arc`, `founder_voice_notes`.
- **Verbal style** and **visual style** are keyed by slot (`slot_1` to `slot_5`). Each slot is a full template with a name and a use-when.
- **Voice archetypes**: look up options with `get_reference` (`library: "archetypes"`) and link by `archetype_id`.
- **Compliance**: pick standards from `get_reference` (`library: "compliance_standards"`). The free-text compliance and disclosure fields are deprecated.
- **Platform values** for governance rules come from `get_reference` (`library: "governance_platforms"`).

### Collections (each has its own tool)

| Section | Read with `sections:` | Write |
|---|---|---|
| Products and services | `["products"]` | `manage_product` |
| Audience personas | `["audience"]` | `manage_audience_persona` |
| AI personas | `["ai_personas"]` | `manage_ai_persona` |
| Company ICPs | `["company_icps"]` | `manage_company_profile` |
| Customers | `["customers"]` | `manage_company_profile` |
| Competitors | `["competitors"]`, `["competitor_suggestions"]` | `manage_competitor` |
| Partners | `["partners"]` | `manage_partner` |
| Customer quotes | `["customer_quotes"]` | `manage_customer_quote` |
| Objections | `["objections"]` | `manage_objection` |
| Attack angles | `["attack_angles"]` | `manage_attack_angle` |
| Anti-slop rules | `["anti_slop_rules"]` | `manage_anti_slop_rule` |
| Expression examples | `["expression_examples"]` | `manage_expression_example` |
| Logo assets | `["logo_assets"]` | `manage_logo_asset` |
| Visual assets (image, video, audio) | `["visual_assets"]` | `manage_visual_asset` |
| Knowledge files | `["knowledge_files"]`, then `get_knowledge_file` | `manage_knowledge_file` |
| Social profiles | `["social_profiles"]` | `scrape_source` |
| Content drafts | `["content_drafts"]` | `draft_brand_content` |

What the main collections hold:

- **Products and services**: name, type, description, key benefits, USP, competitive differentiation, pricing, use cases.
- **Audience personas**: demographics, goals, pain points, buying behavior, preferred channels, professional context, core motivation, representative quote. Allowed field values come from `get_reference` (`library: "persona_vocabulary"`).
- **AI personas**: name, purpose, role definition, tasks, behavioral rules, tone overrides, guardrails. For a ready-to-use system prompt, call `get_brand_context_for_agent` with `output: "system_prompt"` and the `persona_name`.
- **Competitors**: name, URL, description, positioning, target ICPs, when each was last verified.
- **Anti-slop rules**: banned terms, AI-tell phrases, punctuation and structure rules, each hard or soft, optionally scoped to platforms. `check_draft` enforces them.
- **Knowledge files**: supplementary documents (style guides, playbooks, research). Each has a relevance hint that says when to load it.

### Generating and enriching

| Tool | Use |
|---|---|
| `scrape_source` | Pull from a website, product pages, a social profile or the content library |
| `enrich_record` | Enrich one record (a product, persona, competitor, company profile) |
| `generate_records` | Generate records such as audience personas, AI personas or company ICPs |
| `create_brand_kit_from_url` | Build a new kit from a website |
| `get_run` | Poll a job that returned a `run_id` |

### Checking and auditing

| Tool | Use |
|---|---|
| `audit_brand_kit` | Completeness (default), next step, consistency, customer base, lookalikes, governance lint |
| `check_draft` | Test a draft against the kit's writing rules |
| `get_write_history` | See what recent writes changed, or verify a write persisted |
| `doctor` | Check the connection when calls start failing |

## Write rules

1. **Preview first.** Call every write with `dry_run: true`, show the user the preview, and commit only after they approve.
2. **Confirmation.** Accounts can require explicit confirmation. When they do, the commit call needs `confirm: true` and no `dry_run`. `get_agent_briefing` reports this under `account_settings`. For many writes, get one approval and use `approve_write_batch`.
3. **Credits.** Jobs that spend credits (scrapes, enrichment, generation, kit creation) always need the preview and then `confirm: true`.
4. **Provenance.** Send `basis` on every write (for example `customer_stated`, `operator_stated`, `page_verbatim`, `scrape_inferred`, `document`, `ai_inferred`), with `source_ref` when there is a URL or file behind it.
5. **Review queue.** Some writes are staged for a person to approve instead of being written. The response says so. Tell the user it is waiting in their review queue and do not retry.
6. **No hard deletes.** `archive_records` archives and restores. Nothing is deleted.
