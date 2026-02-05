#!/usr/bin/env python3
"""Validate an SDR project's artifacts against quality gates."""

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

RE_CLAIM_REF = re.compile(r"\[C\d+\]")


def die(msg: str) -> None:
    """Print error message and exit."""
    print(f"VALIDATION FAILED: {msg}", file=sys.stderr)
    sys.exit(1)


def load_claim_ids(claims_path: Path) -> list:
    """Load claim IDs from CLAIMS.yml."""
    data = yaml.safe_load(claims_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "claims" not in data:
        die(f"{claims_path} must contain top-level 'claims:' list")
    claims = data["claims"]
    if not isinstance(claims, list) or not claims:
        die(f"{claims_path} must have a non-empty claims list")
    ids = []
    for c in claims:
        if not isinstance(c, dict) or "id" not in c or "text" not in c:
            die(f"Each claim must be a dict with at least 'id' and 'text' in {claims_path}")
        ids.append(str(c["id"]).strip())
    return ids


def read_evidence_rows(evidence_path: Path) -> list:
    """Read and validate EVIDENCE.csv columns."""
    with evidence_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = {
            "claim_id",
            "source_url",
            "title",
            "publisher",
            "date_published",
            "date_accessed",
            "quote",
            "evidence_strength",
            "notes",
        }
        missing = required - set(reader.fieldnames or [])
        if missing:
            die(f"{evidence_path} missing columns: {sorted(missing)}")
        rows = list(reader)
    return rows


def validate_coverage(claim_ids: list, rows: list, evidence_path: Path) -> None:
    """Validate each claim has >= 2 evidence rows with required fields."""
    by_claim = {cid: [] for cid in claim_ids}
    for r in rows:
        cid = (r.get("claim_id") or "").strip()
        if cid in by_claim:
            by_claim[cid].append(r)

    for cid in claim_ids:
        entries = by_claim.get(cid, [])
        if len(entries) < 2:
            die(f"Claim {cid} has only {len(entries)} evidence row(s); need >= 2 in {evidence_path}")

        for idx, r in enumerate(entries, start=1):
            if not (r.get("source_url") or "").strip():
                die(f"Claim {cid} evidence row #{idx} missing source_url")
            if not (r.get("date_accessed") or "").strip():
                die(f"Claim {cid} evidence row #{idx} missing date_accessed")
            if not (r.get("quote") or "").strip():
                die(f"Claim {cid} evidence row #{idx} missing quote")
            strength = (r.get("evidence_strength") or "").strip().upper()
            if strength not in {"HIGH", "MED", "LOW"}:
                die(f"Claim {cid} evidence row #{idx} evidence_strength must be HIGH/MED/LOW")


def validate_report_refs(report_path: Path, claim_ids: list) -> None:
    """Validate REPORT.md references claim IDs."""
    text = report_path.read_text(encoding="utf-8")
    refs = set(RE_CLAIM_REF.findall(text))
    ref_ids = {r.strip("[]") for r in refs}

    if not ref_ids:
        die(f"{report_path} has no claim references like [C1]")

    unknown = sorted([rid for rid in ref_ids if rid not in claim_ids])
    if unknown:
        die(f"{report_path} references unknown claim_id(s): {unknown}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Validate an SDR project"
    )
    ap.add_argument("project_path", help="Path to project folder, e.g. projects/my-topic")
    args = ap.parse_args()

    p = Path(args.project_path)
    if not p.exists() or not p.is_dir():
        die(f"Project path not found: {p}")

    spec = p / "SPEC.md"
    method = p / "METHOD.md"
    claims = p / "CLAIMS.yml"
    evidence = p / "EVIDENCE.csv"
    report = p / "REPORT.md"

    for fp in [spec, method, claims, evidence, report]:
        if not fp.exists():
            die(f"Missing required file: {fp}")

    claim_ids = load_claim_ids(claims)
    rows = read_evidence_rows(evidence)
    validate_coverage(claim_ids, rows, evidence)
    validate_report_refs(report, claim_ids)

    print(f"VALIDATION OK: {p}")


if __name__ == "__main__":
    main()
