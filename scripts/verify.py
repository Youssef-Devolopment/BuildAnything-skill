#!/usr/bin/env python3
"""BuildAnything self-verification script.

Verifies:
1. Every skill folder contains a valid SKILL.md with frontmatter (name + description).
2. All eval fixtures behave as expected (f1, f4, f7 must fail; f8 must pass).
3. Core repo files exist.
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_core_files():
    print("Checking core files...")
    required = [
        "README.md",
        "CHANGELOG.md",
        "install.ps1",
        "update.ps1",
        "build-anything/SKILL.md",
        "build-anything/references/core-protocol.md",
        "eval/README.md",
        "eval/TASKS.md",
        "eval/RESULTS.md",
    ]
    for rel in required:
        p = ROOT / rel
        assert p.is_file(), f"Missing core file: {rel}"
    print(f"  OK: {len(required)} core files present.")


def test_skills_frontmatter():
    print("Checking skill definitions...")
    skill_files = list(ROOT.glob("*/SKILL.md"))
    assert len(skill_files) == 19, f"Expected 19 skills, found {len(skill_files)}"

    for sf in skill_files:
        skill_id = sf.parent.name
        content = sf.read_text(encoding="utf-8")
        assert content.startswith("---"), f"{skill_id}/SKILL.md missing frontmatter start '---'"
        parts = content.split("---", 2)
        assert len(parts) >= 3, f"{skill_id}/SKILL.md malformed frontmatter"
        frontmatter = parts[1]
        assert "name:" in frontmatter, f"{skill_id}/SKILL.md missing 'name:'"
        assert "description:" in frontmatter, f"{skill_id}/SKILL.md missing 'description:'"

    print(f"  OK: All 19 skills have valid frontmatter.")


def test_eval_fixtures():
    print("Checking eval fixtures (expected red/green states)...")
    fixtures = [
        ("eval/fixtures/f1-bug/test_calc.py", 1, "f1-bug must fail"),
        ("eval/fixtures/f4-tricky/test_app.py", 1, "f4-tricky must fail"),
        ("eval/fixtures/f7-truth/test_tasks.py", 1, "f7-truth must fail"),
        ("eval/fixtures/f8-project/test_wordcount.py", 0, "f8-project must pass"),
    ]

    for rel_path, expected_code, msg in fixtures:
        path = ROOT / rel_path
        assert path.is_file(), f"Fixture file not found: {rel_path}"
        proc = subprocess.run(
            [sys.executable, str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        assert proc.returncode == expected_code, (
            f"Fixture check failed for {rel_path}: "
            f"expected returncode {expected_code}, got {proc.returncode}. {msg}"
        )

    print("  OK: 4 test fixtures verified (f1=1, f4=1, f7=1, f8=0).")


def main():
    print(f"Running BuildAnything verification in: {ROOT}")
    try:
        test_core_files()
        test_skills_frontmatter()
        test_eval_fixtures()
        print("\nALL CHECKS PASSED.")
        return 0
    except AssertionError as e:
        print(f"\nVERIFICATION FAILED: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
