password = input("Masukkan password: ")
skor = 0

ada_huruf_besar = False
ada_huruf_kecil = False
ada_angka = False
ada_tanda_baca = False

for i in password:
   if i.isupper():
       ada_huruf_besar = True
   elif i.islower():
       ada_huruf_kecil = True
   elif i.isdigit():
       ada_angka = True
   else:
       ada_tanda_baca = True    

if ada_huruf_besar and ada_huruf_kecil:
    skor += 10
    print(f"{password} -> Ada huruf besar & kecil")
if ada_angka:
    skor += 10
    print(f"{password} -> Ada angka")
if ada_tanda_baca:
    skor += 5
    print(f"{password} -> Ada tanda baca")


if len(password) >= 8:
    skor += 5
    print("Panjang karakter sudah cukup")
else:
    print("Panjang karakter kurang dari 8")


print()
print(f"Skor: {skor}/30")

if skor < 15:
    print("Kategori: LEMAH")
elif skor < 25:
    print("Kategori: SEDANG")   
else:
    print("Kategori: KUAT")
        