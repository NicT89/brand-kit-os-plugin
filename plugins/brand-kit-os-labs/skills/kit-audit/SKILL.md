---
name: kit-audit
description: Audit a Brand Kit OS brand kit and route each gap to the skill or tool that fixes it. Use when the user asks what is missing, what to fix next, or how to improve their brand kit.
---

# Kit Audit

Finds what is missing or weak in a brand kit and sends each gap to the right fix. This skill detects and routes. It does not write content itself: each fix is done by a builder skill or a Brand Kit OS tool, with the user's approval.

## Step 1: Pick the kit and read its health

1. Call `get_agent_briefing` with no arguments to list the kits. If there is more than one, ask which.
2. Call `get_agent_briefing` with the `brand_kit_id` for section health and the recommended next step.
3. Call `audit_brand_kit` for the full picture. The views are:
   - `completeness` (default): scores every section and lists gaps.
   - `consistency`: cross-checks the kit against itself.
   - `governance_lint`: lists authored fields that break the kit's own writing rules.
   - `next_step`: the single next action in dependency order.

Run `completeness` and `consistency` by default. Add `governance_lint` when the user asks about quality or voice.

If the Brand Kit OS tools are not available in this session, say so and ask the user to install and sign in to the `brand-kit-os` plugin.

## Step 2: Add the checks the audit does not run

The audit scores presence and quality thresholds. It does not judge whether a statement is generic. For these fields, read them and apply the test named:

| Field | Test | If it fails |
|---|---|---|
| Mission and vision | Empty, or a competitor could claim the sentence with the company name removed | Route to the `mission-vision-builder` skill |

More fields are added here as their builder skills ship. Do not invent a test for a field that is not in this table: report what the audit returned and stop there.

## Step 3: Route each gap

Sort gaps by dependency, not by score. Later sections are built from earlier ones, so fix in this order: core, products, audience and company ICPs, competitors, personality and expression, governance, everything else.

| Gap | Route |
|---|---|
| Mission or vision missing or generic | `mission-vision-builder` skill |
| Products thin or missing | `scrape_source` (products) or `enrich_record`, then review |
| No audience personas or company ICPs | `generate_records`, then review |
| Competitors unverified or thin | `enrich_record` for the competitor |
| No customers | Ask the user. Real customers cannot be generated |
| Anything else | Report the gap and what the audit says it requires |

## Step 4: Report

Give the user a short, ordered list:

1. The top three gaps, each with why it matters and the fix.
2. What can be fixed now, and what needs something only they have (real customers, a decision, a document).
3. One question: which gap to start on.

Keep the scores out of the headline. A kit can score high on completeness and still read as generic, and the report should say so when that is the case.

## Rules

1. **Detect, do not generate.** This skill never writes brand content. It hands off.
2. **Nothing is written without approval.** Every fix previews first with `dry_run: true` and commits only after the user approves.
3. **Jobs that spend credits are named as such** before they run.
4. **Do not pad.** If the kit is in good shape, say that and name the one thing that would improve it most.
