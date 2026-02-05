#!/usr/bin/env python3
"""Scaffold a new SDR project from templates."""

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
PROJECTS = ROOT / "projects"


def slugify(s: str) -> str:
    """Convert a string to a safe slug for folder names."""
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\-_\s]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s or "project"


def replace_project_name_placeholders(path: Path, project_name: str) -> None:
    """Replace '<project name>' placeholders in a text file (best-effort)."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    if "<project name>" not in text:
        return
    path.write_text(text.replace("<project name>", project_name), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Create a new SDR project scaffold"
    )
    ap.add_argument("name", help="Project name/slug (e.g. 'market-entry-id')")
    args = ap.parse_args()

    project_name = args.name.strip() or "project"
    slug = slugify(args.name)
    dest = PROJECTS / slug
    dest.mkdir(parents=True, exist_ok=True)

    mapping = {
        "PROJECT_SPEC.md": "SPEC.md",
        "PROJECT_METHOD.md": "METHOD.md",
        "PROJECT_CLAIMS.yml": "CLAIMS.yml",
        "PROJECT_EVIDENCE.csv": "EVIDENCE.csv",
        "PROJECT_REPORT.md": "REPORT.md",
    }

    for src_name, dst_name in mapping.items():
        src = TEMPLATES / src_name
        dst = dest / dst_name
        if dst.exists():
            print(f"Skipping {dst_name} (already exists)")
            continue
        shutil.copyfile(src, dst)
        replace_project_name_placeholders(dst, project_name)
        print(f"Created {dst_name}")

    print(f"\nCreated project scaffold at: {dest}")


if __name__ == "__main__":
    main()
