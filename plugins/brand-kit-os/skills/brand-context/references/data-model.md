# Brand Kit OS Data Model Reference

## Brand Kit Structure

Each brand kit contains these related data sections, stored as separate database tables:

### Core Identity (`brand_kit_core`)
- `mission` -- the company's mission statement
- `vision` -- long-term vision
- `brand_story` -- narrative brand story
- `brand_promises` -- array of brand promises/commitments
- `industry_classification_id` -- linked industry category

### Personality (`brand_kit_personality`)
- `trait_ids` -- references to personality trait definitions
- `principle_ids` -- references to brand principles
- `value_ids` -- references to brand values
- `mood_ids` -- references to brand mood/tone settings
- `personality_traits` -- JSONB with detailed trait descriptions
- `brand_values` -- JSONB with detailed value descriptions

### Expression (`brand_kit_expression`)
- `tone_of_voice` -- JSONB with tone descriptors, formality, humor level
- `verbal_style` -- JSONB with sentence structure, vocabulary level, reading level
- `preferred_terminology` -- array of term preferences (use X instead of Y)
- `visual_style` -- JSONB with image style, color preferences
- `voice_archetypes` -- JSONB with selected voice archetype definitions
- `tone_dimensions` -- JSONB with dimensional settings (enthusiasm, assertiveness, etc.)

### Governance (`brand_kit_governance`)
- `behavioral_constraints` -- array of behavioral rules
- `usage_guidelines` -- array of usage rules
- `compliance_notes` -- text compliance/legal notes
- `disclosure_policy` -- text disclosure requirements
- `negative_directory` -- JSONB containing taboo_topics, claims_to_avoid, etc.
- `writing_constraints` -- JSONB with length limits, format rules
- `drift_prevention_prompts` -- JSONB with prompts to keep AI on-brand

### Products (`brand_kit_products`)
Multiple rows per brand kit. Each product has:
- `name`, `description`, `category`
- `features` -- JSONB array of feature descriptions
- `benefits` -- JSONB array of benefit statements
- `pricing_info` -- text pricing details
- `unique_selling_points` -- JSONB array of USPs

### Target Audience (`brand_kit_target_audience`)
Multiple persona rows per brand kit. Each persona has:
- `name`, `title`, `type`
- `is_primary` -- boolean flag for primary persona
- `demographics` -- JSONB with age, location, income, etc.
- `goals` -- JSONB array of goals
- `pain_points` -- JSONB array of pain points
- `values` -- JSONB array of values
- `channels` -- JSONB array of preferred channels

### AI Personas (`brand_kit_personas`)
Multiple rows per brand kit. Custom AI personality configurations:
- `name`, `description`
- `system_prompt` -- the AI persona's system prompt
- `personality_settings` -- JSONB with persona-specific overrides

### Knowledge Files (`user_knowledge_file_uploads`)
Supplementary reference documents:
- `title`, `description`, `file_type`, `tags`
- `brand_kit_id` -- which brand kit this file supports

## Visual Identity (on the brand_kits table directly)
- `primary_color`, `secondary_color`, `accent_color`
- `additional_colors` -- JSONB array
- `heading_font`, `body_font`, `paragraph_font`
- `logo_url`, `logo_dark_url`, `favicon_url`
- `color_details` -- JSONB with light/dark variants
- `tagline`

## Version Tracking
- `brand_kits.version` -- auto-incremented integer on every update
- Use this to detect when cached brand data is stale
