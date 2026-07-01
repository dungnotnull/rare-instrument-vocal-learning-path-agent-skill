# Changelog

All notable changes to the Rare Instrument / Vocal Technique Self-learning Path skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-01

### Added
- **Phase 0:** Research & Skill Architecture complete
  - Mapped domain and selected world-renowned frameworks
  - Defined scoring dimensions with citable sources
  - Identified authoritative data sources

- **Phase 1:** Core Sub-Skills (5 production-grade sub-skills)
  - `sub-learner-intake` — Structured learner profile capture
  - `sub-curriculum-builder` — Evidence-based curriculum scoring
  - `sub-technique-diagnostic` — Error diagnosis with corrective drills
  - `sub-practice-scheduler` — Motor-learning informed practice design
  - `sub-progress-roadmap` — Milestone tracking and plateau strategies

- **Phase 2:** Main Harness + Quality Gates
  - Wired complete workflow: Intake → Evidence → Gate → Score → Challenge → Output
  - Encoded validation gate and devil's-advocate review
  - No output path bypasses quality gates

- **Phase 3:** SECOND-KNOWLEDGE-BRAIN Pipeline
  - Seeded knowledge brain with core frameworks
  - Implemented crawl4ai + WebSearch pipeline
  - De-duplication via URL hash, relevance scoring, date-stamped append
  - Weekly cron schedule documented

- **Phase 4:** Testing & Validation
  - 15 comprehensive test scenarios (5 initial + 10 adversarial/edge cases)
  - Automated validation script (`tests/validate.py`)
  - Quality gate verification for all scenarios

- **Phase 5:** Integration & Cross-Skill Wiring
  - Documented shared sub-skill interfaces
  - Defined 4 core interfaces for `career-education` cluster reuse
  - Comprehensive schemas, quality gates, and reuse contracts

- **Production Documentation**
  - Comprehensive README.md
  - CONTRIBUTING.md with contribution guidelines
  - MIT LICENSE
  - CHANGELOG.md (this file)

### Frameworks Implemented
- Deliberate Practice (Ericsson)
- Motor Learning Theory (blocked vs random/interleaved)
- ABRSM / Trinity graded syllabi
- Vocal Pedagogy (Estill/SOVT)
- Bloom's Taxonomy / Spaced Repetition

### Quality Standards
- Every material claim cites source or marks assumption
- Devil's-advocate review on all outputs
- Structured output schemas (no prose-only)
- Safety and injury risk assessment
- Evidence hierarchy respected

### Testing
- 15 test scenarios covering:
  - Niche instruments and vocal techniques
  - Plateaus and limited time constraints
  - Conflicting goals and physical limitations
  - Equipment mismatches and age appropriateness
  - Degraded mode and insufficient inputs
  - Multiple conflicting technique goals

---

## [Unreleased]

### Planned
- First scheduled knowledge brain crawl
- Additional domain-specific extensions
- Community-contributed test scenarios

---

## Version Format

- **Major.Minor.Patch** (e.g., 1.0.0)
- **Major:** Breaking changes to interfaces or output schemas
- **Minor:** New features, framework additions, backward-compatible changes
- **Patch:** Documentation fixes, minor clarifications, typo corrections

---

## How to Update This Changelog

When making changes:
1. Add entry under `[Unreleased]` section
2. Use category: Added, Changed, Deprecated, Removed, Fixed, Security
3. Include brief description and rationale
4. When releasing, move to new version section with date

---

**Maintained by:** Rare Instrument / Vocal Technique Self-learning Path Contributors
**Framework Versions:** Current as of 2025-01-01
