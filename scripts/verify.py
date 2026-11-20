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
        "build-anything/references/first-time-guide.md",
        "build-anything/references/question-bank.md",
        "caveman-report/SKILL.md",
        "caveman-report/references/modes.md",
        "eval/README.md",
        "eval/TASKS.md",
        "eval/RESULTS.md",
    ]
    for rel in required:
        p = ROOT / rel
        assert p.is_file(), f"Missing core file: {rel}"
    print(f"  OK: {len(required)} core files present.")


def _frontmatter(text: str, skill_id: str) -> dict:
    """Parse and strictly validate a SKILL.md frontmatter block.

    Uses PyYAML when available (CI installs it); otherwise a strict built-in
    scan. Returns the parsed mapping.
    """
    assert text.startswith("---"), f"{skill_id}/SKILL.md missing opening '---'"
    try:
        import yaml  # type: ignore
    except ImportError:
        yaml = None

    end = text.find("\n---", 3)
    assert end != -1, f"{skill_id}/SKILL.md missing closing '---'"
    block = text[3:end].lstrip("\n")

    if yaml is not None:
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError as e:
            raise AssertionError(f"{skill_id}/SKILL.md has invalid YAML: {e}")
        assert isinstance(data, dict), f"{skill_id}/SKILL.md frontmatter is not a mapping"
        return data

    # Fallback: strict line scan (key: value at column 0, non-empty values)
    data: dict = {}
    key = None
    for raw in block.splitlines():
        if raw[:1] in (" ", "\t"):
            if key is None:
                raise AssertionError(f"{skill_id}/SKILL.md frontmatter starts with an indented line")
            continue  # continuation / nested block
        if ":" not in raw:
            raise AssertionError(f"{skill_id}/SKILL.md frontmatter line is not 'key: value': {raw!r}")
        key, _, value = raw.partition(":")
        assert key.strip() == key and key, f"{skill_id}/SKILL.md bad key: {key!r}"
        data[key.strip()] = value.strip()
    return data


def test_skills_frontmatter():
    print("Checking skill definitions (strict YAML)...")
    skill_files = list(ROOT.glob("*/SKILL.md"))
    assert len(skill_files) == 20, f"Expected 20 skills, found {len(skill_files)}"

    try:
        import yaml  # noqa: F401
        mode = "PyYAML"
    except ImportError:
        mode = "built-in parser"

    for sf in skill_files:
        skill_id = sf.parent.name
        data = _frontmatter(sf.read_text(encoding="utf-8"), skill_id)
        name = data.get("name")
        desc = data.get("description")
        assert isinstance(name, str) and name.strip(), f"{skill_id}: 'name' missing/empty"
        assert isinstance(desc, str) and desc.strip(), f"{skill_id}: 'description' missing/empty"

    print(f"  OK: All 20 skills valid ({mode}).")


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


def test_skill_cross_references():
    print("Checking working card's references/ pointers resolve...")
    card = ROOT / "build-anything" / "SKILL.md"
    text = card.read_text(encoding="utf-8")
    import re

    targets = sorted(set(re.findall(r"references/([a-z0-9\-]+\.md)", text)))
    assert targets, "No references/ pointers found in the working card"
    for t in targets:
        p = ROOT / "build-anything" / "references" / t
        assert p.is_file(), f"Working card points at missing file: references/{t}"
    print(f"  OK: {len(targets)} pointer(s) all resolve.")


def main():
    print(f"Running BuildAnything verification in: {ROOT}")
    try:
        test_core_files()
        test_skills_frontmatter()
        test_skill_cross_references()
        test_eval_fixtures()
        print("\nALL CHECKS PASSED.")
        return 0
    except AssertionError as e:
        print(f"\nVERIFICATION FAILED: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
