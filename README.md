# Spec-Driven Research (SDR) – Repo Template

Ini template repo untuk **Spec-Driven Research**: riset diperlakukan seperti engineering.
Output riset bukan cuma narasi, tapi **artefak terstruktur** yang bisa divalidasi (claim → evidence → report).

## Konsep inti
- **SPEC**: apa yang harus dijawab (scope, RQ, DoD).
- **METHOD**: gimana cara cari & menilai bukti.
- **CLAIMS**: daftar klaim atomik yang wajib dibuktikan.
- **EVIDENCE**: tabel bukti (link + kutipan + tanggal + strength).
- **REPORT**: sintesis yang *traceable* ke claim_id.

Repo ini juga menyiapkan pipeline:
- **CI validation** (PR wajib lulus validator).
- **Runner adapter** untuk berbagai agent/CLI:
  - GitHub Copilot (lebih cocok untuk review/iterasi di IDE/terminal)
  - OpenAI Codex CLI
  - Claude Code CLI
  - Gemini CLI
  - Kilo Code / OpenCode / Antigravity (lebih "local-first"; adapter disediakan)

> Catatan: beberapa tool (khususnya antigravity) lebih realistis dijalankan **lokal** daripada GitHub Actions.
> Repo ini tetap menyediakan pola yang sama: agent update artifacts → validator memastikan kualitas.

---

## Quick start (lokal)
1) Buat virtualenv dan install deps:

**Linux/Mac:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

2. Scaffold project riset baru:

```bash
python scripts/new_project.py "contoh-topik"
```

3. Isi `projects/contoh-topik/`:

* SPEC.md (scope/RQ/DoD)
* METHOD.md (standar bukti)
* CLAIMS.yml (klaim atomik)
* EVIDENCE.csv (bukti)
* REPORT.md (sintesis)

4. Jalankan validator:

```bash
python scripts/validate_project.py projects/contoh-topik
```

5. Jalankan agent (cross-platform):

```bash
python scripts/run_agent.py projects/contoh-topik --runner gemini
```

---

## Pipeline (GitHub)

* Setiap PR akan menjalankan `.github/workflows/validate.yml`.
* Workflow `.github/workflows/research.yml` bisa dipicu manual (`workflow_dispatch`) untuk menjalankan agent runner tertentu.

### Secrets (opsional, kalau mau agent jalan di Actions)

Tambahkan secrets di repo settings (nama umum):

* `OPENAI_API_KEY` (Codex CLI)
* `ANTHROPIC_API_KEY` (Claude Code)
* `GEMINI_API_KEY` (Gemini CLI)
* `GITHUB_TOKEN` sudah tersedia untuk workflow (buat push/commit jika diperlukan)

Lihat `docs/pipeline.md` untuk detail.

---

## Cara kerja "kedalaman" (Definition of Done)

Default quality gates ada di `prompts/SDR_RULES.txt` + validator:

* tiap claim punya **>= 2 evidence entries**
* evidence wajib punya **quote** + **date_accessed** + **strength**
* report wajib merefer `claim_id` (contoh: `[C12]`)

Kamu bisa memperketat aturan di `SPEC.md` per project.

---

## Struktur repo

Lihat `docs/structure.md` untuk penjelasan.
