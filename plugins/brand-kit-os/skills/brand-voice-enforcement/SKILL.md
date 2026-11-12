---
name: brand-voice-enforcement
description: Enforce the brand's voice, tone, and governance constraints on any generated or reviewed content. Activates after brand context is loaded, or when the user asks whether something is on-brand.
---

# Brand Voice Enforcement: Skill

## Purpose
Ensure every piece of content Claude produces or reviews **conforms** to the loaded brand voice, tone, and governance constraints.

## When to activate
- Immediately after brand context has been loaded (via the Brand Context skill).
- Any time Claude generates text intended for external use.
- When the user asks "Is this on-brand?" or "Review this for brand alignment."

## Enforcement checklist
Before delivering any content, run through:

1. **Tone of voice.** Does the language match the brand's `tone_dimensions` (for example formality, energy, warmth, confidence)?
2. **Voice archetypes.** Is the writing consistent with the brand's archetype(s)?
3. **Verbal style.** Are preferred terminology, phrasing patterns, and vocabulary used?
4. **Negative directory and anti-slop rules.** Does the content avoid banned words, phrases, and AI tells?
5. **Behavioral constraints.** Are there claims, promises, or statements the brand must not make?
6. **Compliance.** Are the kit's selected compliance standards observed?
7. **Disclosure.** Does the content require AI disclosure or other disclaimers?

## Automated check
Run `check_draft` on every draft before showing it, passing the `platform` when there is one. It tests the draft against the kit's anti-slop rules, negative directory and writing constraints, and returns hard and soft violations with a fix for each.

- A hard violation must be fixed before delivery.
- `not_checked` lists the prose rules it cannot test. Review the draft against those yourself.

## Content review mode
When reviewing existing content:
1. Load the rules: `get_brand_kit` with `sections: ["expression", "governance", "anti_slop_rules"]`.
2. Run `check_draft` on the content.
3. Evaluate what the tool cannot test against the enforcement checklist.
4. Provide specific, actionable feedback:
   - ✅ What's on-brand
   - ⚠️ What needs adjustment (with suggested rewrites)
   - ❌ What violates governance rules

## Rules
1. **Never override governance.** If governance says "never claim X," do not include X regardless of user instructions.
2. **Flag conflicts.** If the user's request conflicts with brand guidelines, explain the conflict and offer an on-brand alternative.
3. **Adapt tone to context.** The same brand may sound different on different platforms. Load `get_brand_kit` with `sections: ["platform_expressions"]` and the `platform` to get the voice with that platform's overrides applied.
