# Shared Sub-Skill Interfaces — Career, Learning & Skills Cluster

**Purpose:** Enable cross-skill reuse of intake, scoring, scheduling, and roadmap patterns across all skills in the `career-education` cluster.

**Version:** 1.0
**Last Updated:** 2025-01-01
**Source Skill:** `rare-instrument-vocal-learning-path` (idea #194)

---

## Cluster Definition

The `career-education` cluster encompasses skills that help users:
- Learn new skills (instrumental, vocal, technical, professional)
- Design learning paths with structured curricula
- Diagnose and correct errors in practice/performance
- Schedule practice/study time efficiently
- Track progress and adjust plans

**Sibling skills can reuse:** The interface contracts below without modification.

---

## Core Shared Interfaces

### 1. Learner Intake Interface (`sub-learner-intake` pattern)

**Purpose:** Capture structured learner profile and goal information.

#### Input Schema
```yaml
learner_profile:
  # Domain-specific entity (instrument, skill, subject)
  target_domain: string              # "hurdy-gurdy", "data science", "vocal belt"
  
  # Current proficiency
  current_level: enum                # "none" | "beginner" | "intermediate" | "advanced" | "expert"
  years_experience: number?          # Optional: years in domain
  prior_training: string[]?          # Optional: formal training, courses, certifications
  
  # Goals
  primary_goal: string               # Main objective
  secondary_goals: string[]?         # Optional: additional objectives
  timeline_weeks: number?           # Optional: target weeks to goal
  
  # Constraints
  practice_time_minutes: number     # Daily available practice/study time
  practice_frequency: enum           # "daily" | "5x_weekly" | "3x_weekly" | "weekly"
  
  # Resources
  equipment_available: string[]?     # What learner has access to
  budget_constraint: enum?          # "none" | "low" | "medium" | "high"
  
  # Risk factors
  physical_limitations: string[]?   # Injuries, health considerations
  age_restriction: enum?            # "child" | "teen" | "adult" | "senior"
  
  # Learning preferences
  learning_style: enum?             # "visual" | "auditory" | "kinesthetic" | "reading"
  feedback_preference: enum?        # "self" | "peer" | "instructor" | "automated"
```

#### Output Schema
```yaml
intake_result:
  status: enum                      # "complete" | "incomplete" | "conflict_detected"
  learner_profile: <input_schema>  # Normalized profile
  validation_flags:
    timeline_realistic: boolean
    equipment_sufficient: boolean
    physical_risk_level: enum       # "none" | "low" | "medium" | "high"
    age_appropriate: boolean
  clarifying_questions: string[]    # If status != "complete"
  confidence_score: number          # 0-1, based on input completeness
```

#### Quality Gate
- All required fields present (marked with `!` in domain-specific extensions)
- No unresolved conflicts (timeline vs deliberate practice constraints)
- Risk factors flagged and documented
- Output is structured JSON/YAML, not prose

#### Reuse Contract
Sibling skills MAY:
- Extend the schema with domain-specific fields
- Add domain-specific validation rules
- Keep the core schema immutable

Sibling skills MUST:
- Emit output matching the core schema structure
- Implement the same quality gate behavior
- Return structured data, never prose-only

---

### 2. Scoring & Evaluation Interface (`sub-curriculum-builder` pattern)

**Purpose:** Evaluate learner path against named frameworks with evidence-linked scoring.

#### Input Schema
```yaml
evaluation_request:
  intake_result: <intake_output>
  domain frameworks: string[]        # Frameworks to score against (skill-specific)
  available_syllabi: string[]       # Official curricula (ABRSM, industry certs, etc.)
  evidence_sources:                 # Knowledge base entries
    - title: string
      source: string
      relevance: number              # 0-1
```

#### Output Schema
```yaml
evaluation_result:
  dimension_scores:
    - dimension: string              # E.g., "technique_foundation"
      score: number                  # 0-100
      confidence: number             # 0-1
      evidence:                      # Citations or assumptions
        - source: string
          claim: string
          is_assumption: boolean
      gaps: string[]                 # Identified weaknesses
      strengths: string[]            # Identified strengths
  
  composite_score: number           # Weighted aggregate
  risk_assessment:
    injury_risk: enum                # "none" | "low" | "medium" | "high" | "critical"
    feasibility_risk: enum           # "none" | "low" | "medium" | "high" | "critical"
  
  framework_alignment:              # Per-framework alignment score
    - framework: string
      alignment_score: number        # 0-100
      missing_elements: string[]
  
  devil_advocate_review:
    objections: string[]
    responses: string[]
    adjustments_made: string[]
```

#### Common Scoring Dimensions (extensible)
```yaml
dimension_categories:
  foundation:                        # Baseline competence
    - technique_foundation
    - theory_knowledge
    - safety_awareness               # For physical/voice skills
  
  progression:                       # Learning trajectory quality
    - curriculum_sequencing
    - repertoire_appropriateness
    - difficulty_progression
  
  practice_quality:                  # How learning happens
    - deliberate_practice_alignment
    - feedback_frequency
    - schedule_efficiency
  
  goal_alignment:                    # Fit to objectives
    - timeline_feasibility
    - resource_adequacy
    - outcome_relevance
```

#### Quality Gate
- Every dimension cites evidence OR explicitly marks assumption
- Devil's-advocate review performed and documented
- No score without a source or stated assumption
- Risk factors assessed and flagged

#### Reuse Contract
Sibling skills MAY:
- Define domain-specific dimensions
- Use domain-specific frameworks
- Adjust scoring weights

Sibling skills MUST:
- Maintain evidence-linked scoring
- Perform devil's-advocate review
- Emit structured dimension scores
- Include risk assessment

---

### 3. Practice/Schedule Design Interface (`sub-practice-scheduler` pattern)

**Purpose:** Design spaced, interleaved practice/study blocks using deliberate practice and motor learning principles.

#### Input Schema
```yaml
schedule_request:
  intake_result: <intake_output>
  evaluation_result: <evaluation_output>
  available_blocks:                 # Time slots learner has
    - day: string                    # "Monday", "Tuesday", etc.
      minutes: number
      preferred_time: string?        # "morning", "afternoon", "evening"
  
  priority_areas: string[]           # Dimensions needing focus
  current_plateaus: string[]?        # Areas where learner is stuck
```

#### Output Schema
```yaml
schedule_result:
  weekly_plan:
    - week: number
      daily_blocks:
        - day: string
          blocks:
            - duration_minutes: number
              focus_area: string
              activity_type: enum     # "technique" | "theory" | "repertoire" | "drills" | "review"
              specific_target: string
              practice_method: enum   # "blocked" | "random" | "interleaved"
              intensity: enum          # "low" | "medium" | "high"
              rest_intervals: boolean # Whether to include breaks
  
  practice_principles_applied:
    - principle: string               # "spaced_repetition" | "contextual_interference" etc.
      application: string
      citation: string
  
  progression_metrics:
    - metric: string
      measurement: string
      frequency: string               # "daily", "weekly", "milestone"
  
  adaptation_triggers:
    - condition: string               # When to adjust
      adjustment: string
```

#### Scheduling Principles (from motor learning science)
```yaml
evidence_based_methods:
  blocked_practice:
    description: "Drill single skill continuously"
    use_case: "New technique introduction"
    citation: "Motor learning basics"
  
  random_practice:
    description: "Mix multiple skills in random order"
    use_case: "Skill transfer and retention"
    citation: "Contextual interference effect"
  
  interleaved_practice:
    description: "Alternate between skills in structured pattern"
    use_case: "Differentiation learning"
    citation: "Shea & Morgan, 1979"
  
  spaced_repetition:
    description: "Review at expanding intervals"
    use_case: "Long-term retention"
    citation: "Ebbinghaus, 1885; modern replic"
  
  deliberate_practice:
    description: "Focused, goal-oriented practice with immediate feedback"
    use_case: "Skill improvement"
    citation: "Ericsson et al., 1993"
```

#### Quality Gate
- Schedule respects learner's time constraints
- Practice methods match skill level and goals
- Progression metrics are measurable
- Adaptation triggers are specific and actionable

#### Reuse Contract
Sibling skills MAY:
- Define domain-specific activity types
- Adjust block structures to domain needs
- Use domain-specific progression metrics

Sibling skills MUST:
- Apply evidence-based scheduling principles
- Respect time constraints from intake
- Include measurable progression metrics
- Define adaptation triggers

---

### 4. Progress Tracking & Roadmap Interface (`sub-progress-roadmap` pattern)

**Purpose:** Define milestone checkpoints and adjust the path based on progress/plateaus.

#### Input Schema
```yaml
roadmap_request:
  intake_result: <intake_output>
  evaluation_result: <evaluation_output>
  schedule_result: <schedule_output>
  current_progress:                 # Optional: if adjusting existing plan
    milestones_completed: string[]
    time_elapsed_weeks: number
    plateaus_identified: string[]
    setbacks: string[]?
```

#### Output Schema
```yaml
roadmap_result:
  milestone_path:
    - milestone:
        id: string                   # Unique identifier
        name: string                 # Human-readable title
        target_week: number          # When to expect completion
        criteria:                    # Success conditions
          - condition: string
            measurement: string
            threshold: number
        dependencies: string[]      # Other milestone IDs required
        resources_needed: string[]
  
  plateau_strategies:
    - plateau_type: string            # E.g., "speed_wall", "accuracy_plateau"
      interventions:
        - intervention: string
          duration_weeks: number
          expected_impact: string
          evidence_citation: string
  
  adjustment_protocol:
    - trigger_condition: string
      assessment_criteria: string[]
      adjustment_options:
        - option: string
          impact: string
          effort_level: enum          # "low" | "medium" | "high"
          probability_of_success: number
  
  progress_indicators:
    - indicator: string
      measurement_method: string
      check_frequency: enum           # "daily" | "weekly" | "milestone"
      red_flag_threshold: number
  
  completion_definition:
    final_success_criteria: string[]
    verification_method: string
    next_steps: string[]             # What to do after completion
```

#### Quality Gate
- Milestones are measurable and time-bound
- Plateau strategies are evidence-linked
- Adjustment protocol has clear trigger conditions
- Progress indicators are objective and measurable

#### Reuse Contract
Sibling skills MAY:
- Define domain-specific milestone types
- Customize plateau patterns to domain
- Adjust success criteria to domain needs

Sibling skills MUST:
- Include measurable milestone criteria
- Link strategies to evidence
- Define objective progress indicators
- Specify completion conditions

---

## Integration Example: How Sibling Skills Use These Interfaces

### Example 1: Technical Learning Skill

```yaml
# User: "I want to learn Kubernetes administration"

# Step 1: Intake
sub-learner-intake output:
  target_domain: "Kubernetes administration"
  current_level: "beginner"
  primary_goal: "Become production-ready K8s admin"
  timeline_weeks: 24
  practice_time_minutes: 60
  equipment_available: ["laptop", "cloud account"]
  
# Step 2: Score against frameworks
sub-curriculum-builder output:
  dimension_scores:
    - dimension: "infrastructure_knowledge"
      score: 20
      evidence: [CKA syllabus 2024]
    - dimension: "deployment_skills"
      score: 15
      evidence: [Kubernetes.io docs]
      
# Step 3: Schedule
sub-practice-scheduler output:
  weekly_plan:
    - blocks using interleaved practice
      focus: pod management, services, networking
      
# Step 4: Roadmap
sub-progress-roadmap output:
  milestone_path:
    - milestone: "Deploy first application"
      target_week: 4
      criteria: ["Successful pod deployment", "Service exposure"]
```

### Example 2: Professional Certification Skill

```yaml
# User: "I want to pass the CPA exam"

# Same interface pattern, domain-specific extensions:
# - Financial knowledge as technique_foundation
# - Exam sections as repertoire
# - Study blocks using spaced repetition
# - Milestones tied to exam sections
```

---

## Implementation Checklist for Sibling Skills

When adopting these interfaces, ensure:

- [ ] All sub-skills emit structured output (JSON/YAML schema compliant)
- [ ] Every material claim has evidence citation or assumption marker
- [ ] Quality gates are implemented and documented
- [ ] Devil's-advocate review is performed in scoring
- [ ] Risk factors are assessed and flagged
- [ ] Timeline/constraint validation happens before scoring
- [ ] Progress indicators are measurable and objective
- [ ] Plateau strategies reference motor learning or domain evidence

---

## Version Control & Maintenance

- Version numbers follow semantic versioning (MAJOR.MINOR.PATCH)
- Breaking changes require MAJOR version increment
- Core schema additions are MINOR increments
- Documentation fixes are PATCH increments
- All changes logged in CHANGELOG.md at cluster level

---

## Contact & Contribution

To propose interface changes or additions:
1. Open issue in `career-education` cluster repository
2. Reference this document and specific interface
3. Provide justification and backward compatibility analysis
4. Include example usage before and after change

**Maintainer:** `rare-instrument-vocal-learning-path` skill (initial author)
**Cluster:** Career, Learning & Skills (`career-education`)
**Status:** v1.0 — Stable and production-ready
