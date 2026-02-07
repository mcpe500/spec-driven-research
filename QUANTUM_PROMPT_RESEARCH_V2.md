# QUANTUM_PROMPT_RESEARCH_V1

## Tujuan

Mempublikasikan prompt template untuk riset bertema quantum pada topik **<TOPIK>** dengan pendekatan **spec-driven research**.

## Instruksi utama (wajib)

- Tugas anda adalah **mengeksekusi prompt**.
- **PAHAMI mengeksekusi prompt ini**.
- jika belum ada struktur maka buatlah struktur folder atau file output apa pun. Dokumen ini hanya template instruksi.

---

# Prompt — Spec-Driven Research (Struktur Baru)

Gunakan metode **spec-driven research** dengan struktur output yang rapi dan mudah dinavigasi.

Fokus utama versi ini: hasil akhir berupa **dokumen HTML** yang rapi, mudah dibaca, dan kaya visualisasi untuk membantu pemahaman konsep quantum (circuit, state, probabilitas).

## Struktur (konsep) yang dituju

Gunakan struktur berikut sebagai acuan penamaan dan versioning (ini adalah *kontrak struktur*, bukan perintah untuk mengisi konten riset):

```text
spec/
  README.md
  handoff/
  results/
    <TOPIK-SLUG>/
      <TOPIK-SLUG>-v1.html
      <TOPIK-SLUG>-v2.html
      ...
      CHANGELOG.md
```

Contoh `<TOPIK-SLUG>` (hanya contoh):
- `deutsch-jozsa`
- `qft`
- `fft`

## Aturan lokasi output

- `spec/`:
  - dokumen spec topik dan aturan riset.
- `spec/handoff/`:
  - jawaban mentah per pertanyaan + sumber.
  - boleh format poin/Q&A.
- `spec/results/<topik-slug>/`:
  - laporan final naratif.
  - wajib versioning per topik: `<TOPIK-SLUG>-vN.html`.
  - (opsional) subfolder aset jika dibutuhkan:
    - `assets/` (gambar, SVG circuit, data kecil untuk chart, dll.)

## Aturan versioning

- Versi baru selalu menjadi file baru:
  - `<TOPIK-SLUG>-v1.html`, `<TOPIK-SLUG>-v2.html`, `<TOPIK-SLUG>-v3.html`, dst.
- Versi lama tidak ditimpa.
- Buat `CHANGELOG.md` per topik untuk merangkum perubahan antiversi.

Contoh entri changelog:
- `v2: Perjelas 2.3; tambah tracing solusi klasik; rapikan alur 2→3→5`

## Gaya penulisan hasil report

- Bahasa Indonesia, to-the-point, mudah dibaca.
- Hindari kata ganti orang (contoh: `kita`, `aku`, `kamu`).
- Hindari format “jawaban nomor 1/2/3”.
- Tulis sebagai narasi yang mengalir; jika paragraf dibaca, jawaban inti sudah ter-cover.

## Format output (WAJIB: HTML, bukan Markdown)

- Output final yang diberikan adalah **HTML utuh** (bukan Markdown).
- Minimal gunakan struktur HTML yang valid: `<!doctype html>`, `<html>`, `<head>`, `<body>`.
- Gunakan **CSS internal** via `<style>` (agar file bisa dibuka offline).
- Untuk rumus LaTeX, gunakan **KaTeX** atau **MathJax** (disarankan KaTeX via CDN).
- Untuk diagram alur, gunakan **Mermaid**.
- Kode program ditulis dalam `<pre><code>`.

## Aturan visualisasi (WAJIB, quantum-friendly)

Laporan final wajib mengandung visualisasi yang benar-benar membantu:

Wajib ada minimal:

- 1 diagram alur (Mermaid) untuk alur riset/algoritma utama.
- 1 diagram konteks problem nyata (Mermaid: dataflow/sequence/komponen).
- 1 **diagram circuit** (pilih salah satu):
  - SVG inline sederhana, atau
  - tabel “wire x time-step” yang menggambar gate per kolom.
- 1 tabel tracing yang sangat detail untuk bagian quantum (state/amplitudo/probabilitas) per langkah gate penting.
- 1 visualisasi probabilitas hasil ukur (bar chart sederhana) menggunakan HTML+CSS (tanpa library) atau SVG inline.

Catatan:

- Visualisasi boleh sederhana, yang penting akurat dan mudah dibaca.
- Jika memakai CDN untuk Mermaid/KaTeX, tetap sediakan konten fallback (mis. circuit versi tabel) agar tetap terbaca saat offline.

## Struktur isi report (wajib)

1. Definisi masalah / problem statement + contoh problem.
2. Dasar matematika/fisika/mekanika kuantum.
3. Teori quantum computing (qubit, superposition, entanglement, gate seperti Hadamard, CNOT, dll).
4. Solusi klasik + kode sederhana + tracing.
5. Solusi kuantum + circuit + tracing sangat detail.

Alur penjelasan wajib mengalir: **2 → 3 → 5**.

## Kebutuhan kedalaman

- Bagian 2.2, 2.3, 2.4, 2.5 harus panjang, jelas, dan benar.
- Jelaskan konsep dulu dalam kata-kata, lalu notasi.
- Hindari rumus berlebihan; fokus pemahaman pembaca software (mahasiswa S1 Informatika).

## Aturan notasi matematika

Jika menulis notasi matematika, gunakan LaTeX yang rapi, misalnya:

$$
f: \{0,1\}^n \to \{0,1\}.
$$

Tambahan untuk quantum:

- Jelaskan arti notasi Dirac ($|0\rangle$, $|1\rangle$, $|\psi\rangle$) dalam kata-kata.
- Jika menulis matriks gate (H, X, Z, CNOT), jelaskan efeknya secara intuitif.

## Catatan eksekusi

- Gunakan sumber online untuk backup referensi.
- Jika ada PDF internal, gunakan sebagai baseline lalu perkuat dengan sumber online.
- Lingkungan dapat memiliki `.venv`; gunakan jika perlu menjalankan tool lokal.

## Kerangka HTML (template WAJIB diikuti)

Gunakan kerangka berikut sebagai baseline. Isi konten sesuai topik `<TOPIK>` dan pastikan semua visualisasi muncul.

```html
<!doctype html>
<html lang="id">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Spec-Driven Research (Quantum) — <TOPIK></title>
    <style>
      :root { color-scheme: light; }
      body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.55; margin: 24px; }
      main { max-width: 1040px; margin: 0 auto; }
      h1, h2, h3 { line-height: 1.2; }
      code, pre { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
      pre { padding: 12px; overflow: auto; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 8px; }
      table { border-collapse: collapse; width: 100%; }
      th, td { border: 1px solid #d0d7de; padding: 8px; vertical-align: top; }
      th { background: #f6f8fa; text-align: left; }
      .muted { color: #57606a; }
      .grid { display: grid; grid-template-columns: 1fr; gap: 12px; }
      .card { padding: 12px; border: 1px solid #d0d7de; border-radius: 8px; background: #fff; }
      .barRow { display: grid; grid-template-columns: 120px 1fr 60px; gap: 8px; align-items: center; margin: 6px 0; }
      .bar { height: 12px; background: #0969da; border-radius: 999px; }
      .barWrap { height: 12px; background: #eaeef2; border-radius: 999px; overflow: hidden; }
      .nowrap { white-space: nowrap; }
    </style>

    <!-- KaTeX (opsional tapi disarankan) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css" />
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>
  </head>
  <body>
    <main>
      <header>
        <h1>Spec-Driven Research (Quantum) — <TOPIK></h1>
        <p class="muted">Versi: <TOPIK-SLUG>-v1.html</p>
      </header>

      <section class="grid">
        <div class="card">
          <h2>Ringkasan cepat</h2>
          <ul>
            <li>Masalah inti: ...</li>
            <li>Intuisi quantum: ...</li>
            <li>Output yang diukur: ...</li>
          </ul>
        </div>
      </section>

      <section>
        <h2>Problem statement</h2>
        <p>...</p>
      </section>

      <section>
        <h2>Dasar matematika/fisika (intuitif → notasi)</h2>
        <p>...</p>
        <p>Contoh notasi: <span class="math">|\psi\rangle = \alpha|0\rangle + \beta|1\rangle</span></p>
      </section>

      <section>
        <h2>Teori quantum computing</h2>
        <p>Qubit, superposition, entanglement, dan gate dasar.</p>
        <h3>Diagram konteks (Mermaid)</h3>
        <pre class="mermaid">flowchart LR
  P[Problem] --> C[Encode ke qubit]
  C --> U[Unitary / Gate sequence]
  U --> M[Measurement]
  M --> R[Result]
        </pre>
      </section>

      <section>
        <h2>Solusi klasik</h2>
        <p>...</p>
        <pre><code class="language-python"># IF/ELSE/ELIF/WHILE/FOR untuk alur utama
def classical_solve(data):
    return data
</code></pre>
      </section>

      <section>
        <h2>Solusi kuantum</h2>
        <h3>Circuit diagram (pilih SVG atau tabel)</h3>
        <div class="card">
          <p class="muted">Contoh sederhana (SVG placeholder). Ganti sesuai circuit topik.</p>
          <svg width="900" height="140" viewBox="0 0 900 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Quantum circuit">
            <rect x="0" y="0" width="900" height="140" fill="#fff" />
            <line x1="40" y1="40" x2="860" y2="40" stroke="#24292f" stroke-width="2" />
            <line x1="40" y1="100" x2="860" y2="100" stroke="#24292f" stroke-width="2" />
            <text x="10" y="45" font-family="monospace" font-size="14">q0</text>
            <text x="10" y="105" font-family="monospace" font-size="14">q1</text>
            <rect x="160" y="22" width="36" height="36" fill="#f6f8fa" stroke="#24292f" />
            <text x="178" y="45" text-anchor="middle" font-family="monospace" font-size="14">H</text>
            <circle cx="340" cy="40" r="6" fill="#24292f" />
            <line x1="340" y1="40" x2="340" y2="100" stroke="#24292f" stroke-width="2" />
            <circle cx="340" cy="100" r="12" fill="#fff" stroke="#24292f" stroke-width="2" />
            <line x1="328" y1="100" x2="352" y2="100" stroke="#24292f" stroke-width="2" />
            <line x1="340" y1="88" x2="340" y2="112" stroke="#24292f" stroke-width="2" />
          </svg>
        </div>

        <h3>Tracing sangat detail</h3>
        <p>Tracing menampilkan perubahan state (amplitudo) dan/atau probabilitas setelah gate penting.</p>
        <table>
          <thead>
            <tr>
              <th class="nowrap">Langkah</th>
              <th>Operasi / gate</th>
              <th>State ringkas</th>
              <th>Probabilitas ukur (contoh)</th>
              <th>Penjelasan</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>Inisialisasi</td>
              <td><span class="math">|00\rangle</span></td>
              <td>P(00)=1</td>
              <td>Mulai dari basis state.</td>
            </tr>
          </tbody>
        </table>

        <h3>Visualisasi probabilitas (bar sederhana)</h3>
        <div class="card">
          <div class="barRow">
            <div class="nowrap">00</div>
            <div class="barWrap"><div class="bar" style="width: 75%"></div></div>
            <div class="muted">0.75</div>
          </div>
          <div class="barRow">
            <div class="nowrap">01</div>
            <div class="barWrap"><div class="bar" style="width: 10%"></div></div>
            <div class="muted">0.10</div>
          </div>
        </div>
      </section>

      <section>
        <h2>Sumber</h2>
        <ul>
          <li><a href="https://...">...</a></li>
        </ul>
      </section>
    </main>

    <!-- Mermaid (opsional, tapi disarankan untuk memenuhi aturan visualisasi) -->
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
      mermaid.initialize({ startOnLoad: true });
    </script>

    <!-- KaTeX auto-render -->
    <script>
      window.addEventListener('DOMContentLoaded', () => {
        if (typeof renderMathInElement !== 'function') return;
        renderMathInElement(document.body, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
          ],
        });
      });
    </script>
  </body>
</html>
```
