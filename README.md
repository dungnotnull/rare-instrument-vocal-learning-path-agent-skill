# Rare Instrument / Vocal Technique Self-learning Path

> **Skill name:** `rare-instrument-vocal-learning-path`
> **Idea #194** · Cluster: Career, Learning & Skills
> **Status:** Production-Ready · Open Source

A self-learning path design skill for rare instruments or difficult vocal techniques. Uses evidence-based frameworks (Deliberate Practice, Motor Learning, ABRSM/Trinity) to build graded curricula with milestone checkpoints, error-correction drills, and practice scheduling—all with safety guardrails and scientific backing.

---

## Problem This Skill Solves

Self-learners of niche instruments (hurdy-gurdy, theremin) or advanced vocal techniques (belt, coloratura) lack structured curricula and face:
- **No clear progression path** — what to practice, in what order
- **Injury risk** — poor technique leads to strain, nodules, or worse
- **Wasted practice time** — ineffective methods, poor scheduling
- **Plateau frustration** — no roadmap for breakthrough
- **Teacher scarcity** — rare instruments have few qualified instructors

This skill designs a staged learning path grounded in pedagogy and motor-learning science, with diagnostic checkpoints and corrective drills—protecting your health while maximizing progress.

---

## How It Works

```
User Input → Intake → Evidence Sync → Gate Validation → Scoring → Devil's Advocate Review → Output
```

1. **Intake** — Captures instrument/voice type, level, goals, time, equipment, limitations
2. **Evidence Sync** — Loads knowledge brain; refreshes via WebSearch when available
3. **Gate Validation** — Confirms sufficient inputs; asks targeted questions if not
4. **Scoring** — Evaluates against named frameworks (Deliberate Practice, Motor Learning, ABRSM)
5. **Devil's Advocate** — Challenges own scores; seeks disconfirming evidence
6. **Output** — Prioritized roadmap with timeline, practice schedule, and milestone checkpoints

**Quality Guarantee:** Every material claim cites a source or explicitly marks an assumption. No fabricated facts.

---

## Evaluation Frameworks

All scoring and curriculum design draws from world-renowned, citable frameworks:

| Framework | Application |
|-----------|-------------|
| **Deliberate Practice (Ericsson)** | Focused, goal-oriented practice with immediate feedback |
| **Motor Learning Theory** | Blocked vs random/interleaved practice for retention |
| **ABRSM / Trinity** | Graded syllabi and assessment criteria |
| **Vocal Pedagogy (Estill/SOVT)** | Evidence-informed voice technique and health |
| **Bloom's Taxonomy** | Learning objective sequencing and progression |

---

## What You Get

### 1. Comprehensive Learner Intake
Structured profile covering:
- Target domain (instrument/technique) and current level
- Goals, timeline, and practice constraints
- Equipment, budget, and physical limitations
- Learning preferences and context

### 2. Scored Curriculum Evaluation
Six dimensions with evidence-linked scoring:
- Technique foundation
- Theory knowledge
- Repertoire progression
- Practice schedule quality
- Injury risk / vocal health
- Goal alignment

### 3. Progressive Roadmap
Staged curriculum with:
- Clear milestones with measurable success criteria
- Practice scheduling optimized for your time
- Error diagnostic system with corrective drills
- Progress monitoring and plateau strategies

### 4. Safety & Risk Management
- Injury risk assessment and mitigation
- Age-appropriateness validation
- Equipment sufficiency checks
- Medical referral triggers when appropriate

---

## Use Cases

- "I want to learn the hurdy-gurdy from scratch" → Graded curriculum with method-book references
- "I want to belt safely" → SOVT-based progression with vocal-health guardrails
- "I've stalled on fast passages" → Diagnosis with interleaved practice drills
- "Only 20 min/day" → Optimized deliberate-practice blocks for constraints
- "Preparing for ABRSM Grade 5" → Aligned to official syllabus criteria

---

## Installation

### As a Skill

```bash
# Clone the repository
git clone https://github.com/your-org/rare-instrument-vocal-learning-path.git

# The skill lives in skills/main.md
# Load it into your AI assistant harness
```

### Dependencies

The skill requires these tools (graceful degradation when offline):
- `WebSearch`, `WebFetch` — live evidence and trend updates
- `Read`, `Write` — knowledge brain and deliverable I/O
- `Bash` — knowledge updater pipeline execution

Optional (for knowledge updates):
- `crawl4ai` — ArXiv and domain source crawling
- Python 3.8+ — knowledge_updater.py execution

---

## Project Structure

```
rare-instrument-vocal-learning-path/
├── CLAUDE.md                          # Project instructions
├── PROJECT-detail.md                  # Full technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Phase completion tracking
├── SECOND-KNOWLEDGE-BRAIN.md          # Living domain knowledge base
├── README.md                          # This file
├── skills/
│   ├── main.md                        # Main harness entry point
│   ├── sub-learner-intake.md          # Intake sub-skill
│   ├── sub-curriculum-builder.md      # Curriculum scoring
│   ├── sub-technique-diagnostic.md    # Error diagnosis & drills
│   ├── sub-practice-scheduler.md      # Practice scheduling
│   └── sub-progress-roadmap.md        # Milestone tracking
├── tools/
│   └── knowledge_updater.py           # crawl4ai pipeline
├── tests/
│   ├── test-scenarios.md              # 15 test scenarios
│   └── validate.py                    # Validation script
└── docs/
    └── shared-sub-skill-interfaces.md # Cluster integration docs
```

---

## Testing

Run the validation script:

```bash
python tests/validate.py
```

This validates:
- All skill files exist with required sections
- Quality gates are properly defined
- Sub-skills have production-grade detail
- Test scenarios cover all required cases
- Integration documentation is complete
- Phase tracking is up to date

---

## Knowledge Base

`SECOND-KNOWLEDGE-BRAIN.md` contains:
- Core frameworks and their applications
- Key research papers (populated by scheduled crawls)
- Authoritative data sources (ABRSM, Journal of Voice, etc.)
- Self-update protocol with weekly cron schedule

**Knowledge updates:** Run `tools/knowledge_updater.py` weekly to:
- Crawl ArXiv (cs.SD, eess.AS, q-bio.NC) for new research
- Fetch updates from domain sources
- Score relevance and de-duplicate via URL hash
- Append date-stamped entries to knowledge brain

Graceful degradation: Works offline from existing knowledge if network unavailable.

---

## Cross-Skill Reuse

This skill defines four shared interfaces for the `career-education` cluster:

1. **Learner Intake** — Structured profile capture schema
2. **Scoring & Evaluation** — Evidence-linked scoring dimensions
3. **Practice/Schedule Design** — Evidence-based scheduling principles
4. **Progress Tracking & Roadmap** — Milestone definition and plateau strategies

Sibling skills can reuse these interfaces without modification. See `docs/shared-sub-skill-interfaces.md` for complete schemas and reuse contracts.

---

## Quality Assurance

Every output passes these quality gates:

- [ ] Intake complete; missing inputs were requested, not assumed
- [ ] Inputs validated against constraints
- [ ] Every dimension cites a source or states an assumption
- [ ] Devil's-advocate review performed and objections addressed
- [ ] Roadmap is prioritized and actionable
- [ ] Evidence hierarchy respected (systematic review > expert opinion)

**No exceptions.**

---

## Development Status

**Phase:** Production-Ready (All phases 0-5 complete)

| Phase | Status | Deliverables |
|-------|--------|--------------|
| 0 Research | ✅ Complete | Frameworks, sources, scoring rubric |
| 1 Sub-skills | ✅ Complete | 5 production-grade sub-skills |
| 2 Harness | ✅ Complete | Main skill with workflow and gates |
| 3 Knowledge Pipeline | ✅ Complete | Knowledge brain + crawl script |
| 4 Testing | ✅ Complete | 15 test scenarios + validation |
| 5 Integration | ✅ Complete | Shared interfaces documented |

---

## Disclaimer

> Recommendations are evidence-based decision-support; validate against your specific context before acting. For vocal techniques, consult a qualified voice teacher or medical professional if you experience pain, strain, or voice changes.

---

## Contributing

We welcome contributions that:
- Add test scenarios for edge cases
- Improve knowledge brain with recent research
- Enhance sub-skills with domain-specific extensions
- Validate against new syllabi or frameworks

Please open issues and PRs with clear descriptions of changes and their evidence basis.

---

## License

[Specify your open source license here]

---

## Acknowledgments

Built on research from:
- K. Anders Ericsson (Deliberate Practice)
- Motor learning research community
- ABRSM and Trinity College London
- Estill Voice Training and NATS
- The broader music education research community

---

**Version:** 1.0 · **Last Updated:** 2025-01-01
