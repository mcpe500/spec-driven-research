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

## Struktur (konsep) yang dituju

Gunakan struktur berikut sebagai acuan penamaan dan versioning (ini adalah *kontrak struktur*, bukan perintah untuk mengisi konten riset):

```text
spec/
  README.md
  handoff/
  results/
    <TOPIK-SLUG>/
      <TOPIK-SLUG>-v1.md
      <TOPIK-SLUG>-v2.md
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
  - wajib versioning per topik: `<TOPIK-SLUG>-vN.md`.

## Aturan versioning

- Versi baru selalu menjadi file baru:
  - `<TOPIK-SLUG>-v1.md`, `<TOPIK-SLUG>-v2.md`, `<TOPIK-SLUG>-v3.md`, dst.
- Versi lama tidak ditimpa.
- Buat `CHANGELOG.md` per topik untuk merangkum perubahan antiversi.

Contoh entri changelog:
- `v2: Perjelas 2.3; tambah tracing solusi klasik; rapikan alur 2→3→5`

## Gaya penulisan hasil report

- Bahasa Indonesia, to-the-point, mudah dibaca.
- Hindari kata ganti orang (contoh: `kita`, `aku`, `kamu`).
- Hindari format “jawaban nomor 1/2/3”.
- Tulis sebagai narasi yang mengalir; jika paragraf dibaca, jawaban inti sudah ter-cover.

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

## Catatan eksekusi

- Gunakan sumber online untuk backup referensi.
- Jika ada PDF internal, gunakan sebagai baseline lalu perkuat dengan sumber online.
- Lingkungan dapat memiliki `.venv`; gunakan jika perlu menjalankan tool lokal.
