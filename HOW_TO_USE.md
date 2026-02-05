# HOW_TO_USE.md — Spec-Driven Research (SDR)

Dokumen ini menjelaskan cara pakai repo **Spec-Driven Research** untuk menghasilkan riset yang *dalam by default* dengan pola:
**SPEC → CLAIMS → EVIDENCE → REPORT → VALIDATE → PR**

Repo ini dirancang supaya LLM/agent **nggak bisa “asal rangkum”**: setiap klaim harus punya bukti, dan report harus traceable.

---

## 0) Konsep 30 detik (biar kebayang)
- **SPEC.md**: kontrak riset (scope, RQ, deliverable, Definition of Done).
- **METHOD.md**: cara kerja (search strategy, rubric evidence, logging).
- **CLAIMS.yml**: daftar klaim atomik (C1..Cn) yang wajib dibuktikan.
- **EVIDENCE.csv**: tabel bukti untuk tiap klaim (link + kutipan + tanggal + strength).
- **REPORT.md**: sintesis akhir, setiap paragraf refer ke claim_id seperti `[C1]`.
- **Validator**: memastikan kualitas (claim punya ≥2 evidence, report punya referensi claim).

> Aturan utama SDR: **tidak boleh nulis REPORT sebelum EVIDENCE lengkap**.

---

## 1) Setup cepat (lokal)
### 1.1 Install dependencies
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

### 1.2 Buat project riset baru

```bash
python scripts/new_project.py "nama-topik"
```

Hasilnya dibuat di:

```
projects/nama-topik/
  SPEC.md
  METHOD.md
  CLAIMS.yml
  EVIDENCE.csv
  REPORT.md
```

---

## 2) Cara kerja manual (tanpa agent) — baseline yang aman

1. Isi `projects/<slug>/SPEC.md`:

   * decision / goal
   * scope (in/out)
   * research questions (RQ)
   * Definition of Done (DoD)

2. Isi `projects/<slug>/METHOD.md`:

   * sumber primer/sekunder
   * query plan
   * inclusion/exclusion
   * rubric evidence (HIGH/MED/LOW)

3. Tulis `CLAIMS.yml` (klaim atomik):

   * pecah RQ jadi klaim yang bisa diverifikasi
   * prioritaskan P0 (paling menentukan keputusan)

4. Isi `EVIDENCE.csv`:

   * minimal 2 baris per claim_id
   * wajib ada `date_accessed` + `quote` + `evidence_strength`
   * kalau ada konflik sumber, tulis sebagai counterevidence row

5. Baru tulis `REPORT.md`:

   * setiap paragraf harus menyebut `[C#]`
   * ada bagian uncertainty + known unknowns + next searches

6. Jalankan validator:

```bash
python scripts/validate_project.py projects/<slug>
```

Kalau validator gagal, berarti *kedalaman belum memenuhi spec*.

---

## 3) Cara kerja semi-otomatis (agent) — recommended

Repo menyediakan adapter:

```bash
python scripts/run_agent.py projects/<slug> --runner <runner>
```

Secara default, setiap kali kamu menjalankan `run_agent.py`, repo akan menulis history singkat ke file:
- `projects/<slug>/RUN_LOG.md`

Isinya berupa metadata run (runner, waktu, perintah CLI yang dipanggil dalam bentuk redacted, status OK/ERROR). Ini berguna untuk audit trail tanpa menyimpan seluruh chat.

Kalau kamu tidak mau logging (mis. karena privacy), jalankan:
```bash
python scripts/run_agent.py projects/<slug> --runner <runner> --no-log
```

Catatan:
- `scripts/run_agent.py` adalah mode **cross-platform (Windows/Linux/Mac)**.
- `scripts/run_agent.sh` masih ada sebagai opsi **Linux/Mac** kalau kamu memang pakai bash.

### 3.1 Runner yang tersedia

* `gemini` → Gemini CLI (paling enak kalau mau web search/fetch)
* `claude` → Claude Code CLI
* `codex` → OpenAI Codex CLI
* `copilot` → stub (Copilot idealnya dipakai di IDE/terminal, bukan CI)
* `kilo` → stub (local-first)
* `opencode` → stub (local-first)
* `antigravity` → stub (interactive/local)

> “stub” artinya: repo sudah siapkan slot/adapternya, tapi kamu perlu isi command sesuai setup tool kamu.

### 3.2 Cara pakai agent (pola standar)

1. Pastikan `SPEC.md` dan `METHOD.md` sudah benar.
2. Jalankan agent:

```bash
python scripts/run_agent.py projects/<slug> --runner gemini
# atau:
python scripts/run_agent.py projects/<slug> --runner claude
# atau:
python scripts/run_agent.py projects/<slug> --runner codex
```

3. Jalankan validator:

```bash
python scripts/validate_project.py projects/<slug>
```

4. Kalau gagal:

   * perbaiki `CLAIMS.yml` (klaim terlalu besar/ambigu)
   * tambah evidence row
   * perbaiki referensi `[C#]` di report

---

## 4) Cara kerja “paling bener”: iterasi 3 loop

Untuk mendapatkan riset yang bener-bener dalam, pakai 3 loop berikut:

### Loop A — Claim shaping (kualitas pertanyaan)

Tujuan: klaim jadi *atomic & testable*.

* Pecah klaim besar jadi 2–5 klaim kecil.
* Pastikan tiap klaim bisa “dibuktikan” lewat sumber.

### Loop B — Evidence widening (triangulasi)

Tujuan: bukti tidak single-source.

* Minimal 2 sumber independen per claim.
* Klaim angka/teknis wajib 1 sumber primer.

### Loop C — Synthesis & red-team

Tujuan: report tidak sekadar ringkas.

* Tulis counterargument.
* Tulis boundary conditions (kapan klaim tidak berlaku).
* Tulis “Known unknowns” + next searches.

---

## 5) Quality gates (Definition of Done) default

Validator repo ini memaksa:

* **≥2 evidence rows** per claim_id
* evidence row wajib:

  * `source_url`
  * `date_accessed`
  * `quote`
  * `evidence_strength` ∈ {HIGH, MED, LOW}
* `REPORT.md` harus punya minimal 1 referensi claim `[C#]`
* `REPORT.md` tidak boleh merefer claim yang tidak ada di `CLAIMS.yml`

> Kamu bisa menambah rules (lebih ketat) lewat:

* menambah aturan di `prompts/SDR_RULES.txt`
* memperluas `scripts/validate_project.py`

---

## 6) Cara pakai di GitHub (CI)

### 6.1 PR gate: validate otomatis

Workflow:

* `.github/workflows/validate.yml`

Ketika kamu PR perubahan di `projects/**`, CI akan:

* install dependencies
* validasi semua project folder yang punya `SPEC.md`

### 6.2 Manual dispatch: jalankan agent dari GitHub Actions

Workflow:

* `.github/workflows/research.yml`

Cara pakai:

1. buka tab **Actions**
2. pilih workflow **Run SDR Agent (manual dispatch)**
3. input:

   * `project_path`: `projects/<slug>`
   * `runner`: `none|gemini|claude|codex|...`

**Secrets** (kalau runner butuh):

* `OPENAI_API_KEY`
* `ANTHROPIC_API_KEY`
* `GEMINI_API_KEY`

> Catatan: install CLI di GitHub Actions kadang tricky. Cara paling stabil:
> jalankan agent **lokal**, push hasilnya, biarkan CI hanya “validate”.

---

## 7) Cara pakai dengan tool spesifik (praktik recommended)

### 7.1 GitHub Copilot (IDE/terminal)

Copilot paling berguna untuk:

* memecah klaim jadi atomic (refactor CLAIMS.yml)
* memperbaiki struktur REPORT
* memperbaiki validator/rules
* membantu review PR (bukan scraping web)

Workflow Copilot:

1. kamu buka project folder di VS Code
2. minta Copilot:

   * “Refine CLAIMS.yml to be atomic”
   * “Fill EVIDENCE.csv rows and add missing fields”
   * “Ensure REPORT.md references claim ids”
3. jalankan validator

### 7.2 Codex CLI

Codex cocok untuk:

* edit file + run validator + iterasi cepat
* bikin perubahan terstruktur tanpa kamu bolak-balik copy-paste

Workflow:

```bash
python scripts/run_agent.py projects/<slug> --runner codex
python scripts/validate_project.py projects/<slug>
```

### 7.3 Claude Code CLI

Claude cocok untuk:

* reasoning + drafting report yang rapi
* menyusun counterevidence & uncertainty

Workflow:

```bash
python scripts/run_agent.py projects/<slug> --runner claude
python scripts/validate_project.py projects/<slug>
```

### 7.4 Gemini CLI

Gemini cocok untuk:

* web search/fetch (kalau kamu memang melakukan browsing untuk evidence)

Workflow:

```bash
python scripts/run_agent.py projects/<slug> --runner gemini
python scripts/validate_project.py projects/<slug>
```

### 7.5 Kilo / OpenCode / Antigravity

Gunakan untuk local-first agentic editing. Minimum pattern yang harus kamu jaga:

* agent membaca `prompts/SDR_RULES.txt`
* agent bekerja di `projects/<slug>/`
* hasil akhir harus lulus validator

Repo ini menyediakan “slot” di `scripts/run_agent.sh` untuk kamu isi command spesifik sesuai instalasi kamu.

Jika kamu bikin project baru dengan `python scripts/new_project.py "nama-topik"`, isi file akan otomatis mengganti placeholder `<project name>` menjadi nama yang kamu input.

Catatan git:
- Repo ini meng-ignore semua folder di `projects/` kecuali `projects/contoh-topik/`.
- Jadi project baru default-nya untuk kerja lokal, dan tidak kepush sampai kamu ubah `.gitignore`.

---

## 8) Troubleshooting (yang paling sering kejadian)

### “Validator fail: Claim Cx has only 1 evidence row”

Solusi:

* tambah minimal 1 evidence entry lagi untuk claim_id itu (sumber berbeda)
* atau pecah claim jadi lebih kecil supaya lebih mudah dibuktikan

### “Validator fail: missing quote/date_accessed”

Solusi:

* isi `date_accessed` (format YYYY-MM-DD)
* isi `quote` (kutipan pendek dari sumber)

### “Report references unknown claim_id”

Solusi:

* pastikan di `REPORT.md` hanya pakai `[C1]` yang ada di `CLAIMS.yml`
* atau tambahkan claim baru di `CLAIMS.yml` (lebih baik: jangan tambahin sembarang)

### “Riset masih terasa dangkal”

Biasanya masalahnya:

* CLAIM terlalu besar (tidak atomic)
* evidence cuma 1 jenis sumber
* report tidak ada counterevidence / boundary

Fix:

* pecah claim
* tambah sumber primer
* tulis bagian “Counterevidence & uncertainty”
* tulis “Known unknowns + next searches”

---

## 9) Minimal best-practice untuk “kedalaman”

Kalau kamu cuma mau 5 aturan paling penting:

1. claim atomik (1 kalimat, bisa benar/salah)
2. 2 sumber independen per claim
3. simpan kutipan dan tanggal akses
4. report harus refer claim_id, bukan “katanya”
5. selalu tulis counterevidence + known unknowns

---

## 10) Checklist cepat sebelum publish report

* [ ] Apakah semua klaim P0 punya evidence HIGH/MED?
* [ ] Apakah ada counterevidence untuk klaim yang kontroversial?
* [ ] Apakah report menyebut batasan & asumsi?
* [ ] Apakah “Known unknowns” berisi query lanjutan yang spesifik?

Kalau semua OK, report kamu biasanya sudah “setara deep research”.