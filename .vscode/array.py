# buah = ["apel", "banana", "cherry", "manggis","jeruk"]
# buah.append('manggis')
# print(buah)


# nama =["Andi", "Budi", "Caca"
#        ",Dedi","Eka",
#        "Feri",
#        "Gina"
# ]
# del nama[2]
# print(nama)



# buah = ["apel", "banana", "cherry", "manggis","jeruk"]
# buah.insert(2, "kiwi")
# print(buah)

# buah = ["apel", "banana", "cherry", "manggis","jeruk"]
# buah.insert(2, "kiwi")
# print(buah)


# def tulislarik(data):
#        n = len(data)
#        for i in range (n):
#               print(data[i], end=" ")
#        print()
# data = [10,20,30,40]
# data[3] = 8
# data.append(50)
# tulislarik(data)
# print('Data Minimum: ', min(data))
# print('Data Maksimum: ', max(data))
# print('Jumlah Data: ', sum(data))
# print('Rata-rata Data: ', sum(data)/len(data))




# matriks = [

#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# def tampil (matriks):
#     for i in range(len(matriks)):
#         for j in range(len(matriks[i])):
#             print(matriks[i][j], end=" ")
#         print() 
# tampil(matriks)


# import array
# data = array.array('i', [10, 20, 30, 40])
# print(data[3])



#mencari genap
# data = [1,2,3,4,5,6,]
# for i in data:
#     if i % 2 == 0:
#         print(i, 'Genap')
#     else: 
#         print(i, 'Ganjil')

import random
def bacadata (M):
    dtlarik = []
    for i in range(M):
        br = random.randint(1, 20)
        print(br, end= " ")
        dtlarik.append(br)
    print()
    return dtlarik
def tulislarik(data, N):
    if N > 0:
        tulislarik(data, N-1)
        print(data[N-1], end=" ")
N = int(input('Banyaknya data: '))
print("Hasil bacadata random: ")
dlr = bacadata(N)
print('Hasil tulis data: ')
tulislarik(dlr, N)
print()
        
        

