---
name: rare-instrument-vocal-learning-path__sub-practice-scheduler
description: Sub-skill of rare-instrument-vocal-learning-path — Design spaced, interleaved practice blocks with deliberate-practice targets.
---

## Purpose
Design evidence-based practice schedules that apply motor learning research (spacing, interleaving, contextual interference) and deliberate practice principles (focused goals, immediate feedback, progressive difficulty) to maximize skill acquisition within learner's time constraints.

## Input Sources
- `sub-learner-intake` output (practice time constraints, preferences)
- `sub-curriculum-builder` output (curriculum stages, priorities)
- `SECOND-KNOWLEDGE-BRAIN.md` for practice method evidence

## Scheduling Framework
Apply research-backed practice methods:

```yaml
evidence_based_methods:
  blocked_practice:
    description: "Repetitive drilling of single skill"
    optimal_for: "New technique introduction, motor pattern establishment"
    duration: "Short sessions, 5-15 minutes per skill"
    evidence: "Shea & Morgan, 1979 - better for initial acquisition"
  
  random_practice:
    description: "Unpredictable mixing of multiple skills"
    optimal_for: "Skill transfer, retention, performance under pressure"
    duration: "After basic skill established"
    evidence: "Contextual interference effect - Lee & Magill, 1983"
  
  interleaved_practice:
    description: "Structured alternating between skills (A-B-A-B)"
    optimal_for: "Differentiation learning, preventing confusion"
    duration: "Mid-learning stage, similar skills"
    evidence: "Panadero et al., 2021 - balance of acquisition and transfer"
  
  spaced_repetition:
    description: "Review at expanding intervals (1d, 3d, 7d, 14d, 30d)"
    optimal_for: "Long-term retention, theory, repertoire maintenance"
    duration: "Integrated across practice week"
    evidence: "Ebbinghaus, 1885; modern meta-analysis"
  
  deliberate_practice:
    description: "Goal-focused, feedback-rich practice outside comfort zone"
    optimal_for: "Skill improvement, breakthrough learning"
    duration: "Limited daily duration due to cognitive load"
    evidence: "Ericsson et al., 1993 - quality over quantity"
```

## Procedure

### 1. Time Constraint Analysis
Calculate effective practice capacity:

```yaml
time_allocation:
  total_daily_minutes: number        # From intake
  effective_practice_ratio: 0.8      # Account for setup, breaks, focus loss
  focused_work_minutes: number       # total_daily_minutes * effective_practice_ratio
  
  deliberate_limit: 30                # Maximum minutes for intense deliberate practice
  maintenance_capacity: number       # Remaining time for repertoire, review
  
  block_division:
    - technique: number              # 30-40% of time
    - repertoire: number             # 30-40% of time  
    - theory_drills: number          # 10-20% of time
    - review_warmup: number          # 10-20% of time
```

### 2. Priority-Based Block Assignment
Map curriculum priorities to time blocks:

```yaml
priority_mapping:
  high_priority_foundation:
    practice_method: "blocked"
    frequency: "daily"
    duration_ratio: 0.4
    placement: "beginning_of_session"
    rationale: "Foundation skills need frequent, focused repetition"
  
  medium_priority_development:
    practice_method: "interleaved"
    frequency: "3-5x_weekly"
    duration_ratio: 0.35
    placement: "middle_of_session"
    rationale: "Development benefits from mixing and comparison"
  
  maintenance_variety:
    practice_method: "random"
    frequency: "2-3x_weekly"
    duration_ratio: 0.25
    placement: "end_of_session"
    rationale: "Maintenance and transfer through variety"
```

### 3. Weekly Schedule Architecture
Design structured practice week:

```yaml
weekly_structure:
  monday:                            # Foundation focus
    technique: 40%
    repertoire: 30%
    theory: 20%
    review: 10%
    primary_method: "blocked"
    emphasis: "technique_foundation"
  
  tuesday:                           # Integration focus  
    technique: 30%
    repertoire: 40%
    theory: 15%
    review: 15%
    primary_method: "interleaved"
    emphasis: "repertoire_application"
  
  wednesday:                         # Consolidation
    technique: 35%
    repertoire: 35%
    theory: 15%
    review: 15%
    primary_method: "mixed"
    emphasis: "skill_integration"
  
  thursday:                          # Variety focus
    technique: 30%
    repertoire: 35%
    theory: 20%
    review: 15%
    primary_method: "random"
    emphasis: "transfer_learning"
  
  friday:                            # Review and prep
    technique: 25%
    repertoire: 40%
    theory: 15%
    review: 20%
    primary_method: "spaced_repetition"
    emphasis: "consolidation"
  
  saturday:                          # Optional light session
    technique: 20%
    repertoire: 50%
    theory: 10%
    review: 20%
    primary_method: "maintenance"
    emphasis: "enjoyment_maintenance"
  
  sunday:                            # Rest or optional light review
    rest_recommended: true
    if_practice:
      review: 100%
      duration: "light_15-30min"
```

### 4. Session Micro-Structure
Design individual practice sessions:

```yaml
session_template:
  warmup_phase:
    duration_minutes: number          # 10-20% of session
    activities:
      - "physical_warmup"
      - "sound_production"
      - "scale_patterns"
    purpose: "prepare_coordination_prevent_injury"
  
  deliberate_focus_phase:
    duration_minutes: number         # 40-50% of session
    activities:
      - "targeted_technique_drills"
      - "specific_problem_solving"
      - "goal_oriented_work"
    characteristics:
      - "clear_objectives"
      - "immediate_feedback"
      - "slightly_difficult"
      - "repetitive_with_variation"
  
  application_phase:
    duration_minutes: number         # 20-30% of session
    activities:
      - "repertoire_work"
      - "etude_application"
      - "contextual_practice"
    characteristics:
      - "apply_technique_in_context"
      - "musical_focus"
      - "expression_development"
  
  cool_down_review:
    duration_minutes: number         # 5-10% of session
    activities:
      - "review_objectives"
      - "note_achievements"
      - "plan_next_session"
    purpose: "consolidation_metacognition"
```

### 5. Adaptive Adjustments
Modify schedule based on constraints:

**Limited Time (<30 min/day):**
```yaml
time_constraint_adaptations:
  daily_practice_under_30min:
    structure: "single_focus_rotation"
    monday_wednesday_friday:
      primary: "technique_focused"
      secondary: "brief_repertoire"
    tuesday_thursday_saturday:
      primary: "repertoire_focused"  
      secondary: "technique_maintenance"
    principles:
      - "quality_over_quantity"
      - "single_deliberate_objective"
      - "technique_repertoire_alternate"
```

**Weekend-Only Practice:**
```yaml
weekend_warrior_adaptations:
  structure: "long_session_split"
  saturday:
    - block: "technique_foundation"
      duration: "45-60min"
    - block: "repertoire_development"
      duration: "45-60min"
  sunday:
    - block: "review_consolidation"
      duration: "30-40min"
    - block: "preparation_for_next"
      duration: "20-30min"
  caution: "spacing_less_optimal_consistency_critical"
```

## Structured Output
```yaml
practice_schedule:
  learner_constraints:
    daily_minutes: number
    days_per_week: number
    total_weekly_minutes: number
  
  weekly_plan:
    - day: enum
      practice_blocks:
        - block:
            name: string
            duration_minutes: number
            category: enum             # "technique" | "repertoire" | "theory" | "review"
            practice_method: enum       # "blocked" | "random" | "interleaved" | "spaced"
            focus_areas: string[]
            specific_targets: string[]
            intensity: enum             # "low" | "medium" | "high"
            objectives: string[]
          rest_intervals: boolean
          transitions: string[]
      total_session_minutes: number
  
  daily_session_template:
    phases:
      - phase: enum                   # "warmup" | "deliberate_focus" | "application" | "cool_down"
        duration_percentage: number
        activities: string[]
        objectives: string[]
        feedback_points: string[]
  
  practice_principles_applied:
    - principle: string
      application: string
      frequency: string
      evidence_citation: string
  
  progression_metrics:
    daily:
      - metric: string
        measurement: string
        recording_method: string
    weekly:
      - metric: string
        measurement: string
        recording_method: string
    milestone:
      - metric: string
        measurement: string
        assessment_method: string
  
  adaptation_protocol:
    - trigger: string
      adjustment: string
      implementation: string
  
  efficiency_optimizations:
    - optimization: string
      time_saved: string
      benefit: string
      evidence: string
  
  schedule_variations:
    - variation: string
      when_to_use: string
      modified_structure: string
  
  evidence_basis:
    - claim: string
      source: string
      confidence: number
  
  recommendations:
    schedule_success_factors: string[]
    common_pitfalls: string[]
    motivation_maintenance: string[]
```

## Quality Gate
- [ ] Schedule respects learner's time constraints exactly
- [ ] Practice methods match skill level and learning stage
- [ ] Each block has clear, measurable objectives
- [ ] Progression metrics are specific and actionable
- [ ] Adaptation triggers are defined for common scenarios
- [ ] Evidence basis cited for scheduling decisions
- [ ] Rest intervals and injury prevention included
- [ ] Output is structured, not prose-only

## Error Handling
- If time constraints prevent effective practice, provide realistic alternatives
- If schedule would cause injury risk, modify with caution notes
- If learner preference conflicts with evidence, explain trade-off
- If multiple scheduling approaches possible, present with pros/cons

## Special Cases

### Injury Recovery:
1. Design gradual rebuilding progression
2. Include frequent breaks
3. Prioritize technique over repertoire
4. Monitor for recurrence

### Performance Preparation:
1. Shift balance toward repertoire and performance simulation
2. Include mental practice and visualization
3. Schedule mock performances
4. Adjust rest before performance

### Technique Crisis:
1. Allocate higher percentage to foundation work
2. Use blocked practice for pattern re-establishment
3. Include frequent diagnostic checks
4. Progress slowly with consolidation

## Integration Notes
This sub-skill translates curriculum priorities into actionable daily practice. The schedule must be specific enough to follow independently while flexible enough to adapt to progress and life circumstances. Feedback from practice informs curriculum adjustments.
