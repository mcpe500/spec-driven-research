# CLASSICAL_PROMPT_RESEARCH_V2

## Tujuan

Mempublikasikan prompt template untuk riset bertopik **<TOPIK>** dengan fokus **solusi klasik** (software-oriented).

## Instruksi utama (wajib)

- Tugas anda adalah **mengeksekusi prompt**.
- **PAHAMI mengeksekusi prompt ini**.
- jika belum ada struktur maka buatlah struktur folder atau file output apa pun. Dokumen ini hanya template instruksi.

---

# Prompt — Spec-Driven Research (Classical)

Gunakan metode **spec-driven research** untuk topik **<TOPIK>**.

Fokus utama versi ini: hasil akhir berupa **dokumen HTML** yang rapi, mudah dibaca, dan kaya visualisasi (diagram + tabel) untuk membantu pemahaman.

## Struktur folder (sebagai spesifikasi target output)

Struktur ini adalah *kontrak penamaan* jika riset dijalankan nanti, bukan perintah untuk membuat folder sekarang:

- `spec/`
  - berisi spec sebelum research dimulai.
- `spec/handoff/`
  - berisi jawaban mentah + sumber yang ditemukan.
- `spec/results/fft/`
  - berisi laporan final topik yang sudah rapi dan mudah dibaca.
  - wajib versioning per file: `<TOPIK-SLUG>-v1.html`, `<TOPIK-SLUG>-v2.html`, dst.
  - (opsional) subfolder aset jika dibutuhkan:
    - `assets/` (gambar yang dihasilkan, file data kecil untuk chart, dll.)

Catatan: `fft` di contoh path bisa diganti menjadi `<TOPIK-SLUG>`.

## Format output (WAJIB: HTML, bukan Markdown)

- Output final yang diberikan adalah **HTML utuh** (bukan Markdown).
- Minimal gunakan struktur HTML yang valid: `<!doctype html>`, `<html>`, `<head>`, `<body>`.
- Gunakan **CSS internal** via `<style>` (agar file bisa dibuka offline).
- Jika memakai library visualisasi (contoh Mermaid), boleh pakai CDN *atau* jelaskan fallback.
- Kode program ditulis dalam `<pre><code>`.

## Aturan visualisasi (WAJIB)

Laporan harus punya visualisasi yang membantu pembaca memahami alur, bukan sekadar dekorasi.

Wajib ada minimal:

- 1 diagram alur algoritma (flowchart) dalam bentuk **Mermaid** (mis. `flowchart TD`).
- 1 tabel tracing yang memperlihatkan perubahan nilai per langkah (mis. kolom: langkah, i, j, state, output).
- 1 visualisasi konteks masalah dunia nyata (mis. diagram komponen sederhana, data flow, atau sequence singkat). Mermaid juga boleh.

Tambahan (opsional, jika relevan):

- Grafik sederhana (bar/line) jika ada metrik (mis. perbandingan waktu proses untuk input kecil).
- Blok “Ringkasan cepat” berupa daftar poin singkat di awal.

## Aturan output report

- Laporan harus naratif, to-the-point, dan mudah dicerna.
- Jangan ditulis seperti jawaban nomor 1/2/3.
- Jangan gunakan kata ganti orang hidup seperti `kita`, `aku`, `kamu`.
- Gunakan sumber online sebagai backup referensi.
- Jangan menuliskan output akhir dalam format Markdown.

## Fokus isi report (<TOPIK>)

1. Definisi masalah / problem statement <TOPIK>, termasuk contoh problem nyata.
2. Solusi klasik:
   - jelaskan algoritma dengan bahasa sederhana,
  - sertakan kode yang mudah dibaca,
   - gunakan hanya kontrol alur dasar: `IF`, `ELSE`, `ELIF`, `WHILE`, `FOR`.
3. Tracing detail:
   - tracing per baris penting atau per loop,
   - tunjukkan alur perubahan nilai agar mudah diikuti.
4. Contoh implementasi dan real case:
   - berikan minimal satu contoh implementasi,
   - berikan minimal satu contoh kasus nyata,
   - sertakan tracing langkah demi langkah.

Catatan untuk implementasi kode:

- Pilih satu bahasa yang umum untuk mahasiswa (disarankan: Python atau C).
- Hindari sintaks tingkat lanjut yang menyamarkan alur (mis. list comprehension kompleks, recursion yang tidak perlu, metaprogramming).

## Gaya penjelasan

- Target pembaca adalah mahasiswa Informatika (software-oriented).
- Jangan terlalu banyak rumus.
- Jika ada rumus, jelaskan juga dalam kata-kata.

## Kerangka HTML (template WAJIB diikuti)

Gunakan kerangka berikut sebagai baseline. Isi konten sesuai topik `<TOPIK>` dan pastikan semua visualisasi muncul.

```html
<!doctype html>
<html lang="id">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Spec-Driven Research (Classical) — <TOPIK></title>
    <style>
      :root { color-scheme: light; }
      body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.55; margin: 24px; }
      main { max-width: 980px; margin: 0 auto; }
      h1, h2, h3 { line-height: 1.2; }
      code, pre { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
      pre { padding: 12px; overflow: auto; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 8px; }
      table { border-collapse: collapse; width: 100%; }
      th, td { border: 1px solid #d0d7de; padding: 8px; vertical-align: top; }
      th { background: #f6f8fa; text-align: left; }
      .muted { color: #57606a; }
      .callout { padding: 12px; border: 1px solid #d0d7de; border-radius: 8px; background: #ffffff; }
    </style>
  </head>
  <body>
    <main>
      <header>
        <h1>Spec-Driven Research (Classical) — <TOPIK></h1>
        <p class="muted">Versi: <TOPIK-SLUG>-v1.html</p>
      </header>

      <section>
        <h2>Ringkasan cepat</h2>
        <ul>
          <li>Masalah inti: ...</li>
          <li>Intuisi solusi klasik: ...</li>
          <li>Kompleksitas (perkiraan): ...</li>
        </ul>
      </section>

      <section>
        <h2>Problem statement</h2>
        <p>...</p>
        <div class="callout">
          <strong>Contoh problem nyata</strong>
          <p>...</p>
        </div>
      </section>

      <section>
        <h2>Solusi klasik</h2>
        <h3>Intuisi</h3>
        <p>...</p>

        <h3>Diagram alur (Mermaid)</h3>
        <pre class="mermaid">flowchart TD
  A[Mulai] --> B[Input data]
  B --> C{Kondisi}
  C -->|Ya| D[Langkah]
  C -->|Tidak| E[Selesai]
        </pre>

        <h3>Kode</h3>
        <pre><code class="language-python"># contoh (ganti sesuai topik)
def solve(data):
    # IF/ELSE/ELIF/WHILE/FOR saja untuk alur utama
    return data
</code></pre>
      </section>

      <section>
        <h2>Tracing detail</h2>
        <p>Tracing menjelaskan perubahan nilai pada langkah penting.</p>
        <table>
          <thead>
            <tr>
              <th>Langkah</th>
              <th>State / variabel kunci</th>
              <th>Penjelasan singkat</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>...</td>
              <td>...</td>
            </tr>
          </tbody>
        </table>
      </section>

      <section>
        <h2>Real case</h2>
        <p>...</p>
        <h3>Visualisasi konteks</h3>
        <pre class="mermaid">flowchart LR
  U[User] --> S[Sistem]
  S --> D[(Data)]
        </pre>
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
  </body>
</html>
```
