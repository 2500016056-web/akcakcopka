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


class Geometri:
    def __init__(self, sisi, simbol):
        self.sisi = sisi
        self.simbol = simbol

    def bujursaangkar(self):
        n = self.sisi
        for i in range(n):
            for j in range(n):
                print(self.simbol, end=" ")
            print()

    def segitiga(self):
        n = self.sisi
        for i in range(n):
            for j in range(i + 1):
                print(self.simbol, end=" ")
            print()

    def gunung(self):
        n = self.sisi
        for i in range(n):
            for j in range(i, n):
                print(" ", end="")
            for j in range(2 * i + 1):
                print(self.simbol, end="")
            print()


gambar1 = Geometri(10, "#")
gambar1.gunung()
gambar1.segitiga()
gambar2 = Geometri(5, "+")
gambar2.bujursaangkar()
