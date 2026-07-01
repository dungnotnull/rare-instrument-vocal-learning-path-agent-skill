---
name: rare-instrument-vocal-learning-path__sub-curriculum-builder
description: Sub-skill of rare-instrument-vocal-learning-path — Sequence a graded curriculum (technique, theory, repertoire) against ABRSM/Trinity milestones.
---

## Purpose
Design a graded, evidence-based curriculum that sequences technique, theory, and repertoire development appropriate to the learner's level, goals, and constraints. Map progression to recognized frameworks (ABRSM, Trinity, etc.) while applying motor-learning principles for optimal skill acquisition.

## Input Sources
- `sub-learner-intake` output (learner_profile, validation_flags)
- `SECOND-KNOWLEDGE-BRAIN.md` for framework details and evidence
- Domain-specific syllabi (ABRSM, Trinity, method books)

## Scoring Dimensions
```yaml
evaluation_dimensions:
  technique_foundation:
    description: "Baseline technical competence and mechanics"
    weight: 0.25
    criteria:
      - posture/instrument_holding
      - basic_sound_production
      - fundamental_coordination
      - technique_appropriate_to_level
  
  theory_knowledge:
    description: "Understanding of music/theory fundamentals"
    weight: 0.15
    criteria:
      - notation_reading
      - rhythm_understanding
      - key/tonality_concepts
      - structural_awareness
  
  repertoire_progression:
    description: "Appropriate repertoire sequencing and challenge curve"
    weight: 0.25
    criteria:
      - difficulty_progression
      - genre_diversity
      - technical_appropriateness
      - interest_alignment
  
  practice_schedule_quality:
    description: "Alignment with motor learning and deliberate practice principles"
    weight: 0.15
    criteria:
      - time_allocation_efficiency
      - practice_structure
      - feedback_opportunities
      - rest_interval_inclusion
  
  injury_risk_vocal_health:
    description: "Safety and physical wellbeing considerations"
    weight: 0.10
    criteria:
      - technique_safety
      - overload_prevention
      - warm_up_inclusion
      - rest_days_scheduled
  
  goal_alignment:
    description: "Fit between curriculum and learner objectives"
    weight: 0.10
    criteria:
      - milestone_targeting
      - timeline_feasibility
      - resource_matching
      - motivation_sustenance
```

## Procedure

### 1. Framework Selection
Select appropriate frameworks based on `target_instrument_voice`:

**For Instruments:**
- ABRSM graded music exam syllabi (where available)
- Trinity College London syllabi
- Recognized method books (e.g., Suzuki, Rubank, Arban)
- Conservatory technique sequences

**For Vocal Techniques:**
- Estill Voice Training™ levels
- SOVT progression frameworks
- NATS (National Association of Teachers of Singing) guidelines
- Belt technique safety protocols

**For Rare/Niche Areas:**
- Map to nearest available formal syllabus
- Apply Deliberate Practice stages directly
- Use motor learning research for sequencing

### 2. Level Assessment
Determine appropriate starting level:

```yaml
level_mapping:
  none:
    abrsm_equivalent: "Pre-Grade 1"
    focus: ["basic_sound_production", "posture", "fundamental_technique"]
    theory: ["basic_notation", "rhythm_recognition"]
    repertoire: ["simple_folk", "basic_exercises"]
  
  beginner:
    abrsm_equivalent: "Grade 1-2"
    focus: ["scale_patterns", "basic_coordination", "simple_repertoire"]
    theory: ["key_signatures", "time_signatures", "intervals"]
    repertoire: ["grade_appropriate_pieces", "etudes"]
  
  intermediate:
    abrsm_equivalent: "Grade 3-5"
    focus: ["articulation", "dynamics", "technique_consolidation"]
    theory: ["harmony", "form_analysis", "advanced_rhythm"]
    repertoire: ["stylistic_variety", "period_pieces", "technical_studies"]
  
  advanced:
    abrsm_equivalent: "Grade 6-8+"
    focus: ["interpretation", "advanced_technique", "performance_refinement"]
    theory: ["advanced_harmony", "analysis", "historical_context"]
    repertoire: ["major_repertoire", "virtuosic_pieces", "performance_prep"]
```

### 3. Curriculum Sequencing
Design progressive stages:

**Stage 1: Foundation (Weeks 1-8 or equivalent)**
- Technique basics and mechanics
- Sound production fundamentals
- Basic theory and notation
- Simple repertoire for application

**Stage 2: Development (Weeks 9-20 or equivalent)**
- Technique expansion and consolidation
- Intermediate theory concepts
- Grade-appropriate repertoire
- Introduction to style and interpretation

**Stage 3: Advancement (Weeks 21-40 or equivalent)**
- Advanced technique refinement
- Comprehensive theory integration
- Diverse and challenging repertoire
- Performance preparation

**Stage 4: Refinement (as needed for goals)**
- Specialized technique mastery
- Advanced theoretical understanding
- Professional-level repertoire
- Performance excellence

### 4. Evidence-Based Scoring
For each dimension, score 0-100 with evidence linkage:

```yaml
scoring_methodology:
  score_calculation:
    - Assess current level against framework milestones
    - Identify gaps in each dimension
    - Rate curriculum quality against evidence-based criteria
    - Apply dimension weights for composite score
  
  evidence_sources:
    - ABRSM/Trinity syllabus requirements
    - Motor learning research (blocked vs random practice)
    - Deliberate Practice principles (Ericsson)
    - Vocal pedagogy research (Estill, SOVT)
    - Instrument method book progressions
  
  assumption_marking:
    - When formal syllabus unavailable, state assumption
    - When mapping rare instrument to nearest framework, document reasoning
    - When timeline exceeds research norms, flag as assumption
```

### 5. Devil's Advocate Review
Challenge the proposed curriculum:

**Review Questions:**
1. Is this timeline realistic given deliberate practice research?
2. Are the prerequisites truly met for each stage?
3. Could this progression cause injury or overwhelm?
4. Is there a more efficient sequencing based on transfer of learning?
5. Are we overestimating practice efficiency or learner consistency?

**Review Process:**
- List potential objections to curriculum design
- Provide evidence-based responses to each
- Adjust curriculum if objections are valid
- Document all objections and resolutions

### 6. Structured Output Generation
Emit comprehensive curriculum evaluation:

```yaml
curriculum_evaluation:
  dimension_scores:
    - dimension: string
      score: number                    # 0-100
      confidence: number               # 0-1
      evidence:
        - source: string
          claim: string
          url: string?
          is_assumption: boolean
      gaps: string[]
      strengths: string[]
      recommendations: string[]
  
  composite_score: number
  overall_confidence: number
  
  proposed_curriculum:
    stages:
      - stage: number
        name: string
        duration_weeks: number
        technique_focus: string[]
        theory_topics: string[]
        repertoire_suggestions:
          - piece: string
            difficulty: enum
            purpose: string
        practice_allocation:
          technique: number            # percentage
          theory: number
          repertoire: number
        milestones:
          - milestone: string
            criteria: string[]
  
  risk_assessment:
    injury_risk: enum
    feasibility_risk: enum
    overwhelm_risk: enum
    mitigation_strategies: string[]
  
  framework_alignment:
    - framework: string
      alignment_score: number
      missing_elements: string[]
      additional_elements: string[]
  
  devil_advocate_review:
    objections:
      - objection: string
        response: string
        adjustment_made: string
    final_adjustments: string[]
  
  recommendations:
    prioritized:
      - recommendation: string
        impact: enum                  # "high" | "medium" | "low"
        effort: enum                   # "high" | "medium" | "low"
        rationale: string
```

## Quality Gate
Before passing to next stage:
- [ ] Every dimension score cites evidence OR marks assumption
- [ ] Devil's-advocate review performed and documented
- [ ] Curriculum stages are time-bound and measurable
- [ ] Risk factors assessed and mitigation provided
- [ ] Output is structured, not prose-only
- [ ] Framework alignment documented
- [ ] Timeline validated against deliberate practice norms

## Special Cases

### Rare Instruments Without Formal Syllabi:
1. Map to nearest instrument family syllabus
2. Apply motor learning stages directly
3. Use method book progressions as proxy
4. Explicitly document mapping assumptions

### Vocal Techniques with Safety Concerns:
1. Prioritize vocal health in scoring
2. Include warm-up and cool-down requirements
3. Set progression caution thresholds
4. Recommend professional monitoring for advanced techniques

### Limited Practice Time:
1. Prioritize deliberate practice over extensive repertoire
2. Use interleaved practice for efficiency
3. Focus on high-impact technique elements
4. Adjust timeline expectations realistically

## Error Handling
- If insufficient information for curriculum design, request clarification
- If goal is demonstrably unrealistic with constraints, provide alternatives
- If safety risk identified, prioritize risk mitigation in recommendations
- If framework unavailable, document and use nearest proxy with explicit assumption

## Integration Notes
This sub-skill receives validated intake and produces the core curriculum design that informs practice scheduling and progress tracking. Its output must be specific enough to guide subsequent stages while flexible enough to adapt to individual progress.
