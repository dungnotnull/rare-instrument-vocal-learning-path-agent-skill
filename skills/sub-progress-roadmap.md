---
name: rare-instrument-vocal-learning-path__sub-progress-roadmap
description: Sub-skill of rare-instrument-vocal-learning-path — Define milestone checkpoints and adjust the path based on progress/plateaus.
---

## Purpose
Define clear milestone checkpoints with measurable success criteria, establish monitoring protocols to track progress, and provide evidence-based adjustment strategies when learners encounter plateaus, setbacks, or unexpected accelerations.

## Input Sources
- `sub-learner-intake` output (goals, timeline)
- `sub-curriculum-builder` output (curriculum stages)
- `sub-practice-scheduler` output (practice structure)
- Progress reports from learner (or assessment data)

## Milestone Framework
Define meaningful checkpoints:

```yaml
milestone_types:
  foundation_milestones:
    description: "Basic technique and mechanics established"
    criteria_type: "competency_checklist"
    assessment: "self_report_or_teacher_assessment"
    examples:
      - "produce_clear_tone_on_all_notes"
      - "execute_basic_scale_patterns"
      - "demonstrate_proper_posture_holding"
  
  skill_integration_milestones:
    description: "Multiple skills combined effectively"
    criteria_type: "performance_tasks"
    assessment: "task_completion_evaluation"
    examples:
      - "perform_etude_with_articulation_dynamics"
      - "synchronize_both_hands_in_passage_work"
      - "apply_technique_in_repertoire_context"
  
  repertoire_milestones:
    description: "Specific pieces learned to performance standard"
    criteria_type: "piece_completion_criteria"
    assessment: "performance_recording_or_live"
    examples:
      - "perform_piece_X_from_memory"
      - "execute_grade_Y_repertoire_requirements"
      - "demonstrate_style_appropriate_interpretation"
  
  theoretical_understanding_milestones:
    description: "Conceptual knowledge demonstrated"
    criteria_type: "knowledge_application"
    assessment: "analysis_or_explanation"
    examples:
      - "analyze_harmonic_structure_of_piece"
      - "explain_technique_theoretical_basis"
      - "identify_key_modulation_and_return"
  
  performance_milestones:
    description: "Public or formal performance achievements"
    criteria_type: "performance_standard"
    assessment: "audience_teacher_evaluation"
    examples:
      - "successful_recital_performance"
      - "exam_submission_meets_criteria"
      - "ensemble_participation_success"
```

## Procedure

### 1. Milestone Sequencing
Order milestones in logical progression:

```yaml
sequencing_principles:
  prerequisite_chain:                # Each milestone enables the next
    - "technique_mechanics_before_repertoire"
    - "foundation_before_advanced_technique"
    - "basic_theory_before_analysis"
    - "piece_learning_before_performance"
  
  concurrent_development:           # Some areas develop in parallel
    - "technique_and_repertoire_together"
    - "theory_anchors_practical_application"
    - "performance_skills_with_repertoire"
  
  spiral_learning:                  # Return to concepts at higher levels
    - "revisit_basic_concepts_in_advanced_contexts"
    - "apply_foundation_to_increasingly_complex_repertoire"
    - "deepen_theoretical_understanding_with_experience"
  
  realistic_pacing:
    - "allow_consideration_for_practice_time"
    - "include_consolidation_periods"
    - "account_for_life_demands"
    - "buffer_for_setbacks_and_plateaus"
```

### 2. Success Criteria Definition
Make milestones measurable:

```yaml
success_criteria_template:
  milestone_id: string
  milestone_name: string
  target_week: number
  
  completion_criteria:
    - criterion: string
      measurement: string
      standard: string
      evidence_type: enum           # "recording" | "teacher_assessment" | "self_check" | "test"
  
  prerequisite_milestones:
    - milestone_id: string
  
  resources_needed:
    - resource: string
      acquisition_source: string
  
  anticipated_challenges:
    - challenge: string
      mitigation_strategies: string[]
```

### 3. Progress Monitoring Protocol
Establish ongoing assessment:

```yaml
monitoring_schedule:
  daily_tracking:
    time_investment:
      metric: "practice_minutes_logged"
      method: "practice_log"
      red_flag: "consistent_under_80percent_of_plan"
    
    objective_progress:
      metric: "daily_objectives_met"
      method: "checkbox_confirmation"
      red_flag: "consistent_objective_failures"
  
  weekly_assessment:
    skill_development:
      metric: "technique_exercises_improvement"
      method: "recording_comparison_or_teacher_notes"
      red_flag: "no_measurable_progress_3weeks"
    
    repertoire_advancement:
      metric: "pieces_or_sections_learned"
      method: "performance_checklist"
      red_flag: "stuck_on_same_section_extended"
    
    practice_quality:
      metric: "focused_effective_practice_ratio"
      method: "self_reflection_on_session_quality"
      red_flag: "mindless_practice_dominating"
  
  milestone_evaluation:
    milestone_attempts:
      metric: "meets_success_criteria"
      method: "formal_assessment_recording_teacher"
      red_flag: "three_failed_attempts"
    
    milestone_timing:
      metric: "weeks_vs_target_week"
      method: "schedule_tracking"
      red_flag: "significantly_behind_schedule"
```

### 4. Plateau Diagnosis & Intervention
Identify and address stagnation:

```yaml
plateau_types:
  technique_plateau:
    indicators:
      - "exercise_speed_stagnated"
      - "tension_persisting_despite_drills"
      - "coordination_not_improving"
    likely_causes:
      - "foundational_gaps"
      - "incorrect_practice_methods"
      - "physical_limitations_compensations"
    interventions:
      - "return_to_foundation"
      - "practice_method_review"
      - "professional_diagnostic"
  
  learning_plateau:
    indicators:
      - "new_concepts_not_sticking"
      - "same_mistakes_recurring"
      - "no_clear_understanding_development"
    likely_causes:
      - "insufficient_practice_quality"
      - "missing_prerequisites"
      - "cognitive_overload"
    interventions:
      - "reduce_complexity"
      - "improve_practice_focus"
      - "alternate_explanation_approach"
  
  motivation_plateau:
    indicators:
      - "practice_consistency_dropping"
      - "goals_losing_meaning"
      - "enthusiasm_declining"
    likely_causes:
      - "unrealistic_initial_expectations"
      - "insufficient_small_wins"
      - "goal_mismatch"
    interventions:
      - "reframe_goals"
      - "create_intermediate_milestones"
      - "add_variety_and_interest"
  
  performance_plateau:
    indicators:
      - "practice_room_success_performance_failure"
      - "nerves_undermining_ability"
      - "inconsistent_quality_under_pressure"
    likely_causes:
      - "insufficient_performance_preparation"
      - "mental_game_development_needed"
      - "incomplete_learning_automization"
    interventions:
      - "mock_performance_schedule"
      - "mental_rehearsal_training"
      - "incremental_performance_pressure"
```

### 5. Adjustment Protocol
Define when and how to modify the path:

```yaml
adjustment_triggers:
  major_adjustments:
    trigger: "multiple_failed_milestone_attempts"
    assessment_period: "6-8_weeks"
    adjustment_options:
      - option: "extend_timeline"
        impact: "reduced_pressure_realistic_pacing"
        effort_level: "low"
        probability_of_success: "high"
      - option: "simplify_curriculum"
        impact: "focus_on_essentials_delay_ancillary"
        effort_level: "medium"
        probability_of_success: "medium"
      - option: "change_approach"
        impact: "alternative_methods_new_perspective"
        effort_level: "high"
        probability_of_success: "variable"
  
  minor_adjustments:
    trigger: "single_milestone_delay"
    assessment_period: "2-3_weeks"
    adjustment_options:
      - option: "shuffle_practice_allocation"
        impact: "more_time_to_challenged_areas"
        effort_level: "low"
        probability_of_success: "medium"
      - option: "add_specific_drills"
        impact: "targeted_weakness_addressing"
        effort_level: "low"
        probability_of_success: "high"
      - option: "temporarily_reduce_complexity"
        impact: "consolidate_before_advancing"
        effort_level: "low"
        probability_of_success: "high"
  
  acceleration_opportunities:
    trigger: "rapid_milestone_achievement"
    assessment_period: "continuous"
    adjustment_options:
      - option: "advance_to_next_milestone"
        impact: "maintain_momentum_challenge"
        effort_level: "low"
        probability_of_success: "medium"
      - option: "add_supplementary_milestones"
        impact: "broader_development_depth"
        effort_level: "medium"
        probability_of_success: "high"
      - option: "introduce_advanced_concepts"
        impact: "enrich_learning_extend_horizons"
        effort_level: "medium"
        probability_of_success: "medium"
```

## Structured Output
```yaml
progress_roadmap:
  milestone_path:
    - milestone:
        id: string
        name: string
        category: enum                # "foundation" | "integration" | "repertoire" | "theory" | "performance"
        target_week: number
        description: string
        success_criteria:
          - criterion: string
            measurement: string
            evidence_type: enum
            standard: string
        dependencies:
          milestone_ids: string[]
        resources:
          - resource: string
            source: string
        risks:
          - risk: string
            mitigation: string
  
  monitoring_protocol:
    daily:
      - metric: string
        measurement_method: string
        recording_frequency: string
        red_flag_threshold: string
        green_flag_indication: string
    
    weekly:
      - assessment: string
        criteria: string[]
        method: string
        adjustment_trigger: string
    
    milestone:
      - evaluation: string
        method: string
        success_definition: string
        failure_consequences: string
  
  plateau_strategies:
    - plateau_type: string
      identification_criteria: string[]
      diagnostic_questions: string[]
      intervention_options:
        - intervention: string
          duration_weeks: number
          expected_impact: string
          implementation_steps: string[]
          evidence_citation: string
          success_indicators: string[]
  
  adjustment_protocol:
    - trigger: string
      assessment_criteria: string[]
      options:
        - option: string
          impact: string
          effort_level: enum
          success_probability: number
          implementation_plan: string[]
      decision_method: string
  
  progress_indicators:
    leading_indicators:
      - indicator: string
        measurement: string
        frequency: enum
        trend_significance: string
    
    lagging_indicators:
      - indicator: string
        measurement: string
        frequency: enum
        milestone_correlation: string
  
  completion_definition:
    final_success_criteria:
      - criterion: string
        verification_method: string
        standard: string
    
    celebration_milestones:
      - milestone: string
        recognition_type: string
    
    next_steps:
      - step: string
        category: enum              # "maintenance" | "advancement" | "new_goal" | "performance"
        recommendation: string
  
  evidence_basis:
    - claim: string
      source: string
      confidence: number
      application: string
  
  flexibility_notes:
    - situation: string
      adaptation: string
      principle_cited: string
```

## Quality Gate
- [ ] Milestones are specific and measurable
- [ ] Success criteria are objective and verifiable
- [ ] Dependencies between milestones are logical
- [ ] Monitoring protocol is actionable
- [ ] Plateau strategies are evidence-linked
- [ ] Adjustment triggers are specific with clear options
- [ ] Progress indicators include both leading and lagging
- [ ] Completion definition is comprehensive
- [ ] Output is structured, not prose-only

## Error Handling
- If timeline is unrealistic for milestones, propose extended or simplified path
- If milestones are too sparse, add intermediate checkpoints
- If learner has limited assessment resources, provide self-assessment alternatives
- If goals are vague during roadmap creation, request clarification

## Special Cases

### Accelerated Learners:
1. Monitor for foundation gaps despite fast progress
2. Offer enrichment rather than just speeding up
3. Ensure consolidation isn't sacrificed for advancement
4. Prepare for higher-level challenges ahead of schedule

### Struggling Learners:
1. Diagnose whether issue is foundation, practice, or motivation
2. Add more frequent, smaller milestones for confidence
3. Increase monitoring and feedback frequency
4. Consider alternative approaches to challenging areas

### Career/Performance-Focused Goals:
1. Prioritize performance milestones over comprehensive coverage
2. Include mock performance and audition preparation
3. Build repertoire strategically for performance contexts
4. Include mental preparation and stage presence development

### Hobby/Personal Growth Goals:
1. Emphasize enjoyment and personal satisfaction metrics
2. Allow more flexible milestone timing
3. Include exploration and variety in repertoire
4. Balance challenge with fun factor

## Integration Notes
This sub-skill provides the tracking and adaptation framework for the entire learning journey. It connects curriculum design to daily practice and enables evidence-based adjustments when reality diverges from plans. The roadmap should be specific enough to guide progress yet flexible enough to adapt to individual learning rates and life circumstances.
