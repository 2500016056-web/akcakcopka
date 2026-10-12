nilai = [2,3,4,5]
hasil = 0
for i in range(len(nilai)):
    if i % 2 == 0:
        hasil += nilai[i]
    else:
        hasil *= nilai [i]
print(hasil) 
#Jika variabel hasil = 0
#indeks 0 (1) = hasil(0) + nilai = 2
#indeks 1 (2) = hasil(2) x nilai = 6
#indeks 2 (3) = hasil(6) + nilai =  10
#indeks 3 (4) = hasil(10) x nilai = 50

#Jika variabel hasil = 1
#indeks 0 (1) = hasil (1) + nilai = 3
#indeks 1 (2) = hasil (3) x nilai = 9
#indeks 2 (3) = hasil (9) + nilai = 13
#indeks 3 (4) = hasil (13) x nilai = 65



