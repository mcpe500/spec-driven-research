# CLASSICAL_PROMPT_RESEARCH_V1

## Tujuan

Mempublikasikan prompt template untuk riset bertopik **FFT (Fast Fourier Transform)** dengan fokus **solusi klasik** (software-oriented).

## Instruksi utama (wajib)

- Tugas hanya **mempublikasikan prompt**.
- **Jangan mengeksekusi prompt ini**: jangan melakukan riset FFT, jangan browsing, jangan menulis report FFT.
- Jangan membuat struktur folder atau file output apa pun. Dokumen ini hanya template instruksi.

---

# Prompt — Spec-Driven Research (FFT, Classical)

Gunakan metode **spec-driven research** untuk topik **FFT (Fast Fourier Transform)**.

## Struktur folder (sebagai spesifikasi target output)

Struktur ini adalah *kontrak penamaan* jika riset dijalankan nanti, bukan perintah untuk membuat folder sekarang:

- `spec/`
  - berisi spec sebelum research dimulai.
- `spec/handoff/`
  - berisi jawaban mentah + sumber yang ditemukan.
- `spec/results/fft/`
  - berisi laporan final FFT yang sudah rapi dan mudah dibaca.
  - wajib versioning per file: `fft-v1.md`, `fft-v2.md`, dst.

## Aturan output report

- Laporan harus naratif, to-the-point, dan mudah dicerna.
- Jangan ditulis seperti jawaban nomor 1/2/3.
- Jangan gunakan kata ganti orang hidup seperti `kita`, `aku`, `kamu`.
- Gunakan sumber online sebagai backup referensi.

## Fokus isi report (FFT)

1. Definisi masalah / problem statement FFT, termasuk contoh problem nyata.
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

## Gaya penjelasan

- Target pembaca adalah mahasiswa Informatika (software-oriented).
- Jangan terlalu banyak rumus.
- Jika ada rumus, jelaskan juga dalam kata-kata.
