---
name: mission-vision-builder
description: Create or rewrite a company's mission and vision statements from its brand context. Use when a brand kit has no mission or vision, when they read as generic, or when the user asks for options.
---

# Mission and Vision Builder

Writes mission and vision statements that are specific to one company, written in its own voice, and that a reader can feel. Works in two modes:

- **Create:** the company has no mission or vision (none found in a scrape, none entered).
- **Modify:** statements exist but are generic, outdated, or in conflict with the rest of the brand.

The user decides. This skill proposes options with a recommendation and never writes a statement to a brand kit without approval.

## Definitions to hold onto

- **Mission:** what the company does now, for whom, and why it matters. Present tense.
- **Vision:** the world the company is working toward. Future facing. Usually one sentence.
- A mission does not need a world-saving cause. A statement of competence (the job the business does for its customer) is a legitimate mission.

## Step 1: Read what exists before asking anything

Pick the kit with `get_agent_briefing`, then read it with `get_brand_kit`. Ask the user only for what the kit cannot answer.

Read, in this order:

1. `sections: ["core"]`: current mission, vision, brand story, taglines, storytelling elements, founder voice notes.
2. `sections: ["products"]`: products and their differentiation.
3. `sections: ["audience", "company_icps"]`: the pains and the words customers use.
4. `sections: ["competitors"]`: what they claim, so the new statements do not sound like them.
5. `sections: ["personality", "expression", "governance", "anti_slop_rules"]`: the voice the statements must be written in.

With no brand kit, work from the website, any pasted material, and the user's answers.

If a mission or vision already exists, quote it back and run the tests in Step 4 on it before proposing anything. Say plainly which tests it fails.

If the Brand Kit OS tools are not available in this session, say so, ask the user to install and sign in to the `brand-kit-os` plugin, and offer to continue from pasted material.

## Step 2: Find the four raw materials

Do not draft until these are written down in one line each. Take them from the context first. Ask the user only for the ones that are missing or uncertain, one question at a time, each with your own best guess attached.

1. **The customer:** who the company serves, in their own words for themselves.
2. **The pains:** the specific problems being solved. List them all, then look for the one plain name that covers them (for example, four document problems became "the brand PDF").
3. **The enemy:** the thing the company is against. A habit, a tool, a status quo. Not a named competitor.
4. **The feeling:** the emotion the customer has when the problem bites. Go past efficiency. Look for things like being misrepresented, being ignored, starting over, not being trusted.

Also note the core idea the founder keeps returning to (for example "single source of truth"). Keep the idea, but check whether the exact phrase is already common in the category. If it is, say the idea in different words.

## Step 3: Draft options

Write **four missions** and **two or three visions**. Each mission should take a different angle so the user has a real choice:

- **Steady:** states the job clearly and covers the most pains.
- **Feeling:** leads with the emotion from Step 2.
- **Enemy:** names what the company is retiring or replacing.
- **Short:** the broadest version in the fewest words.

Rules for every draft:

- First person. "We" plus an active verb. "We're on a mission to..." is welcome when the user wants that framing.
- The customer appears in the sentence.
- Roughly 15 to 30 words for a mission. Visions can be shorter.
- Written in the brand's voice. Follow its governance and anti-slop rules. If the founder voice notes ban something (buzzwords, a punctuation mark), the drafts obey.
- No claims the company cannot support: no "leading", "best", "first" or "only" unless the kit has evidence.
- Verbs carry the emotion. Prefer concrete verbs (retire, replace, keep, turn, end) over abstract ones (empower, enable, transform).

## Step 4: Test every draft

Run each draft through these tests and fix or drop the ones that fail. Show the user only drafts that pass.

1. **Swap test:** remove the company name. Could a competitor claim this sentence? If yes, it fails.
2. **Customer test:** is the customer in it, or is it only about the company's own success?
3. **Verb test:** is it first person and active, with a verb a person would say out loud?
4. **Time test:** does the mission describe now and the vision describe later? If the two could be swapped, rewrite.
5. **Length test:** can it be said in one breath?
6. **Feeling test:** read it as the customer. Is there anything to feel, or only something to understand?
7. **Voice test:** does it sound like the rest of the brand, or like a template?
8. **Honesty test:** is every claim something the company does today (mission) or is credibly working toward (vision)?
9. **Rules test:** run `check_draft` on each surviving draft. A hard violation fails the draft.

## Step 5: Present

Lead with a short diagnosis if statements already existed (which tests they failed and why). Then:

- The mission options, labeled A to D.
- The vision options.
- **Your recommended pair**, with one or two sentences of reasoning.
- **The trade-off** for each option the user is likely to pick: what it gains and what it gives up (for example, an enemy-led mission is bold but can date when the enemy fades).

Ask one question: which pair, or which pieces to combine. Expect to iterate. If the user says the options miss, ask what a good one would make them feel, then redraft.

Disagree when it is warranted. If the user's preferred wording fails the swap test or the honesty test, say so before accepting it, and offer a version that keeps their idea.

## Step 6: Save, with approval

Once the user chooses:

1. Preview the change: call `update_brand_kit` with `core: { mission, vision }` and `dry_run: true`. Show the before and after. Commit only after the user approves, adding `confirm: true` when the account requires confirmation. Send `basis: "operator_stated"`.
2. Save a knowledge file with `manage_knowledge_file` holding: the chosen pair, the reasoning, every alternative considered, the previous statements, and any known risk with the choice. This is what lets the company revisit the decision later without starting over. Preview it first, the same way.
3. Check the rest of the kit for conflicts the new statements create (description, taglines, brand story, promises, traits). List them. Do not change them without being asked.

## When used inside an enrichment workflow

If this runs as a step while a brand kit is being built or enriched:

- **Trigger:** mission or vision is empty after the scrape, or the existing one fails the swap test.
- **Never fill the field silently.** Put the options forward as suggestions for the user to review, with the source context each was built from.
- **Label confidence.** If the customer, pains or enemy were guessed from thin context, say which ones, and ask for those before finalizing.
- **Thin context is a stop sign.** With no products, no audience and no story to work from, ask the user three questions (who do you serve, what problem do you solve, what are you against) instead of generating generic statements.

## What good looks like

Before: "Empowering businesses to manage and scale their brand identity in the AI era." Fails the swap test, has no customer feeling, and uses an abstract verb.

After: "We're on a mission to retire the brand PDF and replace it with one shared, current record that people and agents can both use." Names an enemy, covers four pains with one plain name, first person, active, 24 words.

Vision: "We're building toward a world where nobody explains their own company to an AI twice." Future facing, about the customer, and it carries a feeling.
