#!/usr/bin/env python3
"""Package BuildAnything skills for drag-and-drop installers (e.g. Bionic).

Requirement being satisfied: a folder must contain a SKILL.md file, and a
SKILL.md must include the skill name and description in YAML.

Produces in dist/:
  BuildAnything-<skill-id>.zip   one zip per skill; archive root is the
                                 skill folder (contains SKILL.md), so it can
                                 be dragged/selected directly.
  BuildAnything-all.zip          all 19 skill folders at the archive root.
"""

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKIP_DIRS = {"__pycache__", ".git", "dist", "node_modules"}


def skill_folders():
    return sorted(
        (p.parent for p in ROOT.glob("*/SKILL.md")),
        key=lambda p: p.name,
    )


def add_folder(zf: zipfile.ZipFile, folder: Path, prefix: str) -> int:
    count = 0
    for path in sorted(folder.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            arcname = f"{prefix}/{path.relative_to(folder).as_posix()}"
            zf.write(path, arcname)
            count += 1
    return count


def main() -> int:
    skills = skill_folders()
    if not skills:
        print("No skills found.", file=sys.stderr)
        return 1

    DIST.mkdir(exist_ok=True)
    for old in DIST.glob("*.zip"):
        old.unlink()

    total_files = 0
    for skill in skills:
        out = DIST / f"BuildAnything-{skill.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            total_files += add_folder(zf, skill, skill.name)
        print(f"  {out.name}")

    bundle = DIST / "BuildAnything-all.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as zf:
        for skill in skills:
            add_folder(zf, skill, skill.name)
    print(f"  {bundle.name}")

    print(f"\n{len(skills)} skill zips + 1 bundle -> {DIST} ({total_files} files packed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
