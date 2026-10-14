---
name: brand-voice-enforcement
description: >
  Enforce brand voice guidelines when creating or reviewing content. This skill should be used
  when the user asks to "write in my brand voice", "check if this is on-brand",
  "rewrite this in our tone", "make this sound like us", "enforce brand voice",
  "apply brand guidelines", "review this for brand compliance", "is this on-brand",
  "draft an email", "write a blog post", "create social media content",
  "write marketing copy", or any content creation request where brand consistency matters.
  Also triggers when the user shares existing content and asks for a brand voice review.
version: 0.1.0
---

# Brand Voice Enforcement

Apply Brand Kit OS brand guidelines to content creation and review. Ensure every piece of content matches the brand's tone, style, and constraints.

## Prerequisites

Before enforcing voice, brand context must be loaded. If no brand context is available in the current session:

1. Call `list_brand_kits` to find available brand kits
2. If one kit exists, load its expression and governance data automatically
3. If multiple kits exist, ask the user which brand to use
4. Call `get_brand_kit_expression` and `get_brand_kit_governance` at minimum

## Enforcement Process

### For New Content Creation

When asked to write content (emails, blog posts, social media, ads, proposals, etc.):

1. **Load context** if not already loaded:
   - Expression data (tone, verbal style, voice archetypes)
   - Governance data (constraints, taboo topics, claims to avoid)
   - Audience data if the content targets a specific persona

2. **Apply voice rules** during writing:
   - Match tone descriptors (e.g., if tone includes "warm" and "professional", write accordingly)
   - Follow formality level setting
   - Respect humor level setting
   - Write at the specified reading level
   - Use sentence structure from verbal style settings
   - Include do-phrases where natural
   - Strictly avoid dont-phrases

3. **Check constraints** before finalizing:
   - Scan for taboo topics -- rewrite any sections that touch them
   - Verify no claims-to-avoid are present
   - Include required disclaimers if applicable
   - Check compliance notes for industry-specific rules

4. **Apply audience targeting** if persona data is loaded:
   - Reference pain points the audience cares about
   - Align with their goals and values
   - Use language appropriate for their channels

### For Content Review

When asked to review existing content for brand compliance:

1. **Load the full governance and expression data**

2. **Score the content** across these dimensions:
   - **Tone alignment** -- does the content match the brand's tone descriptors?
   - **Language compliance** -- are dont-phrases present? Are do-phrases used?
   - **Constraint compliance** -- any taboo topics or forbidden claims?
   - **Audience fit** -- is it appropriate for the target persona?
   - **Style consistency** -- does formality, humor, and reading level match?

3. **Report findings** in a clear format:
   - List specific violations with the exact text that needs changing
   - Suggest replacement text for each violation
   - Note what the content does well (positive reinforcement)

4. **Offer to rewrite** problematic sections while preserving the original meaning

## Voice Application Reference

### Tone Mapping

When the brand expression data includes tone descriptors, map them to writing behavior:

- "professional" -- avoid slang, use industry terminology appropriately, maintain authority
- "warm" -- use inclusive language ("we", "you"), show empathy, be approachable
- "bold" -- use strong verbs, make declarative statements, avoid hedging
- "playful" -- lighter sentence structure, occasional wordplay, conversational
- "authoritative" -- cite specifics, use data, position as expert
- "empathetic" -- acknowledge reader's challenges, validate feelings, offer support

### Formality Levels

- "very formal" -- no contractions, full sentences, traditional structure
- "formal" -- minimal contractions, professional but accessible
- "neutral" -- standard business writing, occasional contractions
- "casual" -- contractions encouraged, conversational flow, shorter sentences
- "very casual" -- colloquial, fragment sentences okay, personality-forward

### Reading Level Adaptation

- "simple" -- short sentences, common words, avoid jargon
- "standard" -- clear prose, explain technical terms when used
- "advanced" -- industry terminology expected, complex sentence structure acceptable
- "expert" -- assume deep domain knowledge, technical precision valued

## Drift Prevention

Over the course of a long conversation, voice consistency can drift. Use these strategies:

- Periodically re-reference the loaded brand context before generating new content
- If the user asks for multiple pieces of content, re-apply voice rules for each one
- When switching between content types (e.g., from email to social post), re-calibrate tone for the new format
- If `drift_prevention_prompts` exist in the governance data, incorporate them as internal reminders

## Content Type Guidelines

### Email
- Lead with the key message
- Match formality to the audience relationship
- Include CTA from the brand's primary_ctas when relevant

### Blog Post
- Use the brand story or positioning as a narrative thread
- Incorporate SEO keywords naturally (load `get_brand_kit_products` for keyword context)
- End with a CTA from the brand kit

### Social Media
- Shorter, punchier application of the brand voice
- Lean into personality traits more heavily
- Use brand keywords as hashtag candidates

### Ad Copy
- Lead with value propositions from products
- Address the primary persona's top pain point
- Use the brand's primary CTA as the action driver

### Proposal / Pitch
- Open with the elevator pitch from messaging
- Emphasize differentiators
- Align with the audience's stated goals
