#spotify = [["Mijil", "Pocung","Maskulin"],
  #         ["Nor-ibu", "Manuk dadali","Borero" ],
 #          ["Zapin ","Ranca Kuah"],
 #          ["Bidadari Surga","Tombok Ati" ]]
#for genre in spotify:
   #for judul in genre:
       #jml_karakter = len(judul)
       #print(f"Judul: {judul}, Jumlah karakter: {jml_karakter}")
          




#baju = 30000
##celana = 45000
#topi = 15000

#jb = int(input('Masukkan jumlah Baju: '))
#jc = int(input('Masukkan jumlah Celana: '))
#jt = int(input('Masukkan jumlah Topi: '))

#harga = jb * baju + jc * celana + jt * topi
#jbr =  jb + jc + jt
# Tentukan persentase diskon berdasarkan jumlah barang
#if jbr == 0:
 #  diskon_persen = 0.0
##  diskon_persen = 0.20
#else:
 #  diskon_persen = 0.30

#diskon = diskon_persen * harga
#total_semua = harga - diskon

#print(f"Total harga (sebelum diskon): Rp. {harga}")
#print(f"Diskon: {int(diskon_persen*100)}% )")
#print(f"Total yang harus anda bayar adalah: Rp. {int(total_semua)}")






# Tugas Mencari Posisi Indeks Elemen didalam Array.
# array = [10,20,30,40,50,]

# elemen = int(input('Masukkan elemen yang dicari : '))
# ketemu = False

# for i in range (len (array)):
#     if array[i] == elemen:
#         print(f'Angka {elemen} ditemukan pada indeks ke-{i}')
#         ketemu = True
#         break


#Tugas Reverse Array
# array = [1,2,3,4,5]
# array_reversed = []

# for i in range(len(array)-1, -1, -1):
#     array_reversed.append(array[i])
# print(f'Array asli: {array}')
# print(f'Array setelah direverse: {array_reversed}')


#Tugas Membuat Ascending 
# array = [5,3,8,6,2]

# a = len(array)
# for i in range(a):
#     for j in range(0, a-i-1):
#         if array[j] > array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]

# print(f'Array setelah diurutkan secara ascending: {array}')


# array = [5, 3, 8, 6, 2]

# for i in range(1, len(array)):
#     angka = array[i]
#     j = i - 1
    
#     while j >= 0 and array[j] < angka:  
#         array[j + 1] = array[j]
#         j -= 1
    
#     array[j + 1] = angka
# print(f'Array setelah diurutkan secara descending: {array}')


#Tugas Mencari Duplikat dalam Array
# array =  [1, 2, 3, 4, 5, 2, 3]
# duplikat = []
# for i in range(len(array)):
#     for j in range(i + 1, len(array)):
#         if array[i] == array[j] and array[i] not in duplikat:
#             duplikat.append(array[i])

# print(f'Array: {array}')
# print(f'Duplikat: {duplikat}')


#Tugas Menghitung Panjang string dalam array
# array = ["Alice", "Bob", "Charlie", "Diana"]
# panjang_nama = []
# for i in array:
#     if len(i) > 4:
#         panjang_nama.append(i)
# print(f'Array: {array}')
# print(f'Nama dengan panjang lebih dari 4 karakter: {panjang_nama}')


#Tugas Menghitung Jumlah huruf A dalam nama sendiri
# nama = input("Masukkan nama kamu: ")
# n = nama.lower()
# jumlah_a = 0
# for i in n:
#     if i == 'a':
#         jumlah_a += 1

# print(f'Jumlah huruf a/A dalam nama kamu adalah: {jumlah_a}')

#Tugas pisahkan nama nama lalu gabungkan dengan pemisah " dan "
# text = "agus , gus , budi , yayan " 
# nama_list = text.split(",")
# hasil = "dan".join(nama_list)
# print(hasil)

#  Diberikan sebuah text "Saya adalah warga indonesia" ubah huruf a di text itu menjadi i
# Output Siyi idilih wirgi indonesii


# nama ='Akbar KING PS'
# umur = 21
# tinggi_badan = 171.5

# boolean = True
# print('Halooo semuanyaaaaa, kenalin nama saya', nama)
# print('Umur saya sekarang', umur)
# print('tinggi badan saya adalah', tinggi_badan)

# Daftar harga kopi
harga_kopi = {
    "Espresso": {"M": 15000, "L": 18000, "XL": 21000},
    "Americano": {"M": 18000, "L": 21000, "XL": 24000},
    "Latte": {"M": 22000, "L": 25000, "XL": 28000},
    "Cappuccino": {"M": 22000, "L": 25000, "XL": 28000},
    "Macchiato": {"M": 23000, "L": 26000, "XL": 29000},
    "Mocha": {"M": 25000, "L": 28000, "XL": 31000},
    "Flat White": {"M": 24000, "L": 27000, "XL": 30000}
}

biaya_bawa_pulang = 2000

print("=" * 50)
print("Selamat datang di kedai kopi".center(50))
print("=" * 50)

while True:
    jumlah_kopi = int(input('Masukkan jumlah kopi yang ingin dipesan: '))
    total_harga = 0

    for i in range(jumlah_kopi):
        print(f"Pesanan ke-{i+1}: ")
        print("Pilihan kopi:")
        for kopi in harga_kopi:
            print(f"- {kopi}")

        nama_kopi = input("Masukkan nama kopi yang ingin dipesan: ")
        ukuran = input("Masukkan ukuran (M/L/XL): ").upper()

        if nama_kopi in harga_kopi and ukuran in harga_kopi[nama_kopi]:
            total_harga += harga_kopi[nama_kopi][ukuran]
        else:
            print("Kopi atau ukuran tidak valid.")

    bawa_pulang = input("Apakah Anda ingin membawa pulang? (y/n): ").lower()
    if bawa_pulang == "y":
        total_harga += biaya_bawa_pulang

    print(f"Total harga: Rp. {total_harga}")