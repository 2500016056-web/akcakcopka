
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

print("Masukkan nama-nama siswa:")
daftar_siswa = [input(f"Nama siswa ke-{i+1}: ") 
for i in range(jumlah_siswa)]

hadir = 0
tidak_hadir = 0

print("=== PRESENSI DIMULAI ===")
for siswa in daftar_siswa:
    kehadiran = input(f"Apakah {siswa} hadir? (y/n): ")
    
    if kehadiran == 'y' or kehadiran == 'Y':
        hadir += 1
    else:
        tidak_hadir += 1

print("=== RINGKASAN PRESENSI ===")
print(f"Total siswa di kelas: {jumlah_siswa}")
print(f"Jumlah siswa hadir: {hadir}")
print(f"Jumlah siswa tidak hadir: {tidak_hadir}")
