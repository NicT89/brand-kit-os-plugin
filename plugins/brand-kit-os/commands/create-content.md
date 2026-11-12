---
description: Generate brand-aligned content for a specified content type, audience, and topic
argument-hint: <content type> for <audience> about <topic>
---

# /brand-kit-os:create-content

Generate brand-aligned content for a specified content type, audience, and topic using Brand Kit OS data.

## Arguments

`$ARGUMENTS` should include any combination of:
- **Content type** — email, proposal, social post, blog post, ad copy, landing page, etc.
- **Audience** — target persona or audience description
- **Topic** — subject matter, key messages, or brief

## Workflow

1. **Identify brand kit** — Call `get_agent_briefing` with no arguments to list the user's kits. If there is more than one, ask the user which to use.
2. **Parse arguments** — Extract content type, audience, and topic from the user's input. If any are missing, ask before proceeding.
3. **Load relevant sections** — Based on the content type:
   - Always: `get_brand_kit` with `sections: ["expression", "governance", "anti_slop_rules"]`
   - If audience specified: `get_brand_kit` with `sections: ["audience"]`
   - If product-focused: `get_brand_kit` with `sections: ["products"]`
   - If persona-driven: `get_brand_kit` with `sections: ["ai_personas"]`
4. **Delegate to content-generation agent** — Pass brand context, content requirements, and audience details for generation.
5. **Adapt for audience** — If a specific persona is targeted, delegate to the audience-adaptation agent for persona-specific tuning.
6. **Validate** — Run `check_draft` on the draft, then the quality-assurance agent, before delivery. If `check_draft` reports a hard violation or QA returns Needs Revision, revise the draft and run both checks again. If QA returns Fail, explain the findings to the user instead of delivering the draft as final. Deliver only after both checks pass.
7. **Present** — Deliver the content with brand application notes explaining voice, tone, and terminology choices.
8. **Offer next steps** — Suggest variations (different audience, platform, or tone), batch generation, or content review.

## When no brand kit is found

If `get_agent_briefing` lists no brand kits, inform the user:
> "No brand kits found. Create a brand kit at brandkitos.com to start generating brand-aligned content."

## Rules

1. Always load expression and governance before generating — these are the minimum for on-brand content
2. Layer additional data on demand — don't load the full brand kit unless explicitly needed
3. For batch requests (e.g., "5 emails for different personas"), generate each variant with persona-specific adaptation while maintaining brand consistency
4. Include brand application notes with every delivery so the user understands what guidelines shaped the output
