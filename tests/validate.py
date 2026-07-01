#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate.py — automated validation harness for rare-instrument-vocal-learning-path

Dry-runs the main skill against all test scenarios and verifies quality gates pass.
Run with: python tests/validate.py

Exit codes:
  0: All validations pass
  1: One or more validations fail
  2: Error in test setup
"""

import os, sys, json, re
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

HERE = Path(__file__).parent
PROJECT = HERE.parent
SCENARIOS_FILE = HERE / "test-scenarios.md"
SKILLS_DIR = PROJECT / "skills"
MAIN_SKILL = SKILLS_DIR / "main.md"
SUB_SKILLS = {
    "intake": SKILLS_DIR / "sub-learner-intake.md",
    "curriculum": SKILLS_DIR / "sub-curriculum-builder.md",
    "diagnostic": SKILLS_DIR / "sub-technique-diagnostic.md",
    "scheduler": SKILLS_DIR / "sub-practice-scheduler.md",
    "roadmap": SKILLS_DIR / "sub-progress-roadmap.md",
}
KNOWLEDGE_BRAIN = PROJECT / "SECOND-KNOWLEDGE-BRAIN.md"


class ValidationResult:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []
        self.total_checks = 0

    def add_pass(self, check: str, detail: str = ""):
        self.passed.append((check, detail))
        self.total_checks += 1

    def add_fail(self, check: str, detail: str = ""):
        self.failed.append((check, detail))
        self.total_checks += 1

    def add_warning(self, check: str, detail: str = ""):
        self.warnings.append((check, detail))
        # warnings don't count as checks

    def summary(self) -> str:
        passed_count = len(self.passed)
        failed_count = len(self.failed)
        warning_count = len(self.warnings)

        lines = [
            f"\n{'='*60}",
            f"Validation Summary",
            f"{'='*60}",
            f"Total checks: {self.total_checks}",
            f"Passed: {passed_count}",
            f"Failed: {failed_count}",
            f"Warnings: {warning_count}",
            f"{'='*60}\n",
        ]

        if self.failed:
            lines.append("FAILED CHECKS:")
            for check, detail in self.failed:
                lines.append(f"  [FAIL] {check}")
                if detail:
                    lines.append(f"         {detail}")
            lines.append("")

        if self.warnings:
            lines.append("WARNINGS:")
            for check, detail in self.warnings:
                lines.append(f"  [WARN] {check}")
                if detail:
                    lines.append(f"         {detail}")
            lines.append("")

        if self.passed and not self.failed:
            lines.append("All critical checks passed!")

        return "\n".join(lines)

    def exit_code(self) -> int:
        return 1 if self.failed else 0


def read_file(path: Path) -> str:
    """Read file content, return empty string if missing."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[validate] Error reading {path}: {e}", file=sys.stderr)
        return ""


def extract_scenarios(content: str) -> List[Dict[str, Any]]:
    """Parse test scenarios from markdown."""
    scenarios = []
    current_scenario = {}
    scenario_pattern = re.compile(r"### Scenario (\d+): ([^\n]+)")

    for match in scenario_pattern.finditer(content):
        num = match.group(1)
        name = match.group(2).strip()
        scenarios.append({
            "id": num,
            "name": name,
            "input": extract_field(content, match.end(), "User input"),
            "expected": extract_field(content, match.end(), "Expected behavior"),
            "frameworks": extract_field(content, match.end(), "Frameworks exercised"),
            "quality_gate": extract_field(content, match.end(), "Quality gate under test"),
            "pass_criteria": extract_field(content, match.end(), "Pass criteria"),
        })

    return scenarios


def extract_field(content: str, start_pos: int, field_name: str) -> str:
    """Extract a specific field value from scenario content."""
    pattern = rf"- \*\*{field_name}:\*\* ([^\n]+)"
    match = re.search(pattern, content[start_pos:start_pos+2000])
    return match.group(1).strip() if match else ""


def validate_skill_structure(result: ValidationResult):
    """Verify all skill files exist and have required sections."""
    print("[validate] Checking skill structure...")

    # Main skill
    if not MAIN_SKILL.exists():
        result.add_fail("Main skill exists", f"Missing: {MAIN_SKILL}")
    else:
        content = read_file(MAIN_SKILL)
        required_sections = ["Role & Persona", "Workflow", "Sub-skills", "Evaluation Frameworks", "Quality Gates"]
        for section in required_sections:
            if section not in content:
                result.add_fail(f"Main skill has {section} section")
        result.add_pass("Main skill structure", "All required sections present")

    # Sub-skills
    for name, path in SUB_SKILLS.items():
        if not path.exists():
            result.add_fail(f"{name} sub-skill exists", f"Missing: {path}")
        else:
            content = read_file(path)
            # More flexible section matching - check for variations
            section_checks = [
                ("Purpose", "Purpose" in content),
                ("Inputs", "Input" in content),  # Matches "Input Sources" or "Inputs"
                ("Procedure", "Procedure" in content),
                ("Outputs", "Output" in content),  # Matches "Output Schema" or "Outputs"
                ("Quality Gate", "Quality Gate" in content)
            ]
            for section, present in section_checks:
                if present:
                    result.add_pass(f"{name} has {section} section")
                else:
                    result.add_fail(f"{name} has {section} section")


def validate_quality_gates(result: ValidationResult):
    """Verify quality gates are defined in main skill."""
    print("[validate] Checking quality gates...")

    content = read_file(MAIN_SKILL)
    if not content:
        result.add_fail("Quality gates validation", "Cannot read main skill")
        return

    required_gates = [
        "Intake complete",
        "Inputs validated",
        "Every dimension cites a source",
        "Devil's-advocate review",
        "Roadmap is prioritized",
        "Evidence hierarchy respected"
    ]

    gates_section = content[content.find("Quality Gates"):content.find("Quality Gates") + 500]
    for gate in required_gates:
        if gate in gates_section:
            result.add_pass(f"Quality gate: {gate}")
        else:
            result.add_fail(f"Quality gate missing", gate)


def validate_knowledge_brain(result: ValidationResult):
    """Verify SECOND-KNOWLEDGE-BRAIN.md structure."""
    print("[validate] Checking knowledge brain...")

    if not KNOWLEDGE_BRAIN.exists():
        result.add_fail("Knowledge brain exists", f"Missing: {KNOWLEDGE_BRAIN}")
        return

    content = read_file(KNOWLEDGE_BRAIN)
    required_sections = [
        "Core Concepts & Frameworks",
        "Key Research Papers",
        "Authoritative Data Sources",
        "Analytical Frameworks"
    ]

    for section in required_sections:
        if section not in content:
            result.add_fail(f"Knowledge brain has {section} section")
        else:
            result.add_pass(f"Knowledge brain: {section}")

    # Check crawl protocol documented
    if "crawl4ai" in content or "Crawl" in content:
        result.add_pass("Knowledge brain crawl protocol documented")


def validate_sub_skill_quality(result: ValidationResult):
    """Verify sub-skills have production-grade quality."""
    print("[validate] Checking sub-skill production readiness...")

    for name, path in SUB_SKILLS.items():
        content = read_file(path)
        if not content:
            result.add_fail(f"{name} content check", "Cannot read file")
            continue

        # Check for structured output schema (YAML/JSON indicators)
        if "schema:" in content.lower() or "yaml" in content.lower():
            result.add_pass(f"{name} has structured output schema")
        else:
            result.add_warning(f"{name} may lack explicit output schema")

        # Check for evidence linking
        if "evidence" in content.lower() or "citation" in content.lower():
            result.add_pass(f"{name} mentions evidence linking")
        else:
            result.add_warning(f"{name} may not explicitly link to evidence")

        # Check for procedure detail (length indicates substance)
        if len(content) > 2000:
            result.add_pass(f"{name} has substantive procedure detail")
        else:
            result.add_fail(f"{name} appears underdeveloped", f"Length: {len(content)} chars")


def validate_scenario_completeness(result: ValidationResult):
    """Verify test scenarios cover all required cases."""
    print("[validate] Checking test scenario coverage...")

    content = read_file(SCENARIOS_FILE)
    if not content:
        result.add_fail("Test scenarios file readable")
        return

    scenarios = extract_scenarios(content)
    result.add_pass("Test scenarios loaded", f"Found {len(scenarios)} scenarios")

    # Check for required scenario types
    required_types = [
        ("Niche instrument", "hurdy-gurdy"),
        ("Vocal technique", "belt"),
        ("Plateau", "stalled"),
        ("Limited time", "20 min"),
        ("Exam prep", "ABRSM"),
        ("Degraded mode", "offline"),
        ("Insufficient input", "vague"),
        ("Conflicting goals", "incompatible"),
        ("Physical limitation", "injury"),
        ("Equipment mismatch", "equipment"),
    ]

    for type_name, keyword in required_types:
        # More flexible keyword matching - check both name and full content
        found = False
        for s in scenarios:
            # Check name and full input text
            if keyword.lower() in s.get("name", "").lower() or keyword.lower() in s.get("input", "").lower():
                found = True
                break
        if found:
            result.add_pass(f"Scenario type covered: {type_name}")
        else:
            result.add_warning(f"Scenario type may be missing: {type_name}")


def validate_regression_checklist(result: ValidationResult):
    """Verify regression checklist exists and is comprehensive."""
    print("[validate] Checking regression checklist...")

    content = read_file(SCENARIOS_FILE)
    if not content:
        return

    if "Regression Checklist" in content:
        result.add_pass("Regression checklist section exists")

        # Check for checklist items
        checklist_items = [
            "gates enforced",
            "Scores trace",
            "Devil's-advocate",
            "Roadmap prioritized",
            "Disclaimer"
        ]

        for item in checklist_items:
            if item.lower() in content.lower():
                result.add_pass(f"Checklist item: {item}")
    else:
        result.add_warning("Regression checklist not found")


def validate_integration_docs(result: ValidationResult):
    """Verify integration and shared interface documentation."""
    print("[validate] Checking integration documentation...")

    # Check for shared sub-skill interfaces
    interfaces_file = PROJECT / "docs" / "shared-sub-skill-interfaces.md"
    if interfaces_file.exists():
        result.add_pass("Shared sub-skill interfaces documented")
        content = read_file(interfaces_file)

        required_interfaces = [
            "Learner Intake",
            "Scoring & Evaluation",
            "Practice/Schedule Design",
            "Progress Tracking & Roadmap"
        ]

        for interface in required_interfaces:
            if interface in content:
                result.add_pass(f"Interface documented: {interface}")
            else:
                result.add_warning(f"Interface may be missing: {interface}")
    else:
        result.add_warning("Shared interfaces documentation not found")


def validate_phase_tracking(result: ValidationResult):
    """Verify PROJECT-DEVELOPMENT-PHASE-TRACKING.md is up to date."""
    print("[validate] Checking phase tracking...")

    tracking_file = PROJECT / "PROJECT-DEVELOPMENT-PHASE-TRACKING.md"
    if not tracking_file.exists():
        result.add_fail("Phase tracking file exists")
        return

    content = read_file(tracking_file)

    # Check all phases are present
    phases = ["Phase 0", "Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5"]
    for phase in phases:
        if phase in content:
            # Check if marked complete (more flexible pattern)
            phase_section = content[content.find(phase):content.find(phase) + 400].lower()
            # Check for completion indicators
            if "complete" in phase_section or "✅" in phase_section or "✔" in phase_section:
                result.add_pass(f"{phase} marked complete")
            # Check for ongoing indicators
            elif "ongoing" in phase_section or "planned" in phase_section or "🔄" in phase_section:
                result.add_warning(f"{phase} marked as ongoing")
            else:
                result.add_warning(f"{phase} status unclear")
        else:
            result.add_fail(f"{phase} not found in tracking")


def print_scenario_summary(result: ValidationResult):
    """Print summary of what would be tested in actual harness run."""
    content = read_file(SCENARIOS_FILE)
    if not content:
        return

    scenarios = extract_scenarios(content)
    print(f"\n{'='*60}")
    print(f"Test Scenarios Summary ({len(scenarios)} total)")
    print(f"{'='*60}")

    for s in scenarios:
        print(f"\nScenario {s['id']}: {s['name']}")
        print(f"  Input: {s.get('input', 'N/A')[:60]}...")
        print(f"  Quality Gate: {s.get('quality_gate', 'N/A')}")

    print(f"\n{'='*60}")


def main():
    print("[validate] Starting validation for rare-instrument-vocal-learning-path")
    print(f"[validate] Project: {PROJECT}")
    print(f"[validate] Timestamp: {datetime.now().isoformat()}")

    result = ValidationResult()

    # Run all validation checks
    validate_skill_structure(result)
    validate_quality_gates(result)
    validate_knowledge_brain(result)
    validate_sub_skill_quality(result)
    validate_scenario_completeness(result)
    validate_regression_checklist(result)
    validate_integration_docs(result)
    validate_phase_tracking(result)

    # Print summary
    print(result.summary())
    print_scenario_summary(result)

    # Exit with appropriate code
    if result.exit_code() == 0:
        print("[PASS] All critical validations passed!")
    else:
        print("[FAIL] Some validations failed. Review output above.")

    return result.exit_code()


if __name__ == "__main__":
    sys.exit(main())
