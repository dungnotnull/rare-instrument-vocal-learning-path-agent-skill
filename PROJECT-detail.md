# PROJECT-detail.md — Rare Instrument / Vocal Technique Self-learning Path

## Executive Summary
`rare-instrument-vocal-learning-path` is a harness skill in the **Career, Learning & Skills** cluster (idea #194). Designs a self-study path for rare instruments or difficult vocal techniques with milestone curricula and error-correction drills. It executes a research-first, framework-grounded workflow that ends in a multi-dimensional score and a prioritized, effort/impact-ranked improvement roadmap.

> **Note:** Recommendations are evidence-based decision-support; validate against your specific context before acting.

## Problem Statement
Self-learners of niche instruments or advanced vocal techniques lack structured curricula and feedback, risking injury and ingrained errors. This skill designs a staged learning path grounded in pedagogy and motor-learning science, with diagnostic checkpoints and corrective drills.

## Target Users & Use Cases
- Practitioners, learners and small teams who need an expert-grade, evidence-based analysis without hiring a specialist.
- Trigger examples:
  - "I want to learn the hurdy-gurdy from scratch" → the skill runs its full harness and returns a scored deliverable.
  - "I want to belt safely" → the skill runs its full harness and returns a scored deliverable.
  - "I've stalled on fast passages" → the skill runs its full harness and returns a scored deliverable.
  - "Only 20 min/day" → the skill runs its full harness and returns a scored deliverable.
  - "Preparing for ABRSM grade 5" → the skill runs its full harness and returns a scored deliverable.

## Harness Architecture
```
User input
   │
   ▼
[Stage 1 Intake]  sub-learner-intake
   │
   ▼
[Stage 2 Research]  SECOND-KNOWLEDGE-BRAIN.md + WebSearch/WebFetch
   │
   ▼
[Stage 3 Gate]  requirement validation
   │
   ▼
[Stage 4 Scoring]  sub-curriculum-builder  → score vs frameworks
   │
   ▼
[Stage 5 Challenge]  devil's-advocate review
   │
   ▼
[Stage 6 Synthesis]  sub-practice-scheduler  → scored report + roadmap
```

## Full Sub-Skill Catalog
### `sub-learner-intake`
- **Purpose:** Capture instrument/voice type, current level, goals, practice time, equipment and any physical limitations.
- **Inputs:** structured fields from prior stages / user.
- **Outputs:** structured record consumed by the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** outputs are complete, evidence-linked, and assumptions are explicit.
### `sub-curriculum-builder`
- **Purpose:** Sequence a graded curriculum (technique, theory, repertoire) against ABRSM/Trinity milestones.
- **Inputs:** structured fields from prior stages / user.
- **Outputs:** structured record consumed by the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** outputs are complete, evidence-linked, and assumptions are explicit.
### `sub-technique-diagnostic`
- **Purpose:** Diagnose errors from user description/recording notes and map to corrective drills (motor-learning informed).
- **Inputs:** structured fields from prior stages / user.
- **Outputs:** structured record consumed by the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** outputs are complete, evidence-linked, and assumptions are explicit.
### `sub-practice-scheduler`
- **Purpose:** Design spaced, interleaved practice blocks with deliberate-practice targets.
- **Inputs:** structured fields from prior stages / user.
- **Outputs:** structured record consumed by the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** outputs are complete, evidence-linked, and assumptions are explicit.
### `sub-progress-roadmap`
- **Purpose:** Define milestone checkpoints and adjust the path based on progress/plateaus.
- **Inputs:** structured fields from prior stages / user.
- **Outputs:** structured record consumed by the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** outputs are complete, evidence-linked, and assumptions are explicit.

## Evaluation Frameworks
1. **Deliberate Practice (Ericsson)** — Evidence-based framework for skill acquisition through focused, feedback-rich, progressively harder practice.
2. **Motor learning theory (blocked vs random/contextual interference)** — Practice-scheduling science that improves retention and transfer of technique.
3. **ABRSM / Trinity graded syllabi** — Internationally recognized graded curricula and assessment criteria for instruments and voice.
4. **Vocal pedagogy (estill / SOVT)** — Evidence-informed voice-technique and vocal-health frameworks (semi-occluded vocal tract exercises).
5. **Bloom's taxonomy / spaced repetition** — Learning-objective sequencing and retention scheduling for theory and repertoire.

## Scoring Dimensions
- Technique foundation
- Theory knowledge
- Repertoire progression
- Practice-schedule quality
- Injury-risk/vocal health
- Goal alignment

Each dimension is scored 0–100 (or 1–5) with an explicit rationale and at least one cited source or stated assumption. The composite score is a transparent weighted aggregate; weights are disclosed.

## Skill File Format Specification
- Frontmatter: `name` (= `rare-instrument-vocal-learning-path`), `description` (one line).
- Required sections: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates.

## E2E Execution Flow
1. Parse request; classify the task and detect missing inputs (ask targeted questions).
2. Run intake sub-skill → structured profile.
3. Sync evidence from the knowledge brain; refresh via WebSearch/WebFetch when available; otherwise signal degraded mode.
4. Run the validation gate — **halt and route out** on red flags.
5. Score against frameworks; record evidence per dimension.
6. Devil's-advocate pass: challenge weakest assumptions, seek disconfirming evidence.
7. Synthesize the deliverable: scored report + prioritized roadmap (effort × impact).
8. Run quality gates; only then present output.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: ArXiv (cs.SD, eess.AS, q-bio.NC) + the authoritative domain sources listed in `CLAUDE.md`.
- Crawl config and append format are defined in `tools/knowledge_updater.py` and `SECOND-KNOWLEDGE-BRAIN.md`.

## Supporting Tools Spec — `knowledge_updater.py`
- **Inputs:** crawl query list (below), source URLs, last-run timestamp.
- **Outputs:** appended, de-duplicated, date-stamped entries in `SECOND-KNOWLEDGE-BRAIN.md`.
- **Schedule:** weekly cron.
- **Crawl queries:** `deliberate practice music skill acquisition 2026`, `contextual interference motor learning music`, `SOVT vocal warmup evidence`, `spaced repetition instrument learning`

## Quality Gates (must all pass before output)
- Every scored dimension cites a source or states an assumption.
- The applicable safety/compliance gate has passed.
- The devil's-advocate review has been performed and its objections addressed.
- The roadmap items are prioritized by effort × impact and are actionable.
- Evidence hierarchy respected (systematic review > meta-analysis > RCT/standard > expert opinion > blog).

## Test Scenarios
1. **Niche instrument start** — *User:* "I want to learn the hurdy-gurdy from scratch" → *Skill:* Builds graded curriculum with milestones and method-book references. (**Gate:** Path matched to weekly practice time.)
2. **Vocal technique** — *User:* "I want to belt safely" → *Skill:* Designs SOVT-based progression with vocal-health guardrails. (**Gate:** Strain red flags route to voice clinician.)
3. **Plateau** — *User:* "I've stalled on fast passages" → *Skill:* Diagnoses likely cause, prescribes interleaved/slow-practice drills. (**Gate:** Drill cited to motor-learning evidence.)
4. **Limited time** — *User:* "Only 20 min/day" → *Skill:* Optimizes deliberate-practice blocks for the constraint. (**Gate:** Schedule respects stated time budget.)
5. **Exam prep** — *User:* "Preparing for ABRSM grade 5" → *Skill:* Aligns curriculum to graded syllabus criteria. (**Gate:** Milestones mapped to official syllabus.)

## Key Design Decisions
1. Research-first: no scored claim without a citation or explicit assumption.
2. Framework-grounded: scoring uses only the named world-renowned frameworks above.
3. Composable sub-skills (≥3) with explicit gates between stages.
4. Self-improving knowledge brain via the crawl pipeline.
5. Graceful degradation when WebSearch/WebFetch are unavailable.
