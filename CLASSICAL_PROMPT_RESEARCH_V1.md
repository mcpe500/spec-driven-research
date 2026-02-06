# CLASSICAL_PROMPT_RESEARCH_V1

## Tujuan

Mempublikasikan prompt template untuk riset bertopik **<TOPIK>** dengan fokus **solusi klasik** (software-oriented).

## Instruksi utama (wajib)

- Tugas hanya **mempublikasikan prompt**.
- **Jangan mengeksekusi prompt ini**: jangan melakukan riset topik, jangan browsing, jangan menulis report topik.
- Jangan membuat struktur folder atau file output apa pun. Dokumen ini hanya template instruksi.

---

# Prompt — Spec-Driven Research (Classical)

Gunakan metode **spec-driven research** untuk topik **<TOPIK>**.

## Struktur folder (sebagai spesifikasi target output)

Struktur ini adalah *kontrak penamaan* jika riset dijalankan nanti, bukan perintah untuk membuat folder sekarang:

- `spec/`
  - berisi spec sebelum research dimulai.
- `spec/handoff/`
  - berisi jawaban mentah + sumber yang ditemukan.
- `spec/results/fft/`
  - berisi laporan final topik yang sudah rapi dan mudah dibaca.
  - wajib versioning per file: `<TOPIK-SLUG>-v1.md`, `<TOPIK-SLUG>-v2.md`, dst.

Catatan: `fft` di contoh path bisa diganti menjadi `<TOPIK-SLUG>`.

## Aturan output report

- Laporan harus naratif, to-the-point, dan mudah dicerna.
- Jangan ditulis seperti jawaban nomor 1/2/3.
- Jangan gunakan kata ganti orang hidup seperti `kita`, `aku`, `kamu`.
- Gunakan sumber online sebagai backup referensi.

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

## Gaya penjelasan

- Target pembaca adalah mahasiswa Informatika (software-oriented).
- Jangan terlalu banyak rumus.
- Jika ada rumus, jelaskan juga dalam kata-kata.
