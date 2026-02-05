# Pipeline (automation)

Ada dua workflow utama:

1) `validate.yml` (PR gate)
- Trigger: pull_request
- Action: `python scripts/validate_project.py <path>` untuk setiap folder project yang berubah
- Tujuan: memastikan *kedalaman* terjaga via rules deterministic

2) `research.yml` (manual dispatch)
- Trigger: workflow_dispatch
- Input: `project_path` + `runner`
- Step:
  a) jalankan `scripts/run_agent.py` (cross-platform) atau `scripts/run_agent.sh` (bash) untuk runner pilihan
  b) jalankan validator
  c) (opsional) commit & push perubahan

## Runner support
Runner adapter ada di:
- `scripts/run_agent.py` (Python, cross-platform - **recommended**)
- `scripts/run_agent.sh` (Bash, Linux/Mac only)

Ia akan:
- cek command ada/tidak
- menjalankan agent dengan prompt rules (`prompts/SDR_RULES.txt`) + konteks project

## Running locally

**Cross-platform (Windows/Linux/Mac):**
```bash
python scripts/run_agent.py projects/<slug> --runner gemini
```

**Linux/Mac only (bash):**
```bash
SDR_RUNNER=gemini bash scripts/run_agent.sh projects/<slug>
```

Catatan penting:
- CI environment beda-beda; beberapa CLI mungkin tidak tersedia.
- Untuk runner yang belum stabil di CI, jalankan lokal dengan pola yang sama.
