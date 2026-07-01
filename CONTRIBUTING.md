# Contributing to Rare Instrument / Vocal Technique Self-learning Path

Thank you for your interest in contributing! This document outlines how to contribute effectively.

---

## How to Contribute

### Areas Where We Welcome Contributions

1. **Test Scenarios**
   - Add edge cases for rare instruments or vocal techniques
   - Improve existing scenario coverage
   - Add regression tests for discovered issues

2. **Knowledge Base**
   - Add recent research papers to `SECOND-KNOWLEDGE-BRAIN.md`
   - Improve framework descriptions with new evidence
   - Suggest additional authoritative sources

3. **Sub-Skills**
   - Add domain-specific extensions to existing sub-skills
   - Improve error handling for new edge cases
   - Enhance integration notes

4. **Documentation**
   - Improve clarity of skill descriptions
   - Add usage examples
   - Fix documentation errors

---

## Contribution Process

### For Small Changes (Documentation, Typos)

1. Fork the repository
2. Create a branch: `git checkout -b fix/description-of-change`
3. Make your changes
4. Commit with clear message: `git commit -m "Fix: brief description"`
5. Push to your fork: `git push origin fix/description-of-change`
6. Open a Pull Request

### For Significant Changes (New Features, Sub-skills)

1. Open an Issue first to discuss the proposed change
2. Reference relevant research and frameworks
3. Wait for approval before implementing
4. Follow the implementation plan from the issue discussion
5. Ensure all quality gates pass
6. Update documentation and tests
7. Submit PR with clear description of changes

---

## Code & Content Standards

### General Principles

- **Evidence-based:** All claims must cite sources or explicitly mark assumptions
- **Clear structure:** Use YAML schemas for structured data
- **Quality gates:** Every sub-skill must include quality gate checklist
- **No prose-only outputs:** Skills must emit structured data
- **English only:** All code, comments, and documentation in English
- **Professional tone:** No emojis, casual language, or slang

### Sub-Skill Structure

Every sub-skill MUST include:
- Purpose (clear, concise)
- Input schema (YAML format)
- Procedure (detailed steps)
- Output schema (YAML format)
- Quality gate checklist
- Error handling section
- Integration notes

### Documentation Style

- Use present tense for procedures
- Be specific and actionable
- Include examples where helpful
- Cite frameworks and research
- Link to related sections

---

## Testing

Before submitting changes:

```bash
# Run validation script
python tests/validate.py
```

Ensure:
- All checks pass
- No new warnings introduced
- Test scenarios still cover edge cases
- Documentation is consistent with code

---

## Evidence Requirements

### When Adding Claims

**Required for all material claims:**
- Source citation (paper URL, book, framework)
- Confidence level (high/medium/low)
- Year (for research currency)
- Relevance to domain

**Acceptable sources (in priority order):**
1. Systematic reviews and meta-analyses
2. Peer-reviewed journal articles
3. University/conservatory syllabi
4. Recognized method books and frameworks
5. Expert consensus (NATS, ABRSM, etc.)

**Mark assumptions explicitly:**
- When no direct evidence exists
- When extrapolating from related domains
- When making pedagogical judgments

---

## Pull Request Guidelines

### PR Title Format

```
Type: Brief description

Examples:
- Add: hurdy-gurdy specific technique drills
- Fix: validation logic for age appropriateness
- Update: motor learning research references
- Improve: clarity in sub-curriculum-builder
```

### PR Description

Include:
- **Why:** Motivation for the change
- **What:** Summary of changes made
- **Evidence:** Frameworks or research backing changes
- **Testing:** How you validated the changes
- **Documentation:** What docs were updated

### Review Process

- All PRs require at least one approval
- Maintainers may request changes
- Address all review comments before merging
- Squash commits if requested

---

## Code of Conduct

Be respectful, constructive, and evidence-based. Focus on what's best for the community. Disagreements are fine; personal attacks are not.

---

## Questions?

- Open an issue with your question
- Tag with `question` label
- Maintainers will respond as time allows

---

**Thank you for contributing to safer, more effective self-learning paths!**
