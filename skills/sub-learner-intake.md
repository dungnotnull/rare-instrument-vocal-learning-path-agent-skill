---
name: rare-instrument-vocal-learning-path__sub-learner-intake
description: Sub-skill of rare-instrument-vocal-learning-path — Capture instrument/voice type, current level, goals, practice time, equipment and any physical limitations.
---

## Purpose
Capture structured learner profile for rare instrument or vocal technique learning, ensuring all required information is gathered before analysis begins. Validate constraints and flag risk factors that may affect learning path safety or feasibility.

## Input Sources
- Direct user responses
- Prior harness stage outputs (if any)
- `SECOND-KNOWLEDGE-BRAIN.md` for domain reference

## Required Information Schema
The intake MUST collect the following before proceeding to analysis:

```yaml
learner_profile:
  # Core domain identification
  target_instrument_voice: string    # "hurdy-gurdy", "belting", "flute", etc.
  domain_type: enum                  # "instrument" | "vocal_technique" | "instrument_technique"
  
  # Current proficiency
  current_level: enum                # "none" | "beginner" | "intermediate" | "advanced"
  months_experience: number?         # Optional: months in this domain
  prior_training: string[]?          # Formal training, lessons, workshops
  
  # Learning objectives
  primary_goal: string               # Main outcome (e.g., "perform basic melodies", "sing belt safely")
  secondary_goals: string[]?         # Additional objectives
  target_milestone: string?          # Specific milestone (e.g., "ABRSM Grade 5", "perform 2-hour gig")
  timeline_weeks: number?            # Target weeks (if specified)
  
  # Practice constraints
  daily_practice_minutes: number     # Available daily practice time
  practice_frequency: enum           # "daily" | "5x_weekly" | "3x_weekly" | "2x_weekly" | "weekly"
  preferred_schedule: string?       # "mornings", "evenings", "weekends"
  
  # Equipment and resources
  equipment_owned: string[]         # Instrument, accessories, recording device, etc.
  equipment_access: string[]?        # What they can borrow or access
  budget_level: enum?                # "none" | "minimal" | "moderate" | "flexible"
  
  # Physical and safety factors
  physical_limitations: string[]     # Injuries, conditions, mobility issues
  vocal_health_history: string[]?   # For vocal: nodules, polyps, strain history
  age: number?                       # Important for vocal development and repertoire
  
  # Learning preferences
  learning_style: enum?              # "visual" | "auditory" | "kinesthetic" | "reading"
  feedback_preference: enum          # "self" | "peer" | "teacher" | "automated"
  
  # Context
  motivation_factors: string[]       # Why they want to learn this
  performance_context: string?       # "hobby" | "semi-pro" | "professional" | "academic"
```

## Procedure

### 1. Initial Assessment
- Read any existing context from prior stages
- Check for already-provided information
- Identify missing required fields

### 2. Targeted Information Gathering
For each missing required field, ask specific questions:

**Instrument/Voice Type:**
- "What specific instrument or vocal technique are you interested in learning?"
- "Is this for a new instrument/technique, or improving existing skills?"

**Current Level:**
- "Describe your current experience with this instrument/technique."
- "Have you had any formal training or lessons?"

**Goals:**
- "What is your primary goal? (e.g., perform a specific piece, pass an exam, develop a technique)"
- "Is there a specific timeline or milestone you're aiming for?"

**Practice Constraints:**
- "How much time can you realistically practice daily, in minutes?"
- "How many days per week can you practice?"

**Equipment:**
- "What instrument/equipment do you currently have?"
- "Do you have access to additional equipment or resources?"

**Physical/Safety:**
- "Do you have any physical limitations, injuries, or health conditions I should be aware of?"
- For vocal: "Any history of vocal strain, nodules, or other voice health concerns?"

### 3. Constraint Validation
Before passing to analysis, validate:

**Timeline Feasibility Check:**
- If timeline_weeks is specified AND daily_practice_minutes is known:
  - Calculate total practice hours = (daily_practice_minutes / 60) * practice_frequency_per_week * timeline_weeks
  - Flag if total < deliberate practice minimum for goal (typically 100-1000 hours depending on complexity)
  - Return warning if unrealistic

**Equipment Sufficiency:**
- Check if basic equipment requirements for target_instrument_voice are met
- Flag critical gaps (e.g., no instrument for instrumental learning)

**Age Appropriateness:**
- For vocal: check if repertoire/technique is age-appropriate
- Flag if heavy vocal techniques before age 18 (developmental concern)

**Physical Risk:**
- Flag high-risk combinations (e.g., belt technique with vocal injury history)
- Recommend medical consultation when appropriate

### 4. Structured Output Generation
Emit a JSON-structured intake result:

```json
{
  "status": "complete" | "incomplete" | "conflict_detected",
  "learner_profile": { /* full schema above */ },
  "validation_flags": {
    "timeline_feasible": boolean,
    "equipment_sufficient": boolean,
    "age_appropriate": boolean,
    "physical_risk_level": "none" | "low" | "medium" | "high" | "critical"
  },
  "clarifying_questions": [ /* if incomplete */ ],
  "warnings": [ /* if conflicts */ ],
  "confidence_score": 0.0-1.0
}
```

### 5. Evidence Linking
Attach sources for any claims made:
- Age-appropriateness guidelines from vocal pedagogy sources
- Equipment requirements from instrument method books
- Deliberate practice hour estimates from Ericsson research

## Quality Gate
Before passing to next stage:
- [ ] All required fields collected OR clarifying questions documented
- [ ] Constraint validation performed
- [ ] Risk factors flagged and documented
- [ ] Output is structured (JSON/YAML), not prose-only
- [ ] Each material claim cites source OR marks assumption

## Output Schema
```yaml
intake_result:
  status: enum                      # "complete" | "incomplete" | "conflict_detected"
  learner_profile: <full_schema>
  validation_flags:
    timeline_feasible: boolean
    equipment_sufficient: boolean
    age_appropriate: boolean
    physical_risk_level: enum
  clarifying_questions:
    - question: string
      field: string                  # Which field this question targets
      optional: boolean
  warnings:
    - warning: string
      severity: enum                 # "info" | "caution" | "critical"
      recommendation: string
  confidence_score: number           # Based on completeness and specificity
  evidence_citations:
    - claim: string
      source: string
      url: string?
```

## Error Handling
- If user provides inconsistent information, flag as "conflict_detected" and ask specific clarification questions
- If user refuses to provide required field, document as assumption and proceed with explicit disclaimer
- If critical safety issue detected, recommend consulting professional before continuing

## Domain-Specific Extensions

### For Instruments:
- Add instrument-specific equipment questions (reeds, mouthpieces, bows, etc.)
- Ask about access to maintenance/repair
- Consider physical requirements (posture, arm span, lung capacity for winds)

### For Vocal Techniques:
- Ask about current warm-up routine
- Inquire about performance contexts (solo, choir, theater)
- Screen for vocal health red flags (pain, fatigue, loss of range)

### For Advanced Techniques:
- Assess foundation skills first
- Verify prerequisite capabilities
- Check for appropriate preparation for advanced work

## Integration Notes
This sub-skill is called FIRST in the harness flow. Its output becomes the foundation for all subsequent analysis. Incomplete or low-confidence intake results should trigger targeted questions rather than proceeding with assumptions.
