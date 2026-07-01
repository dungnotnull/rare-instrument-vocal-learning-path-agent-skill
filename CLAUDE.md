# CLAUDE.md — Rare Instrument / Vocal Technique Self-learning Path

**Skill name:** `rare-instrument-vocal-learning-path`
**Source idea:** #194 (ideas.md)
**Cluster:** Career, Learning & Skills (`career-education`)
**Tagline:** Designs a self-study path for rare instruments or difficult vocal techniques with milestone curricula and error-correction drills.
**Current phase:** Phase 4 — Testing & Validation (initial build complete)

## Problem This Skill Solves
Self-learners of niche instruments or advanced vocal techniques lack structured curricula and feedback, risking injury and ingrained errors. This skill designs a staged learning path grounded in pedagogy and motor-learning science, with diagnostic checkpoints and corrective drills.

## Harness Flow Summary
1. **Intake** → `sub-learner-intake` gathers structured inputs.
2. **Research / evidence sync** → consult `SECOND-KNOWLEDGE-BRAIN.md`; refresh via WebSearch/WebFetch when available.
3. **Gate** → requirement validation runs before analysis.
4. **Analysis / scoring** → `sub-curriculum-builder` scores against the named frameworks.
5. **Challenge** → devil's-advocate review stress-tests assumptions and evidence.
6. **Synthesize** → `sub-practice-scheduler` produces the scored deliverable + prioritized roadmap.

**Quality gate:** the devil's-advocate review (`sub` quality step) MUST pass before output; every scored claim must trace to a cited source or stated assumption.

## Sub-skills
- `skills/sub-learner-intake.md` — Capture instrument/voice type, current level, goals, practice time, equipment and any physical limitations.
- `skills/sub-curriculum-builder.md` — Sequence a graded curriculum (technique, theory, repertoire) against ABRSM/Trinity milestones.
- `skills/sub-technique-diagnostic.md` — Diagnose errors from user description/recording notes and map to corrective drills (motor-learning informed).
- `skills/sub-practice-scheduler.md` — Design spaced, interleaved practice blocks with deliberate-practice targets.
- `skills/sub-progress-roadmap.md` — Define milestone checkpoints and adjust the path based on progress/plateaus.

## Evaluation Frameworks (world-renowned, citable)
- **Deliberate Practice (Ericsson)** — Evidence-based framework for skill acquisition through focused, feedback-rich, progressively harder practice.
- **Motor learning theory (blocked vs random/contextual interference)** — Practice-scheduling science that improves retention and transfer of technique.
- **ABRSM / Trinity graded syllabi** — Internationally recognized graded curricula and assessment criteria for instruments and voice.
- **Vocal pedagogy (estill / SOVT)** — Evidence-informed voice-technique and vocal-health frameworks (semi-occluded vocal tract exercises).
- **Bloom's taxonomy / spaced repetition** — Learning-objective sequencing and retention scheduling for theory and repertoire.

## Tools Required
- `WebSearch`, `WebFetch` — live evidence and trend updates (graceful degradation to the knowledge brain when unavailable).
- `Read`, `Write` — load the knowledge brain; emit the deliverable.
- `Bash` — run `tools/knowledge_updater.py` (crawl4ai pipeline).

## Knowledge Sources
- **ArXiv / academic categories:** cs.SD, eess.AS, q-bio.NC
- [ABRSM syllabus](https://www.abrsm.org/) — Graded instrument and voice curricula.
- [Journal of Voice](https://www.jvoice.org/) — Peer-reviewed vocal pedagogy and health research.
- [Music education research (Psychology of Music)](https://journals.sagepub.com/home/pom) — Motor learning and practice research.
- [IMSLP](https://imslp.org/) — Public-domain repertoire and method books.
- [NATS (vocal pedagogy)](https://www.nats.org/) — Vocal-health and teaching standards.

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai + WebSearch pipeline that grows `SECOND-KNOWLEDGE-BRAIN.md` (recommended weekly cron).

## Active Development Tasks
- [x] Scaffold all required deliverables
- [x] Define frameworks, sub-skills and scoring dimensions
- [x] Author knowledge brain v1 and crawl pipeline
- [ ] Expand knowledge brain via first scheduled crawl
- [ ] Add adversarial/edge-case test scenarios beyond the initial 5

## Related Root Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — living domain knowledge base
