# Pertemuan 03 Seleksi Python

Nama: Intan Anugra Salsabila
NIM: 2225250154
Kelas: 3F

## Tujuan

Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code menggunakan perintah:

python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
python tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas

Program analisis persamaan kuadrat digunakan untuk menentukan jenis persamaan dan kemungkinan akar berdasarkan persamaan:

ax² + bx + c = 0

Langkah-langkah algoritmanya adalah:

1. Memasukkan nilai koefisien a, b, dan c.
2. Memeriksa nilai koefisien a.
3. Jika a = 0, maka persamaan bukan persamaan kuadrat.
4. Jika a tidak sama dengan 0, menghitung diskriminan dengan rumus b² - 4ac.
5. Jika diskriminan > 0, maka persamaan memiliki dua akar real berbeda.
6. Jika diskriminan = 0, maka persamaan memiliki satu akar real kembar.
7. Jika diskriminan < 0, maka persamaan tidak memiliki akar real.

## Hasil Pengujian

### Latihan 1 — Genap dan Ganjil

| Input | Hasil |
|---|---|
| 8 | 8 adalah bilangan genap. |
| 13 | 13 adalah bilangan ganjil. |
| 0 | 0 adalah bilangan genap. |
| -7 | -7 adalah bilangan ganjil. |

### Latihan 2 — Membandingkan Dua Bilangan

| Input | Hasil |
|---|---|
| 7 dan 4 | 7 lebih besar dari 4. |
| 2 dan 9 | 2 lebih kecil dari 9. |
| 5 dan 5 | 5 sama dengan 5. |
| -3 dan -8 | -3 lebih besar dari -8. |

### Latihan 3 — Kelulusan Bersyarat

| Nilai | Kehadiran | Hasil |
|---:|---:|---|
| 75 | 90% | Lulus. |
| 59 | 90% | Tidak lulus. |
| 75 | 79% | Tidak lulus. |
| 60 | 80% | Lulus. |

### Latihan 4 — Jenis Segitiga

| Sisi | Hasil |
|---|---|
| 3, 3, 3 | Segitiga sama sisi. |
| 5, 5, 8 | Segitiga sama kaki. |
| 3, 4, 5 | Segitiga sembarang. |
| 1, 2, 3 | Bukan segitiga. |

### Tugas — Analisis Persamaan Kuadrat

| a | b | c | Diskriminan | Hasil |
|---:|---:|---:|---:|---|
| 1 | -5 | 6 | 1.00 | Memiliki dua akar real berbeda. |
| 1 | 2 | 1 | 0.00 | Memiliki satu akar real kembar. |
| 1 | 2 | 5 | -16.00 | Tidak memiliki akar real. |
| 0 | 2 | 1 | - | Bukan persamaan kuadrat. |

## Refleksi

Dalam membuat program seleksi, kesalahan logika dapat terjadi ketika kondisi yang digunakan tidak sesuai dengan aturan yang diberikan. Pada analisis persamaan kuadrat, kondisi diskriminan harus dibedakan menjadi tiga kemungkinan, yaitu diskriminan > 0, diskriminan = 0, dan diskriminan < 0.

Dengan menggunakan kondisi tersebut secara tepat, program dapat memberikan hasil yang sesuai untuk setiap kemungkinan persamaan kuadrat. Pengujian dengan beberapa nilai juga membantu memastikan bahwa program dapat menangani kondisi yang berbeda, termasuk nilai pada batas tertentu.
