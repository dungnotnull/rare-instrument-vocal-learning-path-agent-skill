---
name: rare-instrument-vocal-learning-path__sub-technique-diagnostic
description: Sub-skill of rare-instrument-vocal-learning-path — Diagnose errors from user description/recording notes and map to corrective drills (motor-learning informed).
---

## Purpose
Analyze technique problems described by learners (or from performance notes), identify root causes using motor learning and pedagogy frameworks, and prescribe targeted corrective drills that address the specific issue with evidence-based practice methods.

## Input Sources
- User descriptions of problems ("I'm struggling with fast passages", "My high notes sound thin")
- Performance notes or feedback ("teacher says my articulation is unclear")
- Recording notes (from learner self-assessment or instructor feedback)
- `sub-learner-intake` output for context
- `SECOND-KNOWLEDGE-BRAIN.md` for diagnostic patterns

## Problem Taxonomy
Classify reported issues into diagnostic categories:

```yaml
diagnostic_categories:
  technique_mechanics:
    examples:
      - "posture/tension issues"
      - "finger coordination"
      - "breath support"
      - "embouchure/mouthpiece issues"
      - "bow control/stroke"
    root_cause_frameworks:
      - "motor_pattern_disruption"
      - "compensatory_tension"
      - "insufficient_foundation"
  
  timing_rhythm:
    examples:
      - "rush or drag tempo"
      - "uneven rhythm"
      - "subdivision struggles"
      - "syncopation difficulty"
    root_cause_frameworks:
      - "internal_pulse_development"
      - "subdivision_awareness"
      - "metronome_dependence"
  
  sound_quality:
    examples:
      - "thin/tone quality"
      - "intonation issues"
      - "dynamic control"
      - "tone_color"
    root_cause_frameworks:
      - "resonance_understanding"
      - "physical_coordination"
      - "auditory_feedback_loop"
  
  musicality_phrasing:
    examples:
      - "lack of direction"
      - "mechanical playing"
      - "phrase shaping"
      - "style interpretation"
    root_cause_frameworks:
      - "structural_awareness"
      - "expressive_concept"
      - "gesture_understanding"
  
  anxiety_performance:
    examples:
      - "nervous tempo"
      - "memory slips"
      - "physical tension performing"
      - "focus/concentration"
    root_cause_frameworks:
      - "performance_psychology"
      - "preparation_adequacy"
      - "mental_rehearsal"
  
  plateau_stagnation:
    examples:
      - "stuck at current level"
      - "no progress despite practice"
      - "repeating same mistakes"
      - "loss of motivation"
    root_cause_frameworks:
      - "practice_efficiency"
      - "deliberate_focus"
      - "overlearning_plateau"
```

## Diagnostic Procedure

### 1. Problem Clarification
Gather specific information:

**Essential Details:**
- "What specifically happens when you attempt this?"
- "When did this problem first appear?"
- "What have you already tried to fix it?"
- "What does your teacher say about this?" (if applicable)

**Context Gathering:**
- "Does this happen consistently or intermittently?"
- "Is it worse at certain tempos or registers?"
- "Does fatigue or stress affect it?"
- "Are there specific passages where it's most problematic?"

### 2. Root Cause Analysis
Apply frameworks to identify likely causes:

**Motor Learning Perspective:**
- Is this a flawed motor pattern requiring re-learning?
- Would blocked or random practice be more effective?
- Is the issue insufficient repetition or overloaded complexity?
- Are transfer effects being blocked by interference?

**Pedagogical Perspective:**
- Is the learner attempting skills beyond foundation?
- Are prerequisites missing or incomplete?
- Is the problem actually a symptom of a different issue?
- Would scaffolding or isolation exercises help?

**Physical/Safety Perspective:**
- Is there compensatory tension causing the issue?
- Could fatigue or overuse be contributing?
- Is the current approach risking injury?
- Should medical consultation be recommended?

### 3. Evidence-Based Drill Prescription
Map diagnosis to targeted interventions:

**Drill Design Framework:**
```yaml
drill_structure:
  name: string
  category: enum                    # "isolation" | "integration" | "transfer"
  difficulty: enum                  # "foundation" | "intermediate" | "advanced"
  
  target_skill: string              # What specifically this addresses
  root_cause: string                 # Which problem pattern it corrects
  
  practice_method: enum             # "blocked" | "random" | "interleaved" | "variable"
  duration_weeks: number
  daily_minutes: number
  
  procedure:
    - step: number
      instruction: string
      focus_cue: string
  
  success_criteria:
    - criterion: string
      measurement: string
  
  progression_path: string[]         # What to move to after success
  
  evidence_basis:
    - source: string
      finding: string
      confidence: number
```

**Example Drill Mappings:**

```yaml
problem_example: "Fast passages are uneven and tense"

root_cause_diagnosis:
  primary: "excess_tension_compromising_speed"
  secondary: "insufficient_relaxed_base_tempo"
  framework: "motor_pattern_disruption"

corrective_drills:
  - name: "Rhythm Check Slow-Fast"
    category: "isolation"
    practice_method: "variable"
    duration_weeks: 2
    procedure:
      - "Set metronome to half target tempo"
      - "Play passage with perfect rhythm, relaxed"
      - "Increase by 5 BPM only when current is effortless"
      - "Return to half tempo if tension detected"
    success_criteria:
      - "Passage clean at target tempo without tension"
    evidence_basis:
      - source: "Motor learning research - tempo increment studies"
        finding: "Small increments with consolidation produce better retention than large jumps"

  - name: "Pulse-Based Rhythm Grid"
    category: "transfer"
    practice_method: "random"
    procedure:
      - "Practice passage in rhythm grid (dotted, straight, double-dotted)"
      - "Randomize order for transfer enhancement"
      - "Focus on underlying pulse, not surface rhythm"
    success_criteria:
      - "Clean execution in all rhythm grid variations"
    evidence_basis:
      - source: "Contextual interference research"
        finding: "Random practice improves transfer and retention vs blocked"
```

### 4. Progression Planning
Design remediation sequence:

```yaml
remediation_plan:
  immediate_actions:                # Week 1-2
    - drill: string
      focus: "symptom_relief"
      expected_change: string
  
  foundation_reinforcement:         # Week 3-6
    - drill: string
      focus: "root_cause_addressing"
      expected_change: string
  
  integration_transfer:             # Week 7+
    - drill: string
      focus: "real_world_application"
      expected_change: string
  
  monitoring_criteria:
    - checkpoint: string
      timeframe: string
      success_indicators: string[]
      failure_indicators: string[]
```

## Structured Output
```yaml
technique_diagnostic:
  problem_identification:
    reported_issue: string
    category: enum
    specific_symptoms: string[]
    onset_context: string
  
  root_cause_analysis:
    primary_cause:
      type: string
      framework: string
      confidence: number
      evidence: string[]
    secondary_causes:
      - type: string
        framework: string
        confidence: number
        evidence: string[]
  
  diagnostic_confidence: number     # 0-1, based on information quality
  
  corrective_prescription:
    immediate_drills:
      - <drill_structure>
    foundation_drills:
      - <drill_structure>
    integration_drills:
      - <drill_structure>
  
  remediation_timeline:
    total_weeks: number
    phases:
      - phase: string
        duration_weeks: number
        primary_focus: string[]
        expected_outcomes: string[]
  
  monitoring_plan:
    daily_checkpoints:
      - checkpoint: string
        indicator: string
      frequency: string
    
    weekly_assessments:
      - assessment: string
        criteria: string[]
        adjustment_triggers: string[]
  
  risk_assessment:
    injury_risk: enum
    frustration_risk: enum
    plateau_risk: enum
    recommendations: string[]
  
  evidence_basis:
    - claim: string
      source: string
      url: string?
      confidence: number
  
  red_flags:
    - flag: string
      action: string
      urgency: enum                  # "immediate" | "soon" | "monitor"
```

## Quality Gate
- [ ] Problem clearly categorized with specific symptoms documented
- [ ] Root cause analysis cites motor learning or pedagogical frameworks
- [ ] Each drill includes evidence-based practice method selection
- [ ] Success criteria are measurable and specific
- [ ] Progression includes monitoring and adjustment triggers
- [ ] Safety risks flagged and addressed
- [ ] Output is structured, not prose-only
- [ ] Confidence level stated based on information quality

## Error Handling
- If insufficient detail for diagnosis, request specific clarifying questions
- If multiple possible causes, present differential diagnosis with confidence levels
- If safety concern identified, prioritize professional consultation recommendation
- If problem appears medical (persistent pain, significant dysfunction), recommend medical assessment

## Special Cases

### Performance Anxiety:
1. Distinguish anxiety-caused tension from technique issues
2. Recommend both mental and physical interventions
3. Include performance simulation in remediation
4. Address preparation adequacy as root cause

### Long-Standing Plateaus:
1. Assess practice efficiency and quality
2. Check for overlearning of incorrect patterns
3. Consider deliberate practice redesign
4. Evaluate motivation and goal alignment

### Post-Injury Return:
1. Coordinate with medical guidance
2. Design gradual rebuilding progression
3. Prioritize technique foundation over repertoire
4. Include monitoring for recurrence

### Self-Taught Learners:
1. Audit fundamental technique for compensations
2. Address missing foundational elements
3. Provide structure for systematic rebuilding
4. Recommend periodic professional assessment

## Integration Notes
This sub-skill can be invoked independently when learners encounter specific problems, or as part of ongoing curriculum refinement. Diagnostic accuracy improves with more specific input and performance context.
