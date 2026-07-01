# PROJECT-DEVELOPMENT-PHASE-TRACKING.md — Rare Instrument / Vocal Technique Self-learning Path

Idea #194 · `rare-instrument-vocal-learning-path` · Cluster: Career, Learning & Skills

## Phase 0 — Research & Skill Architecture
- **Tasks:** map the domain; select world-renowned frameworks; define scoring dimensions; identify authoritative sources.
- **Deliverables:** framework list, source list, scoring rubric.
- **Success criteria:** every scoring dimension maps to a named, citable framework.
- **Status:** ✅ Complete.

## Phase 1 — Core Sub-Skills
- **Tasks:** implement intake, the gate sub-skill, the scoring engine and the roadmap builder (≥3 sub-skills total).
- **Deliverables:** `skills/sub-*.md` files.
- **Success criteria:** each sub-skill has clear inputs/outputs and a quality gate.
- **Status:** ✅ Complete. 5 production-grade sub-skills authored with comprehensive procedures, schemas, and quality gates: `sub-learner-intake`, `sub-curriculum-builder`, `sub-technique-diagnostic`, `sub-practice-scheduler`, `sub-progress-roadmap`. Each includes detailed input/output schemas, evidence-based frameworks, error handling, and integration notes.

## Phase 2 — Main Harness + Quality Gates
- **Tasks:** wire the stages in `skills/main.md`; encode the validation gate and the devil's-advocate review.
- **Deliverables:** `skills/main.md`.
- **Success criteria:** no output path bypasses the gates.
- **Status:** ✅ Complete. Main harness wired with comprehensive workflow: Intake → Evidence sync → Gate validation → Scoring → Devil's advocate challenge → Synthesis. All quality gates encoded with checklist verification. No output path bypasses validation or review stages. Production-ready with clear persona, tool integration, and structured output format.

## Phase 3 — SECOND-KNOWLEDGE-BRAIN Pipeline
- **Tasks:** author the knowledge brain v1; implement `tools/knowledge_updater.py` (crawl4ai + WebSearch) with de-duplication and date-stamped append.
- **Deliverables:** `SECOND-KNOWLEDGE-BRAIN.md`, `tools/knowledge_updater.py`.
- **Success criteria:** pipeline appends scored, de-duplicated entries; weekly cron documented.
- **Status:** ✅ Complete. Knowledge brain v1 seeded with core frameworks (Deliberate Practice, Motor Learning, ABRSM/Trinity, Vocal Pedagogy, Bloom's Taxonomy). Crawl pipeline implemented with crawl4ai + WebSearch integration, de-duplication via URL hash, relevance scoring, and date-stamped append. Weekly cron schedule documented. Production-ready with graceful degradation when offline.

## Phase 4 — Testing & Validation
- **Tasks:** author ≥5 test scenarios; dry-run the harness against them.
- **Deliverables:** `tests/test-scenarios.md`, `tests/validate.py`.
- **Success criteria:** all scenarios pass their gates; edge cases identified.
- **Status:** ✅ Complete. 15 comprehensive test scenarios authored (5 initial + 10 adversarial/edge cases). Automated validation script (`tests/validate.py`) implemented for dry-run testing against all scenarios with quality gate verification.

## Phase 5 — Integration & Cross-Skill Wiring
- **Tasks:** connect shared cluster sub-skills (intake/scoring/roadmap) for reuse across the `career-education` cluster.
- **Deliverables:** documented shared-sub-skill interfaces.
- **Success criteria:** sibling skills can reuse this skill's intake/scoring patterns.
- **Status:** ✅ Complete. Shared sub-skill interfaces documented in `docs/shared-sub-skill-interfaces.md` with comprehensive schemas, quality gates, and reuse contracts for `career-education` cluster. Four core interfaces defined: Learner Intake, Scoring & Evaluation, Practice/Schedule Design, and Progress Tracking & Roadmap.

## Effort Estimate
| Phase | Effort |
|------|--------|
| 0 Research | 0.5 d |
| 1 Sub-skills | 1.0 d |
| 2 Harness | 0.5 d |
| 3 Knowledge pipeline | 0.5 d |
| 4 Testing | 0.5 d |
| 5 Integration | 0.5 d |
