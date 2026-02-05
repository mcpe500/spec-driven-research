# Repo structure

## Root
- `projects/` : folder per riset/topik.
- `prompts/`  : rules/kontrak perilaku agent.
- `scripts/`  : tooling deterministic (scaffold, validate, helpers).
- `.github/`  : CI + templates.

## Project folder (`projects/<slug>/`)
Minimal files:
- `SPEC.md`    : decision, scope, RQ, deliverables, DoD.
- `METHOD.md`  : strategi pencarian, rubric bukti, log pencarian.
- `CLAIMS.yml` : daftar klaim atomik (id + text + type + priority).
- `EVIDENCE.csv`: bukti per klaim (quote, dates, strength).
- `REPORT.md`  : sintesis, wajib refer `claim_id` (mis. `[C1]`).
