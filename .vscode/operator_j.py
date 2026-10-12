#Menghitung modulo menggunakan operator aritmatika

#a. 6 mod 3
#a = 6
#b = 3
#hasil_a = a - (a // b) * b
#print("6 mod 3 =", hasil_a)

#b. 75 mod 4
#a = 75
#b = 4
#hasil_b = a - (a // b) * b
#print("75 mod 4 =", hasil_b)

#c.124 mod 5
#a = 124
#b = 5
#hasil_c = a - (a // b) * b
#print("124 mod 5 =", hasil_c)

#d. 225 mod 5
#a = 225
#b = 5
#hasil_d = a - (a // b) * b
#print("225 mod 5 =", hasil_d)








#Menghitung modulo dan menggunakan operator perbandingan

#a. 6 mod 3
#a = 6 % 3
#print("6 mod 3 =", a)
#print("Apakah hasilnya == 0 ?", a == 0)   #True jika hasilnya 0

#b. 75 mod 4
#b = 75 % 4
#print("75 mod 4 =", b)
#print("Apakah hasilnya > 2 ?", b > 2)

#c. 124 mod 5
#c = 124 % 5
#print("124 mod 5 =", c)
#print("Apakah hasilnya != 0 ?", c != 0)

#d. 225 mod 5
#d = 225 % 5
#print("225 mod 5 =", d)
#print("Apakah hasilnya <= 0 ?", d <= 0)






#Menghitung hasil modulo dan memanfaatkan operator logika

#a. 6 mod 3
#a = 6 % 3
#print("6 mod 3 =", a)
#print("Apakah hasilnya 0 dan genap?", (a == 0) and (6 % 2 == 0))

#b. 75 mod 4
#b = 75 % 4
#print("75 mod 4 =", b)
#print("Apakah hasilnya lebih dari 2 atau sama dengan 3?", (b > 2) or (b == 3))

#c. 124 mod 5
#c = 124 % 5
#print("124 mod 5 =", c)
#print("Apakah hasilnya bukan 0 dan lebih kecil dari 5?", (c != 0) and (c < 5))

#d. 225 mod 5
#d = 225 % 5
#print("225 mod 5 =", d)
#print("Apakah hasilnya 0 atau genap?", (d == 0) or (225 % 2 == 0))






#Menghitung hasil modulo menggunakan operator bitwise

#a. 6 mod 3 (bukan pangkat 2, jadi kita pakai rumus umum)
#a = 6
#b = 3
#hasil_a = a - (a // b) * b
#print("6 mod 3 =", hasil_a)

#b. 75 mod 4 → karena 4 = 2^2, bisa pakai bitwise AND
#75 & (4 - 1) = 75 & 3
#hasil_b = 75 & (4 - 1)
#print("75 mod 4 =", hasil_b)

#c. 124 mod 5 → 5 bukan pangkat 2, pakai rumus umum
#c = 124
#d = 5
#hasil_c = c - (c // d) * d
#print("124 mod 5 =", hasil_c)

#d. 225 mod 5 → juga bukan pangkat 2
#e = 225
#f = 5
#hasil_d = e - (e // f) * f
#print("225 mod 5 =", hasil_d)




#Menghitung modulo menggunakan operator assignment

#1. 6 mod 3
#3 x = 6
#x %= 3
#print("6 mod 3 =", x)

#2. 75 mod 4
#x = 75
#x %= 4
#print("75 mod 4 =", x)

#3. 124 mod 5
#x = 124
#x %= 5
#print("124 mod 5 =", x)

#4. 225 mod 5
#x = 225
#x %= 5
#print("225 mod 5 =", x)




#Menghitung modulo dan membandingkan hasilnya dengan operator identitas

#1. 6 mod 3
#a = 6 % 3
#print("6 mod 3 =", a)
#print("Apakah hasilnya adalah 0?", a is 0)

#2. 75 mod 4
#b = 75 % 4
#print("75 mod 4 =", b)
#print("Apakah hasilnya adalah 3?", b is 3)

#3. 124 mod 5
#c = 124 % 5
#print("124 mod 5 =", c)
#print("Apakah hasilnya adalah 4?", c is 4)

#4. 225 mod 5
#d = 225 % 5
#print("225 mod 5 =", d)
#print("Apakah hasilnya adalah 0?", d is 0)




#Latihan menghitung modulo dan menggunakan operator keanggotaan

#List hasil yang benar untuk dicek
#hasil_benar = [0, 3, 4]

#a. 6 mod 3
#a = 6 % 3
#print("Hasil 6 mod 3 =", a)
#print("Apakah hasil a ada di dalam daftar hasil_benar?", a in hasil_benar)

#b. 75 mod 4
#b = 75 % 4
#print("Hasil 75 mod 4 =", b)
#print("Apakah hasil b ada di dalam daftar hasil_benar?", b in hasil_benar)

#c. 124 mod 5
#c = 124 % 5
#print("Hasil 124 mod 5 =", c)
#print("Apakah hasil c ada di dalam daftar hasil_benar?", c in hasil_benar)

#d. 225 mod 5
#d = 225 % 5
#print("Hasil 225 mod 5 =", d)
#print("Apakah hasil d tidak ada dalam daftar hasil_benar?", d not in hasil_benar)





#nilai = input('Masukkan nilai (A,B,C,D,E)')
#match nilai:
    #case "A": ket = "Luar Biasa"
    #case "B": ket = "Baik Sekali"
    #case "C": ket = "Cukup Baik"
    #case "D": ket = "Perlu Peningkatan"
    #case "E": ket = "Tidak Lulus"
#except ValueError:
#ket = "Nilai Tidak Lulus!"
#print(ket)






# 1. Minta input dari user
# .strip() untuk menghapus spasi, .upper() untuk mengubah jadi huruf besar
#nilai_huruf = input("Masukkan nilai huruf (A, B, C, D, atau E): ").strip().upper()

# 2. Gunakan 'match' (mirip 'switch') untuk mengevaluasi nilai
#match nilai_huruf:
    #case "A":
        #keterangan = "Luar biasa!"
    
    #case "B":
        #keterangan = "Baik sekali!"
        
    #case "C":
        #keterangan = "Cukup baik!"
        
    #case "D":
        #keterangan = "Perlu peningkatan!"
        
    #case "E":
        #keterangan = "Tidak lulus!"
        
    # 'case _' sama fungsinya dengan 'default'
    #case _: 
       #keterangan = "Nilai tidak valid!"

# 3. Tampilkan hasil
#print(keterangan)
 




#i = 1
#while (i<=10):
    #print('Iterasi ke : ', i , ' : Belajar Perulangan While')
  # i=i+1
#print(i)

#n = int(input('Masukkan sembarang nilai :'))
#i = 0
#while (n>=0.01):
    #n = n / 2
    #i = i + 1
#rint(i) 
#print('Jumlah Iterasi')




#while loop
# while kondisi:
    #aksi ini
    #aksi itu
#akhir dari program

#angka = 0
#print(f' Angka Sekarang --> {angka}')
#while angka < 5:
    #angka += 1 
   # print(f' Angka Sekarang --> {angka}')
#print('INFAITH KELAZZZZZZZZZZZ')
#print('CUKUP')




# Tugas 1 daspro palindrom
kata = input("Masukkan kata: ")
kata = kata.lower()

kata_balik = kata[::-1]

if kata == kata_balik:
    print("Kata tersebut adalah palindrom")
else:
    print("Kata tersebut bukan palindrom")












