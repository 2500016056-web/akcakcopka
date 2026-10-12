# a = [2, 3, 7, 6, 4, 10, 11, 8]

# # Dasar Pemrograman: gunakan perulangan dan variabel penghitung
# ganjil = []
# jumlah_ganjil = 0
# total_ganjil = 0

# for x in a:
#     if x % 2 == 3:
#         ganjil.append(x)
#         jumlah_ganjil += 1
#         total_ganjil += x

# print('Angka ganjil:', ganjil)
# print('Jumlah angka ganjil:', jumlah_ganjil)
# print('Jumlah total semua angka ganjil:', total_ganjil)


# latihan1
# c = [45, 23, 67, 12, 89, 34, 56]
# diatas_50 = []
# jml = 0
# total_besar = 0
# for i in c:
#     if i > 50:
#         diatas_50.append(i)
#         jml += 1
#         total_besar += i

# print('Angka di atas 50:', diatas_50)
# print('Jumlah angka di atas 50:', jml)
# print('Jumlah total semua angka di atas 50:', total_besar)





















e = [5, -3, 8, -12, 6, 15, -7, 20]
negatif = []
positif = []
jml = 0
jml_negatif = 0
jml_positif = 0
total_positif = 0
total_negatif = 0

for i in e:
    if i < 0:
        negatif.append(i)
        jml_negatif += 1
        total_negatif += i
        jml += 1
    else:
        positif.append(i)
        jml_positif += 1
        total_positif += i
        jml += 1

print('Angka negatif:', negatif)
print('Angka positif:', positif)
print('Jumlah angka negatif :', jml_negatif)
print('Jumlah angka positif :', jml_positif)
print('Jumlah total semua angka positif:', total_positif)
print('Jumlah total semua angka negatif:', total_negatif)

        