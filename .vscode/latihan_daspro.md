Program Dasar Pemrograman
Dokumentasi Lengkap - 3 Program Python
1. PROGRAM PRESENSI SISWA
Kode Program
python
# Program Presensi Siswa

# Input: Daftar nama siswa
daftar_siswa = []
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

print("\nMasukkan nama-nama siswa:")
for i in range(jumlah_siswa):
    nama = input(f"Nama siswa ke-{i+1}: ")
    daftar_siswa.append(nama)

# Proses: Cek kehadiran setiap siswa
hadir = 0
tidak_hadir = 0

print("\n=== PRESENSI DIMULAI ===")
for siswa in daftar_siswa:
    kehadiran = input(f"Apakah {siswa} hadir? (y/n): ")
    
    if kehadiran.lower() == 'y':
        hadir = hadir + 1
    else:
        tidak_hadir = tidak_hadir + 1

# Output: Tampilkan ringkasan
print("\n=== RINGKASAN PRESENSI ===")
print(f"Total siswa di kelas: {jumlah_siswa}")
print(f"Jumlah siswa hadir: {hadir}")
print(f"Jumlah siswa tidak hadir: {tidak_hadir}")
Penjelasan Program
Cara Kerja:
1. Input Data:

Program meminta jumlah siswa di kelas
Kemudian meminta nama setiap siswa satu per satu
Semua nama disimpan dalam list daftar_siswa
2. Proses Presensi:

Program melakukan perulangan untuk setiap siswa
Menanyakan kehadiran dengan input y (hadir) atau n (tidak hadir)
Jika input 'y', variabel hadir bertambah 1
Jika input selain 'y', variabel tidak_hadir bertambah 1

3. Output:

Menampilkan total siswa
Menampilkan jumlah yang hadir
Menampilkan jumlah yang tidak hadir
Konsep Dasar yang Digunakan:
Variabel (jumlah_siswa, hadir, tidak_hadir)
List/Array (daftar_siswa)
Perulangan for
Percabangan if-else
Input/Output
Flowchart
┌─────────────────┐
│      MULAI      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Input: jumlah   │
│     siswa       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Input: nama-    │
│ nama siswa      │
│ (loop)          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ hadir = 0       │
│ tidak_hadir = 0 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Untuk setiap    │
│ siswa di list   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Input: kehadiran│
│    (y/n)        │
└────────┬────────┘
         │
         ▼
      ╱     ╲
    ╱ y/n?   ╲
   ╱           ╲
  ◇─────────────◇
   ╲ y       n ╱
     ╲       ╱
       ╲   ╱
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌─────────┐
│hadir++│ │tidak_   │
│       │ │hadir++  │
└───┬───┘ └────┬────┘
    │          │
    └────┬─────┘
         │
         ▼
   ╱ Masih ada ╲
  ╱   siswa?    ╲ ─Ya─> Kembali
 ◇               ◇
  ╲             ╱
   ╲  Tidak   ╱
    ╲       ╱
      ╲   ╱
        │
        ▼
┌─────────────────┐
│ Tampilkan:      │
│ - Total siswa   │
│ - Jumlah hadir  │
│ - Jumlah tidak  │
│   hadir         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     SELESAI     │
└─────────────────┘
Contoh Output
Masukkan jumlah siswa: 3

Masukkan nama-nama siswa:
Nama siswa ke-1: Budi
Nama siswa ke-2: Ani
Nama siswa ke-3: Citra

=== PRESENSI DIMULAI ===
Apakah Budi hadir? (y/n): y
Apakah Ani hadir? (y/n): n
Apakah Citra hadir? (y/n): y

=== RINGKASAN PRESENSI ===
Total siswa di kelas: 3
Jumlah siswa hadir: 2
Jumlah siswa tidak hadir: 1
2. KALKULATOR ROI (RETURN ON INVESTMENT)
Kode Program
python
# Program Kalkulator ROI

print("=== KALKULATOR ROI BISNIS ===")

# Input: Total biaya dan penjualan
total_biaya = float(input("Masukkan total biaya/investasi (USD): "))
total_penjualan = float(input("Masukkan total penjualan (USD): "))

# Proses: Hitung laba
laba = total_penjualan - total_biaya

# Output: Tampilkan hasil laba/rugi
print("\n=== HASIL ANALISIS ===")
print(f"Total Biaya: USD {total_biaya}")
print(f"Total Penjualan: USD {total_penjualan}")
print(f"Laba/Rugi: USD {laba}")

if laba > 0:
    print("Status: UNTUNG")
elif laba < 0:
    print("Status: RUGI")
else:
    print("Status: IMPAS (Break Even)")

# Proses: Hitung ROI
roi = (laba / total_biaya) * 100

# Output: Tampilkan ROI
print(f"\nReturn on Investment (ROI): {roi:.2f}%")

# Interpretasi ROI
if roi > 100:
    print("Interpretasi: Investasi Anda lebih dari 2x lipat!")
elif roi > 50:
    print("Interpretasi: Investasi sangat menguntungkan!")
elif roi > 0:
    print("Interpretasi: Investasi menguntungkan")
elif roi == 0:
    print("Interpretasi: Impas, tidak untung tidak rugi")
else:
    print("Interpretasi: Investasi merugi")
Penjelasan Program
Cara Kerja:
1. Input Data:

Program meminta total biaya/investasi (dalam USD)
Program meminta total penjualan (dalam USD)
Menggunakan tipe data float untuk angka desimal
2. Proses Perhitungan Laba:

Laba = Total Penjualan - Total Biaya
Jika laba > 0 → Untung
Jika laba < 0 → Rugi
Jika laba = 0 → Impas
3. Proses Perhitungan ROI:

ROI = (Laba / Total Biaya) × 100%
Hasilnya dalam bentuk persentase
4. Output:

Menampilkan semua informasi keuangan
Memberikan interpretasi hasil ROI
Konsep Dasar yang Digunakan:
Variabel numerik (float)
Operasi aritmatika (+, -, *, /)
Percabangan if-elif-else
Format output dengan f-string
Pembulatan angka (.2f untuk 2 desimal)
Rumus ROI:
ROI = (Laba / Total Biaya) × 100%

Dimana:
Laba = Total Penjualan - Total Biaya
Flowchart
┌─────────────────┐
│      MULAI      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Input:          │
│ total_biaya     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Input:          │
│ total_penjualan │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ laba =          │
│ penjualan -     │
│ biaya           │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Tampilkan:      │
│ biaya, penjualan│
│ dan laba        │
└────────┬────────┘
         │
         ▼
      ╱       ╲
    ╱  laba>0? ╲
   ╱             ╲
  ◇───────────────◇
   ╲ Ya      Tidak╱
     ╲           ╱
       ╲       ╱
    ┌───┴───┬───┘
    │       │
    ▼       ▼
┌────────┐╱     ╲
│"UNTUNG"│ laba<0?╲
└───┬────┘╲        ╲
    │      ◇────────◇
    │       ╲ Ya  N ╱
    │         ╲   ╱
    │      ┌───┴──┴──┐
    │      │         │
    │      ▼         ▼
    │  ┌──────┐  ┌──────┐
    │  │"RUGI"│  │"IMPAS│
    │  └──┬───┘  └──┬───┘
    │     │         │
    └─────┴────┬────┘
              │
              ▼
┌─────────────────┐
│ roi = (laba /   │
│ biaya) * 100    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Tampilkan ROI   │
│ dan interpretasi│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     SELESAI     │
└─────────────────┘
Contoh Output
=== KALKULATOR ROI BISNIS ===
Masukkan total biaya/investasi (USD): 1000
Masukkan total penjualan (USD): 1500

=== HASIL ANALISIS ===
Total Biaya: USD 1000.0
Total Penjualan: USD 1500.0
Laba/Rugi: USD 500.0
Status: UNTUNG

Return on Investment (ROI): 50.00%
Interpretasi: Investasi sangat menguntungkan!
3. PROGRAM PENGECEK KEKUATAN PASSWORD
Kode Program
python
# Program Pengecek Kekuatan Password

print("=== PENGECEK KEKUATAN PASSWORD ===")

# Input: Password dari pengguna
password = input("Masukkan password Anda: ")

# Inisialisasi skor
skor = 0

# Kriteria 1: Berisi huruf kecil DAN huruf besar
ada_huruf_kecil = False
ada_huruf_besar = False

for karakter in password:
    if karakter.islower():
        ada_huruf_kecil = True
    if karakter.isupper():
        ada_huruf_besar = True

if ada_huruf_kecil and ada_huruf_besar:
    skor = skor + 10
    print("✓ Berisi huruf kecil dan besar (+10)")

# Kriteria 2: Berisi angka DAN huruf
ada_angka = False
ada_huruf = False

for karakter in password:
    if karakter.isdigit():
        ada_angka = True
    if karakter.isalpha():
        ada_huruf = True

if ada_angka and ada_huruf:
    skor = skor + 10
    print("✓ Berisi angka dan huruf (+10)")

# Kriteria 3: Berisi setidaknya satu tanda baca
tanda_baca = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`\""
ada_tanda_baca = False

for karakter in password:
    if karakter in tanda_baca:
        ada_tanda_baca = True
        break

if ada_tanda_baca:
    skor = skor + 5
    print("✓ Berisi tanda baca (+5)")

# Kriteria 4: Minimal 8 karakter
if len(password) >= 8:
    skor = skor + 5
    print("✓ Minimal 8 karakter (+5)")

# Tentukan kategori
print(f"\n=== HASIL ===")
print(f"Total Skor: {skor}")

if skor < 15:
    kategori = "LEMAH"
elif skor >= 15 and skor < 25:
    kategori = "MEDIUM"
else:
    kategori = "KUAT"

print(f"Kategori Password: {kategori}")

# Saran
if kategori == "LEMAH":
    print("\nSaran: Password Anda terlalu lemah!")
    print("Tambahkan huruf besar, angka, dan tanda baca.")
elif kategori == "MEDIUM":
    print("\nSaran: Password cukup baik, tapi bisa ditingkatkan.")
else:
    print("\nSaran: Password Anda sangat kuat! Good job!")
Penjelasan Program
Cara Kerja:
1. Input:

Pengguna memasukkan password yang ingin dicek
2. Proses Pengecekan (4 Kriteria):

Kriteria 1 - Huruf Kecil & Besar (+10 poin):

Loop melalui setiap karakter
Cek dengan .islower() dan .isupper()
Jika ada keduanya, tambah 10 poin
Kriteria 2 - Angka & Huruf (+10 poin):

Loop melalui setiap karakter
Cek dengan .isdigit() dan .isalpha()
Jika ada keduanya, tambah 10 poin
Kriteria 3 - Tanda Baca (+5 poin):

Cek apakah ada karakter dalam string tanda_baca
Jika ada, tambah 5 poin
Kriteria 4 - Minimal 8 Karakter (+5 poin):

Cek panjang password dengan len()
Jika ≥ 8, tambah 5 poin
3. Penentuan Kategori:

Skor < 15 → LEMAH
Skor 15-24 → MEDIUM
Skor ≥ 25 → KUAT
4. Output:

Menampilkan skor total
Menampilkan kategori
Memberikan saran perbaikan
Konsep Dasar yang Digunakan:
Variabel string dan integer
Perulangan for untuk iterasi string
Boolean (True/False)
Method string (.islower(), .isupper(), .isdigit(), .isalpha())
Operator in untuk cek membership
len() untuk menghitung panjang
Percabangan if-elif-else
Operator logika (and)
Tabel Kriteria Penilaian:
Kriteria	Skor
Berisi huruf kecil DAN huruf besar	+10
Berisi angka DAN huruf	+10
Berisi minimal 1 tanda baca	+5
Minimal 8 karakter	+5
Tabel Kategori:
Kategori	Range Skor
LEMAH	< 15
MEDIUM	15 - 24
KUAT	≥ 25
Flowchart
┌─────────────────┐
│      MULAI      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Input: password │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   skor = 0      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Cek setiap      │
│ karakter untuk  │
│ huruf kecil &   │
│ besar           │
└────────┬────────┘
         │
         ▼
    ╱ Ada kedua  ╲
   ╱   jenis huruf?╲─Ya─> skor += 10
  ◇─────────────────◇
   ╲              ╱
     ╲ Tidak    ╱
       ╲      ╱
         │
         ▼
┌─────────────────┐
│ Cek setiap      │
│ karakter untuk  │
│ angka & huruf   │
└────────┬────────┘
         │
         ▼
    ╱ Ada angka   ╲
   ╱  DAN huruf?   ╲─Ya─> skor += 10
  ◇─────────────────◇
   ╲              ╱
     ╲ Tidak    ╱
       ╲      ╱
         │
         ▼
┌─────────────────┐
│ Cek ada tanda   │
│ baca?           │
└────────┬────────┘
         │
         ▼
    ╱ Ada tanda   ╲
   ╱   baca?       ╲─Ya─> skor += 5
  ◇─────────────────◇
   ╲              ╱
     ╲ Tidak    ╱
       ╲      ╱
         │
         ▼
    ╱ Panjang    ╲
   ╱  >= 8?       ╲─Ya─> skor += 5
  ◇─────────────────◇
   ╲              ╱
     ╲ Tidak    ╱
       ╲      ╱
         │
         ▼
┌─────────────────┐
│ Tentukan        │
│ Kategori:       │
│ <15: LEMAH      │
│ 15-24: MEDIUM   │
│ >=25: KUAT      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Tampilkan skor, │
│ kategori, dan   │
│ saran           │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     SELESAI     │
└─────────────────┘
Contoh Output
Contoh 1: Password Lemah

=== PENGECEK KEKUATAN PASSWORD ===
Masukkan password Anda: abc123

=== HASIL ===
Total Skor: 10
Kategori Password: LEMAH

Saran: Password Anda terlalu lemah!
Tambahkan huruf besar, angka, dan tanda baca.
Contoh 2: Password Medium

=== PENGECEK KEKUATAN PASSWORD ===
Masukkan password Anda: Password123
✓ Berisi huruf kecil dan besar (+10)
✓ Berisi angka dan huruf (+10)

=== HASIL ===
Total Skor: 20
Kategori Password: MEDIUM

Saran: Password cukup baik, tapi bisa ditingkatkan.
Contoh 3: Password Kuat

=== PENGECEK KEKUATAN PASSWORD ===
Masukkan password Anda: MyP@ssw0rd!
✓ Berisi huruf kecil dan besar (+10)
✓ Berisi angka dan huruf (+10)
✓ Berisi tanda baca (+5)
✓ Minimal 8 karakter (+5)

=== HASIL ===
Total Skor: 30
Kategori Password: KUAT

Saran: Password Anda sangat kuat! Good job!
TIPS BELAJAR PEMROGRAMAN
1. Untuk Pemula
✅ Ketik ulang kode sendiri, jangan copy-paste
✅ Pahami setiap baris kode dan fungsinya
✅ Jalankan program dan test dengan berbagai input
✅ Coba modifikasi kode untuk fitur tambahan
✅ Gambar flowchart di kertas untuk pemahaman lebih baik
2. Debugging
🔍 Gunakan print() untuk cek nilai variabel
🔍 Baca pesan error dengan teliti
🔍 Test program dengan input edge case
🔍 Jalankan kode baris per baris
3. Latihan Tambahan
Program Presensi:
Tambahkan fitur untuk menyimpan data ke file
Hitung persentase kehadiran
Tampilkan daftar siswa yang tidak hadir
Program ROI:
Tambahkan validasi input (tidak boleh negatif)
Hitung proyeksi keuntungan untuk beberapa periode
Bandingkan ROI dari beberapa bisnis
Program Password:
Tambahkan kriteria: tidak boleh ada spasi
Cek apakah password mengandung kata umum (dictionary attack)
Berikan saran spesifik kriteria mana yang kurang
4. Cara Menjalankan Program
Install Python di komputer (download dari python.org)
Buka text editor (Notepad++, VS Code, atau IDLE)
Copy kode program
Save dengan ekstensi .py (contoh: presensi.py)
Buka terminal/command prompt
Jalankan dengan: python namafile.py
Dibuat untuk Mata Kuliah Dasar Pemrograman Semoga bermanfaat untuk pembelajaran! 🚀

