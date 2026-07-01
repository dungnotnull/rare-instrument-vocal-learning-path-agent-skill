# tests/test-scenarios.md — Rare Instrument / Vocal Technique Self-learning Path

Scenario-based tests for `rare-instrument-vocal-learning-path` (idea #194). Minimum 5; 7 provided (incl. degraded-mode and insufficient-input edge cases).

### Scenario 1: Niche instrument start
- **User input:** "I want to learn the hurdy-gurdy from scratch"
- **Expected harness behavior:** Builds graded curriculum with milestones and method-book references.
- **Frameworks exercised:** Deliberate Practice (Ericsson), Motor learning theory (blocked vs random/contextual interference), ABRSM / Trinity graded syllabi
- **Quality gate under test:** Path matched to weekly practice time.
- **Pass criteria:** scored output produced, gate enforced, every dimension evidence-linked or assumption-marked, prioritized roadmap included.
### Scenario 2: Vocal technique
- **User input:** "I want to belt safely"
- **Expected harness behavior:** Designs SOVT-based progression with vocal-health guardrails.
- **Frameworks exercised:** Deliberate Practice (Ericsson), Motor learning theory (blocked vs random/contextual interference), ABRSM / Trinity graded syllabi
- **Quality gate under test:** Strain red flags route to voice clinician.
- **Pass criteria:** scored output produced, gate enforced, every dimension evidence-linked or assumption-marked, prioritized roadmap included.
### Scenario 3: Plateau
- **User input:** "I've stalled on fast passages"
- **Expected harness behavior:** Diagnoses likely cause, prescribes interleaved/slow-practice drills.
- **Frameworks exercised:** Deliberate Practice (Ericsson), Motor learning theory (blocked vs random/contextual interference), ABRSM / Trinity graded syllabi
- **Quality gate under test:** Drill cited to motor-learning evidence.
- **Pass criteria:** scored output produced, gate enforced, every dimension evidence-linked or assumption-marked, prioritized roadmap included.
### Scenario 4: Limited time
- **User input:** "Only 20 min/day"
- **Expected harness behavior:** Optimizes deliberate-practice blocks for the constraint.
- **Frameworks exercised:** Deliberate Practice (Ericsson), Motor learning theory (blocked vs random/contextual interference), ABRSM / Trinity graded syllabi
- **Quality gate under test:** Schedule respects stated time budget.
- **Pass criteria:** scored output produced, gate enforced, every dimension evidence-linked or assumption-marked, prioritized roadmap included.
### Scenario 5: Exam prep
- **User input:** "Preparing for ABRSM grade 5"
- **Expected harness behavior:** Aligns curriculum to graded syllabus criteria.
- **Frameworks exercised:** Deliberate Practice (Ericsson), Motor learning theory (blocked vs random/contextual interference), ABRSM / Trinity graded syllabi
- **Quality gate under test:** Milestones mapped to official syllabus.
- **Pass criteria:** scored output produced, gate enforced, every dimension evidence-linked or assumption-marked, prioritized roadmap included.
### Scenario 6: Degraded mode (offline)
- **User input:** any of the above with WebSearch/WebFetch unavailable.
- **Expected behavior:** skill falls back to `SECOND-KNOWLEDGE-BRAIN.md`, explicitly signals degraded mode, and still enforces all gates.
- **Pass criteria:** no fabricated live data; degradation disclosed.

### Scenario 7: Insufficient input
- **User input:** a vague one-line request missing key fields.
- **Expected behavior:** intake sub-skill asks targeted clarifying questions instead of assuming.
- **Pass criteria:** no scored output until required inputs are gathered.

### Scenario 8: Conflicting goals (adversarial)
- **User input:** "I want to master classical violin technique in 2 weeks while practicing 10 minutes per day"
- **Expected behavior:** harness identifies timeline vs deliberate practice constraints as incompatible; proposes realistic alternatives.
- **Frameworks exercised:** Deliberate Practice (Ericsson), Motor learning theory, Bloom's taxonomy
- **Quality gate under test:** Goal alignment scoring detects impossibility; roadmap rejects infeasible targets.
- **Pass criteria:** scored output produced, gate enforced, every dimension evidence-linked or assumption-marked, infeasibility explicitly called out.

### Scenario 9: Physical limitation with injury risk (adversarial)
- **User input:** "I have a history of vocal cord nodules and want to learn belt voice technique"
- **Expected behavior:** harness flags high injury risk; recommends medical consultation before proceeding; offers safer alternative pathways.
- **Frameworks exercised:** Vocal pedagogy (estill / SOVT), Deliberate Practice
- **Quality gate under test:** Injury-risk/vocal health dimension overrides other goals; medical referral triggered.
- **Pass criteria:** scored output produced, safety gate enforced, medical recommendation explicit, every dimension evidence-linked.

### Scenario 10: Equipment/instrument mismatch (adversarial)
- **User input:** "I want to learn professional French horn but I only have a student trumpet"
- **Expected behavior:** harness identifies instrument mismatch; outlines equipment requirements; suggests staging path or alternative instrument.
- **Frameworks exercised:** ABRSM graded syllabi, Deliberate Practice
- **Quality gate under test:** Equipment validation prevents unbuildable curriculum; realistic staging proposed.
- **Pass criteria:** scored output produced, equipment gap documented, staging alternatives provided.

### Scenario 11: Age/development appropriateness (adversarial)
- **User input:** "I'm 6 years old and want to learn operatic tenor repertoire"
- **Expected behavior:** harness identifies developmentally inappropriate goals for age; proposes age-appropriate staging; protects vocal health.
- **Frameworks exercised:** Vocal pedagogy (SOVT), ABRSM graded syllabi, Bloom's taxonomy
- **Quality gate under test:** Developmental appropriateness checked against age/physiology; harm prevention prioritized.
- **Pass criteria:** scored output produced, developmental constraints documented, age-appropriate path offered.

### Scenario 12: Over-advanced starting claim (adversarial)
- **User input:** "I'm a complete beginner but want to start with Paganini Caprices"
- **Expected behavior:** harness validates claimed current level against chosen repertoire; proposes appropriate staging if mismatch detected.
- **Frameworks exercised:** ABRSM graded syllabi, Bloom's taxonomy, Deliberate Practice
- **Quality gate under test:** Current level validation prevents frustration/injury from unrealistic repertoire.
- **Pass criteria:** scored output produced, level-repertoire mismatch diagnosed, appropriate staging provided.

### Scenario 13: Multiple conflicting technique goals (adversarial)
- **User input:** "I want to learn both heavy metal growling and classical coloratura simultaneously"
- **Expected behavior:** harness identifies potentially conflicting technical demands; proposes sequential or integrated approach with clear tradeoffs.
- **Frameworks exercised:** Motor learning theory (contextual interference), Vocal pedagogy, Deliberate Practice
- **Quality gate under test:** Motor learning theory applied to conflicting technique acquisition; interference flagged.
- **Pass criteria:** scored output produced, technical conflicts analyzed, integration strategy proposed.

### Scenario 14: No internet but stale knowledge brain (adversarial)
- **User input:** any scenario with WebSearch unavailable and SECOND-KNOWLEDGE-BRAIN.md timestamp >6 months old.
- **Expected behavior:** harness explicitly signals knowledge currency risk; provides best-available recommendations with timestamp disclaimer; suggests refresh when online.
- **Quality gate under test:** Knowledge freshness explicitly disclosed; recommendations marked with currency confidence.
- **Pass criteria:** knowledge age warning prominent, recommendations marked with confidence, refresh suggestion included.

### Scenario 15: Unusual/rare instrument with limited formal syllabus (edge case)
- **User input:** "I want to learn the theremin from scratch"
- **Expected behavior:** harness adapts graded curriculum framework to rare instrument with limited formal syllabus; applies motor learning and deliberate practice principles; maps to nearest available formal standards.
- **Frameworks exercised:** All frameworks (adaptive application), Deliberate Practice, Motor learning theory
- **Quality gate under test:** Graceful adaptation when formal syllabi limited; framework principles still applied.
- **Pass criteria:** scored output produced, framework adaptation documented, nearest standards mapped.


## Regression Checklist
- [ ] All gates enforced on every path (validation).
- [ ] Scores trace to citations or explicit assumptions.
- [ ] Devil's-advocate review present.
- [ ] Roadmap prioritized by impact × effort.
- [ ] Disclaimer present where applicable.
