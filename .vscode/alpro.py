# for i in range (3):
#     for j in range(3):
#         if j % 2 == 0:
#             print(i,j)

# for i in range (1,5):
#     for j in range(1,i +1):
#        print(j, end=" ")
#     print()

# for i in range (5):
#     for j in range (5):
#         if j+1 <= i:
#             print(j+1, end=" ")
#     print()

# for i in range (1,6):
#     if i % 2 == 0:
#         print(i, "= Genap")
#     else:
#         print(i, "= Ganjil")

# for i in range (1,6):
#     for j in range (1,6):
#         hasil = i * j
#         if hasil % 2 == 0:
#             print(hasil,end="\t")
#         else:
#             print("x", end="\t")
#     print()


# for i in range (5):
#     if i == 2:
#         continue
#     print(i)

# for i in range (5):
#     if i == 3:
#         break
#     print(i)


# for i in range (1,21):
#     if i % 2 != 0:
#         print(i, end=" ")

# for i in range (1,21):
#     if i % 2 == 0:
#         print(i, end=" ")

# for i in range (1,6):
#     for j in range(1,6):
#         hasil = i * j
#         if hasil % 2 == 0:
#             print(hasil,end="\t")
#         else:
#             print("x", end="\t")


# for i in range (2):
#     for j in range (2):
#         if  i == j:
#             continue
#         print(i,j, end=" ")
#     print()


# for  i in range (3):
#     for j in range (3):
#         if (i==j):
#             continue
#         for k in range (3):
#             if (i==k) or (j==k):
#                 continue
#             print(i,j,k, end=" ")
#     print()


# for i in range(5):
#     for j in range(i,5):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         print("*", end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(2 * (n - i) - 1):
#         print("*", end="")
#     print()

# PRAKTIKUM ALPRO 2

# def persegi5 (N):

#     for i in range(N):
#         for j in range(N):
#             print("*", end=" ")
#         print()

# def segitiga(N):

#     for i in range(N):
#         for j in range(i+1):
#             print("*", end=" ")
#         print()

# def  garis(kar,N):
#     for j in range(N):
#         print(kar, end=" ")

# garis('=', 10)
# print()
# persegi5(6)
# print()
# segitiga(5)


# def perkalian():

# def segitiga(N):
#     for i in range(N):
#         for j in range(i+1):
#             print("*", end=" ")
#         print()


# def garis7( gar,N):
#     for i in range(N):
#         print(gar, end=" ")

# def segitiga7(kar1, kar2, N):
#     for i in range(N):
#             garis7(kar1, N-i-1)
#             garis7(kar2, 2*i+1)
#             print()

# segitiga7(" ", "#", 6)


# def jumlah(N):
#     jumlah = 0
#     s = 'Jumlah '
#     for i in range(1, N):
#         jumlah += i
#         s += str(i) + ' + '
#     jumlah += N
#     s += str(N)
#     s += ' = ' + str(jumlah)
#     return s
# EN = int(input('Masukkan nilai N: '))
# hasil = jumlah(EN)
# print(hasil)


# def kali(N):
# jumlah = 1
# s = 'Hasil '
# for i in range(1, N):
#     jumlah *= i
#     s += str(i) + ' *'
# jumlah *= N
# s += str(N)
# s += ' = ' + str(jumlah)
# return s
# EN = int(input('Masukkan nilai N: '))
# hasil = kali(EN)
# print(hasil)
# def apa(N):
#     jumlah = 0
#     s = 'Jumlah '
#     for i in range(1, N):
#         k = 2*i-1
#         jumlah += k
#         s += str(k) + ' + '
#     jumlah *= 2*N-1
#     s += str(2*N-1)
#     s += ' = ' + str(jumlah)
#     return s
# EN = int(input('Masukkan nilai N: '))
# hasil = apa(EN)
# print(hasil)


# Buatkan segitiga terbalik
# def garis (kar,N):
#     s = ""
#     for i in range(N):
#         s += kar + " "
#     return s

# def segitiga(N):
#     s = ""
#     for i in range(1,N+1):
#         s += garis(" ",i-1) + garis (str(i),2*N-2*i+1) + "\n"

#     return s
# print(segitiga(6))

# Buatkan segit
# def garis (kar,N):
#     s = ""
#     for i in range(N):
#         s += kar + " "
#     return s

# def segitiga(kar,N,M):
#     s = ""
#     for i in range(1,N+1):
#         for k in range (M):
#             s += garis(" ",i-1) + garis (str(i),2*N-2*i+1) + "\n"
#             s += garis(" ",N) + garis (kar,M) + "\n"

#     return s
# print(segitiga("*",6,3))


# PRAKTIKUM ALPRO 3
# def tulis (s,n):
#     if n == 0:
#         return
#     print(s[n-1],end ="")
#     tulis(s,n - 1)
# Nama = input("Masukkan namamu: ")
# p = len(Nama)
# tulis(Nama,p)

# def tulis(s,n):
#     if n == 0:
#         print()
#         return
#     print(s[n-1],end ="")
#     tulis(s,n - 1)
# def ayo(s,n):
#     if n == 0:
#         return
#     tulis(s,n-1)
#     ayo(s,n-1)
# Nama = input("Masukkan namamu: ")
# p = len(Nama)
# ayo(Nama,p)


# def tulis(s,n):
#     if n == 0:
#         return "\n"
#     return tulis(s,n-1) + s[n-1]
# def ayo(s,n):
#     if n == 0:
#         return ""
#     return ayo(s,n-1) + tulis(s,n-1)
# Nama = input("Masukkan namamu: ")
# p = len(Nama)
# hasil = ayo(Nama,p)
# print(hasil)

# def faktorial(N):
#     if N <= 1:
#         return 1
#     else:
#         return N * faktorial(N-1)
# def tulis(n):
#     if n == 1:
#         return "1 = "
#     return str(n) + "*" + tulis(n-1)
# bil = int(input('Masukkan bilangan bulat N: '))
# print(tulis(bil) + str(faktorial(bil)))

# Rekursive case
# def hitung_mundur (n):
#     if n == 0:
#         return
#     print(n)
#     hitung_mundur(n - 1)
# hitung_mundur(5)

# def hitung_mundur (n):
#     if n == 0:
#         return
#     hitung_mundur(n - 1)
#     print(n)
# hitung_mundur(3)

# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n-1)
# print(faktorial(5))

# def akalib(a,b):
#     if a == 0:
#         return 0
#     else:
#         return b + akalib(a-1,b)
# print(akalib(5,4))

# def apangkatb(a,b):
#     if b == 0:
#         return 1
#     else:
#         return a * apangkatb(a,b-1)
# print(apangkatb(2,8))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))

# def jumlah (n):
#     if n == 0:
#         return 0
#     return n + jumlah(n-1)
# print(jumlah(5))


# import random
# def bacadata (M):
#     dtlarik = []
#     for i in range(M):
#         br = random.randint(1, 20)
#         print(br, end= " ")
#         dtlarik.append(br)
#     print()
#     return dtlarik
# def tulislarik(data, N):
#     if N > 0:
#         tulislarik(data, N-1)
#         print(data[N-1], end=" ")

# def caridata(data,kunci):
#     N = len(data)
#     for i in range(N):
#         if data[i] == kunci:
#             return i
#     return -5
# def ulangcari():
#     cari = 6
#     while cari > 0:
#         cari = int(input('Data yang dicari: '))
#         ktm = caridata(dlr, cari)
#         if ktm >= 0:
#             print('Ada pada indeks ke ', ktm)
#         else:
#             print('Tidak ketemu!!')


# N = int(input('Banyaknya data: '))
# print("Hasil bacadata random: ")
# dlr = bacadata(N)

# print('Hasil tulis data: ')
# tulislarik(dlr, N)
# print()
# ulangcari()


# import random
# def bacadata (M):
#     dtlarik = []
#     for i in range(M):
#         br = random.randint(1, 20)
#         print(br, end= " ")
#         dtlarik.append(br)
#     print()
#     return dtlarik
# def tulislarik(data, N):
#     if N > 0:
#         tulislarik(data, N-1)
#         print(data[N-1], end=" ")

# def buatdatafrek(data,N):
#     datfrek = []
#     for i in range (10):
#         frek = 0
#         for j in range(N):
#             if data[j] == i+1:
#                 frek += 1
#         print(i, ':', frek)
#         datfrek.append(frek)
#     return datfrek
# def tulisdatafrek(data, N):
#     df = buatdatafrek(data, N)
#     print('=======================================================')
#     print('|                Diagram Frekuensi                 |')
#     print('=======================================================')
#     for i in range (10):
#         print(i, ":", end="")
#         for j in range(df[i]):
#             print("#", end="")
#         print()


# N = int(input('Banyaknya data: '))
# print("Hasil bacadata random: ")
# dlr = bacadata(N)
# print('Hasil tulis data: ')
# tulislarik(dlr, N)
# print()
# tulisdatafrek(dlr, N)

# Pengurutan
# Mempermudah pencarian data
# Membantu analisis data
# Jenis Pengurutan Data 1 -> Ascending (Terurut naik)
# Jenis Pengurutan Data 2 -> Descending (Terurut turun)

# data = [5,2,9,1,7]
# data.sort()
# print(data)

# import random
# def bacadata(M):
#     dtlarik = []
#     for i in range(M):
#         br = random.randint(1, 20)
#         print(br, end= " ")
#         dtlarik.append(br)
#     print()
#     return dtlarik
# def linear_search(data,kunci):
#     for i in range(N):
#         if data[i] == kunci:
#             return i
#     return -1
# N = int(input('Banyaknya data: '))
# print("Hasil bacadata random: ")
# dlr = bacadata(N)
# cari = -8
# while cari < 0:
#     cari = int(input('Data yang dicari: '))
#     ktm = linear_search(dlr, cari)
#     if ktm >= 0:
#         print('Ada pada indeks ke: ', ktm)
#     else:
#         print('Tidak ketemu!!')
# print()


# #Materi hari ini kamis 7 mei 2026
# #Tentang Bubble sort, Selection Sort, Insertion Sort

# def bubble_sort(data):
#     n = len(data)
#     for i in range (n):
#         for j in range(0, n-i-1):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#     return data

# def selection_sort(data):
#     n = len(data)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if data[j] < data[min_idx]:
#                 min_idx = j
#         data[i], data[min_idx] = data[min_idx], data[i]
#     return data

# def insertion_sort(data):
#     n = len(data)
#     for i in range(1, n):
#         key = data[i]
#         j = i - 1
#         while j >= 0 and key < data[j]:
#             data[j + 1] = data[j]
#             j -= 1
#         data[j + 1] = key
#     return data


# def linear_search(data,kunci):
#     for i in range(N):
#         if data[i] == kunci:
#             return i
#     return -1

# def binary_search(data, target):
#     kiri = 0
#     kanan = len(data) -1
#     while kiri <= kanan:
#         tengah = (kiri + kanan) // 2
#         if data[tengah] == target:
#             return tengah
#         elif data[tengah] < target:
#             kiri = tengah + 1
#         else:
#             kanan = tengah - 1
#     return -1

# def bacadata(jumlah):
#     data = []

#     for i in range(jumlah):
#         angka = int(input('Masukkan angka ke: '))
#         data.append(angka)
#     return data
# hasil = bacadata(3)
# print(hasil)


# import random
# def inputdata(n):
#     data = []
#     for i in range(n):
#         angka = random.randint(10,99)
#         data.append(angka)
#     return data

# def tampil(data):
#     for i in range(len(data)):
#         print(data[i], end=" ")
#     print()
# def bubble_sort(data):
#     n = len(data)
#     for i in range (n-1):
#         for j in range( n-i-1):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#     return data
# def sequential_search(data, target):
#     for i in range(len(data)):
#         if data[i] == target:
#             return i
#     return -1
# def menu_pencarian(data):
#     while True:
#         cari = int(input('Masukkan angka yang ingin dicari (0 untuk keluar): '))
#         if cari == 0:
#             print('Program selesai.')
#             break
#         hasil = sequential_search(data, cari)
#         if hasil >= 0:
#             print("Data ditemukan pada indeks ke: ", hasil)
#         else:
#             print("Data tidak ditemukan.")

# angka = int(input('Masukkan jumlah data: '))
# data = inputdata(angka)
# print('Data sebelum sorting: ')
# tampil(data)
# bubble_sort(data)
# print('Data setelah sorting: ')
# tampil(data)
# menu_pencarian(data)

# Perbaiki kode yang salah
# import random
# def buatdata(N):
#     data = []
#     for i in range(N):
#         angka = random.randint(1, 50)
#         data.append(angka)
#     return data
# def cetakdata(data):
#     for i in range(len(data)):
#         print(data[i], end=" ")
#     print()
# def insertion_sort(data):
#     for i in range(1, len(data)):
#         key = data[i]
#         j = i - 1
#         while j >= 0 and key < data[j]:
#             data[j + 1] = data[j]
#             j -= 1
#         data[j + 1] = key
#     return data
# def cari_data(data, target):
#     ditemukan = False
#     for i in range(len(data)):
#         if data[i] == target:
#             ditemukan = True
#     if ditemukan == False:
#         print("Data tidak ditemukan.")
# def proses_cari(data):
#     ulang = 'y'
#     while ulang == 'y':
#         cari = int(input('Masukkan data yang ingin dicari: '))
#         cari_data(data, cari)
#         ulang = input('Cari Lagi? (y/t): ')

# N = int(input('Masukkan banyak data: '))
# data = buatdata(N)
# print('Data awal: ')
# cetakdata(data)
# print('Data setelah diurutkan: ')
# urut = insertion_sort(data)
# cetakdata(urut)
# proses_cari(urut)

# Perbaiki kode ini
# import random
# def pencarian(data):
#     cari = 10
#     while cari > 0:
#         cari = int(input('Masukkan data yang dicari: '))
#         ditemukan = False
#         for i in range(len(data)):
#             if data[i] == cari:
#                 print('Data ditemukan pada indeks ke: ', i)
#                 ditemukan = True
#                 break
#             else:
#                 print('Data tidak ditemukan!!')
# def bacadata(n):
#     data = []
#     for i in range(n):
#         angka = random.randint(1, 20)
#         print(angka, end=" ")
#         data.append(angka)
#     print()
#     return data
# def tulislarik(data, n):
#     if n > 0:
#         tulislarik(data, n-1)
#         print(data[n-1], end=" ")
# def insertion_sort(data):
#     for i in range(1, len(data)):
#         key = data[i]
#         j = i - 1
#         while j >= 0 and key < data[j]:
#             data[j + 1] = data[j]
#             j -= 1
#         data[j + 1] = key
#     return data
# n = int(input('Masukkan banyak data: '))

# data = bacadata(n)
# tulislarik(data, n)

# print("Data setelah diurutkan: ")
# urut = insertion_sort(data)

# tulislarik(urut, n)
# pencarian(urut)

# program menentukan sebuah bilangan kuadrat yang melebih 10 bernilai false, jika tidak maka bernilai true

# D = 1,2,3,4
# for i in D:
#     if i**2 > 10:
#         print(i,'False')
#     else:
#         print(i,'True')


# Pengertian class
# class Aritmetika:
#     def __init__(this, a, b):
#         this.a = a
#         this.b = b

#     def tambah(itu):
#         return itu.a + itu.b

#     def kali(ini):
#         return ini.a * ini.b

#     def kurang(ada):
#         return ada.a - ada.b

#     def pangkat(aku):
#         return aku.a**aku.b


# mt = Aritmetika(5, 7)
# print("Hasil penjumlahan:", mt.tambah())
# print("Hasil perkalian:", mt.kali())
# print("Hasil pengurangan: ", mt.kurang())
# print("Hasil pemangkatan: ", mt.pangkat())


# class Geometri:
#     def __init__(self, sisi, simbol):
#         self.sisi = sisi
#         self.simbol = simbol

#     def bujursaangkar(self):
#         n = self.sisi
#         for i in range(n):
#             for j in range(n):
#                 print(self.simbol, end=" ")
#             print()

#     def segitiga(self):
#         n = self.sisi
#         for i in range(n):
#             for j in range(i + 1):
#                 print(self.simbol, end=" ")
#             print()

#     def gunung(self):
#         n = self.sisi
#         for i in range(n):
#             for j in range(i, n):
#                 print(" ", end="")
#             for j in range(2 * i + 1):
#                 print(self.simbol, end="")
#             print()


# gambar1 = Geometri(10, "#")
# gambar1.gunung()
# gambar1.segitiga()
# gambar2 = Geometri(5, "+")
# gambar2.bujursaangkar()
# import random


# import random
# def bacadata(M):
#     dtlarik = []
#     for i in range(M):
#         br = random.randint(1, 99)
#         dtlarik.append(br)
#     return dtlarik

# def tulislarik(data):
#     N = len(data)
#     for i in range(N):
#         print("%2d" % (data[i]), end=" ")
#         #print(data[i], end=" ")
#     print()

# def selection_sort(data):
#     n = len(data)
#     for i in range(n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if data[j] < data[min_idx]:
#                 min_idx = j
#         tandai(n, i, min_idx)
#         data[i], data[min_idx] = data[min_idx], data[i]
#         tulislarik(data)
#     return data

# def tandai(N, j, k):
#     for i in range(N):
#         if (i == j) or (i == k):
#             print("%2s" % ("^"), end=" ")
#         else:
#             print("%2s" % (" "), end=" ")
#     print()

# N = int(input("Masukan banyaknya data: "))
# data = bacadata(N)
# tulislarik(data)
# print("Langkah-langkah pengurutan metode seleksi")
# print("==========================================")
# tulislarik(data)
# dturut = selection_sort(data)


# class Orang:
#     def __init__(self, nama):
#         self.nama = nama

#     def tulis(ini):
#         print("Nama: ", ini.nama)


# budi = Orang("Budiharjo")
# budi.tulis()


# class Mahasiswa:
#     def __init__(self, nama, nilai1, nilai2):
#         self.nama = nama
#         self.nilai1 = nilai1
#         self.nilai2 = nilai2
# 21
#     def tulis(ini):
#         print("Nama: ", ini.nama)
#         print("Nilai 1: ", ini.nilai1)
#         print("Nilai 2: ", ini.nilai2)
#         rata2 = (ini.nilai1 + ini.nilai2) / 2
#         print("Nilai huruf: ", ini.konversinilai(rata2))
#         print("=========================================")

#     def konversinilai(this, bil):
#         if bil >= 80:
#             return "A"
#         elif bil >= 65:
#             return "B"
#         elif bil >= 55:
#             return "C"
#         elif bil >= 48:
#             return "D"
#         else:
#             return "E"


# budi = Mahasiswa("Budi", 83, 35)
# budi.tulis()

# agus = Mahasiswa("Agus Suryanto", 73, 70)
# agus.tulis()

# kartika = Mahasiswa("Kartika Siti Munarroh", 90, 50)
# kartika.tulis()


# perbaiki kode ini, buatkan ouput seperti larik yang sudah dibuat sebelumnya dengan import random
# class Larik:
#     def __init__(self, n):
#         self.n = n
#         self.data = self.bacadata()

#     def bacadata(self):
#         import random

#         data = []
#         for i in range(self.n):
#             angka = random.randint(1, 99)
#             data.append(angka)
#         return data

#     def tulislarik(self):
#         for i in range(self.n):
#             print("%2d" % (self.data[i]), end=" ")
#         print()

#     def selection_sort(self):
#         n = len(self.data)
#         for i in range(n - 1):
#             min_idx = i
#             for j in range(i + 1, n):
#                 if self.data[j] < self.data[min_idx]:
#                     min_idx = j
#             self.tandai(n, i, min_idx)
#             self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
#             self.tulislarik()
#         return self.data

#     def tandai(self, N, j, k):
#         for i in range(N):
#             if (i == j) or (i == k):
#                 print("%2s" % ("^"), end=" ")
#             else:
#                 print("%2s" % (" "), end=" ")
#         print()


# N = int(input("Masukan banyaknya data: "))
# larik = Larik(N)
# larik.tulislarik()
# print("Langkah-langkah pengurutan metode seleksi")
# print("==========================================")
# larik.tulislarik()
# dturut = larik.selection_sort()


# Merubah pemrograman yang tidak OOP(Object Oriented Programming)  menjadi OOP
# class jenisbilangan:
#     def __init__(self, bil):
#         self.bil = bil

#     def prima(self):
#         num = self.bil
#         yg_prima = True
#         for i in range(2, num):
#             if num % i == 0:
#                 yg_prima = False
#                 break
#         return yg_prima

#     def genap(self):
#         num = self.bil
#         return num % 2 == 0

#     def ganjil(self):
#         num = self.bil
#         return num % 3 == 0


# bilangan = 12
# jb = jenisbilangan(bilangan)
# if jb.prima():
#     print(bilangan, "adalah bilangan prima")
# else:
#     print(bilangan, "bukan bilangan prima")
# if jb.genap():
#     print(bilangan, "adalah bilangan genap")
# else:
#     print(bilangan, "bukan bilangan genap")
# if jb.ganjil():
#     print(bilangan, "adalah bilangan ganjil")


# def jumlahN(N):
#     jumlah = 0
#     s = "Jumlah "
#     for i in range(1, N):
#         jumlah += i
#         s += str(i) + " + "
#     jumlah += N
#     s += str(N)
#     s += " = " + str(jumlah)
#     print(s)


# jumlahN(12)


# buat kode diatas dengan bentuk OOP
# class JumlahN:
#     def __init__(self, bil):
#         self.bil = bil

#     def hitung(self):
#         N = self.bil
#         jumlah = 0
#         s = "Jumlah "
#         for i in range(1, N):
#             jumlah += i
#             s += str(i) + " + "
#         jumlah += N
#         s += str(N)
#         s += " = " + str(jumlah)
#         print(s)


# jumlah = JumlahN(12)
# jumlah.hitung()


# def faktorial(N):
#     jumlah = 1
#     s = "Hasil "
#     for i in range(1, N):
#         jumlah *= i
#         s += str(i) + " * "
#     jumlah *= N
#     s += str(N)
#     s += " = " + str(jumlah)
#     print(s)


# EN = int(input("Masukkan bilanganny: "))
# print(faktorial(EN))


# class Faktorial:
#     def __init__(self, bil):
#         self.bil = bil

#     def hitung(self):
#         N = self.bil
#         jumlah = 1
#         s = "Hasil "
#         for i in range(1, N):
#             jumlah *= i
#             s += str(i) + " * "
#         jumlah *= N
#         s += str(N)
#         s += " = " + str(jumlah)
#         print(s)


# faktorial = Faktorial(5)
# faktorial.hitung()


# class Aritmatika:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def penjumlahan(self):
#         print("Hasil penjumlahan:", self.a, "dan", self.b, "= ", self.a + self.b)

#     def perkalian(self):
#         print("Hasil perkalian:", self.a, "dan", self.b, "= ", self.a * self.b)


# a = int(input("Masukkan bilangan a:"))
# b = int(input("Masukkan bilangan b:"))
# aritmatika = Aritmatika(a, b)
# aritmatika.penjumlahan()
# aritmatika.perkalian()


# class Hewan:
#     def __init___(
#         self,
#         nama,
#     ):
#         self.nama = nama

#     def bersuara(self):
#         print("Bersuara")


# class Kucing(Hewan):
#     def __init__(self):
#         super().__init__("Kucing")

#     def bersuara(self):
#         print(self.nama, "bersuara meong")


# class Anjing(Hewan):
#     def __init__(self):
#         super().__init__("Anjing")

#     def bersuara(self):
#         print(self.nama, "bersuara guk guk")


# class Singa(Hewan):
#     def __init__(self):
#         super().__init__("Singa")

#     def bersuara(self):
#         print(self.nama, "bersuara geerrr...")


# class Bebek(Hewan):
#     def __init__(self):
#         super().__init__("Bebek")

#     def bersuara(self):
#         print(self.nama, "bersuara kwek kwek")


# hewan2 = [Kucing(), Anjing(), Singa(), Bebek()]
# for k in hewan2:
#     k.bersuara()


class OperasiDasar:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hitung(self):
        return "Hasil: "


class Penjumlahan(OperasiDasar):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hitung(self):
        hsl = self.a + self.b
        s = f"Hasil {self.a} + {self.b} = {hsl}"
        return s


class Pengurangan(OperasiDasar):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hitung(self):
        hsl = self.a - self.b
        s = f"Hasil {self.a} - {self.b} = {hsl}"
        return s


class Perkalian(OperasiDasar):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hitung(self):
        hsl = self.a * self.b
        s = f"Hasil {self.a} * {self.b} = {hsl}"
        return s


class Pembagian(OperasiDasar):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hitung(self):
        if self.b == 0:
            return "Hasil pembaginya tidak terdefinisi, penyebutnya 0"

        else:
            hsl = self.a * self.b
            s = f"Hasil {self.a} * {self.b} = {hsl}"
            return s


jum = Penjumlahan(3, 4)
print(jum.hitung()) i
kali = Perkalian(3, 4)
print(kali.hitung())
bagi = Pembagian(5, 0)
print(bagi.hitung())


class Mahasiswa:
    def __init__(self, nim, nama, nilai1, nilai2):
        self.nim = nim
        self.nama = nama
        self.nilai1 = nilai1
        self.nilai2 = nilai2

    def tulis(ini, no):
        print(
            "| %-3d  | %-11s  | %-30s  | %-5d |  %-5d | %-2s |"
            % (no, ini.nim, ini.nama, ini.nilai1, ini.nilai2, ini.konversinilai())
        )

    def konversinilai(this):
        bil = (this.nilai1 + this.nilai2) / 2
        if bil >= 80:
            return "A"
        elif bil >= 65:
            return "B"
        elif bil >= 55:
            return "C"
        elif bil >= 40:
            return "D"
        else:
            return "E"


def bcdt():
    dtlarik = []
    dtlarik.append(Mahasiswa("2200016004", "Weka Hayu Pratista", 82, 60))
    dtlarik.append(Mahasiswa("2500016002", "Rafi Yasin Ramadhan", 70, 83))
    dtlarik.append(Mahasiswa("2500016003", "Muhammad Ahsan", 67, 75))
    dtlarik.append(Mahasiswa("2500016010", "Harun", 77, 65))
    dtlarik.append(Mahasiswa("2500016017", "Wa Dita H. Putri", 67, 70))
    dtlarik.append(Mahasiswa("2500016018", "Muhammad Arkan Zaky", 65, 67))
    dtlarik.append(Mahasiswa("2500016020", "Gunawan", 84, 80))
    dtlarik.append(Mahasiswa("2500016036", "Cita Kharisma Siti Khatijah", 98, 50))
    dtlarik.append(Mahasiswa("2500016042", "Raditha Dwi Oktaviana", 81, 70))
    dtlarik.append(Mahasiswa("2500016047", "Anggun Indriani", 88, 80))
    dtlarik.append(Mahasiswa("2500016048", "Erica Selviana Putri", 95, 75))
    dtlarik.append(Mahasiswa("2500016050", "Halimah", 75, 70))
    return dtlarik


dtmhs = bcdt()
N = len(dtmhs)

print("-" * 87)
print(
    "| %-3s | %-11s | %-30s | %-5s | %-5s | %2s |"
    % ("No", "NIM", "NAMA", "NILAI1", "NILAI2", "NH")
)
print("-" * 87)

for i in range(N):
    dtmhs[i].tulis(i + 1)

print("-" * 87)


# file = open("Sapa.txt", "w")
# file.write("Halo Python\n")
# file.write("Bagaimana kabarmu...")
# file.write("Baikkah?")

# file.close()

# file = open("Sapa.txt", "r")
# isi = file.read()
# print(isi)
# file.close()


# file = open("ayahku.txt", "a")
# file.write("============================\n")
# file.close()
# file = open("ayahku.txt", "r")
# isi = file.read()
# print(isi)
# file.close()


# import json
# data = {"Nama": "Budi", "Umur": 20}

# with open('dtMhsSelasa7.json', 'w') as file:
#     json.dump(data, file)

# with open('dtMhsSelasa7.json', 'r') as file:
#     data= json.load(file)
#     print(data)


# def factorial(n):
#     if n == 0 or n == 1:  # base case
#         return 1
#     return n * factorial(n - 1)


# print(factorial(4))


