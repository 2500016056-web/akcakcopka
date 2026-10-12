#x = int(input('Masukkan sembarang nilai '))

#if x % 2 == 0:
 #   ket ='genap'
#else:
 #   ket = 'ganjil'
#print(ket)

#N = int(input('Masukkan N: '))
#M = 1
#F = 1
#while M <= N:
#    F = F*M
 #   M = M + 1
#print('Hasil F = ', F)








#X = int(input('Masukkan Nilai X: '))
#Y = int(input('Masukkan Nilai Y: '))

#P = X + Y

#if P >= 0:n
    #Q = X*Y
#else:
 #   Q = X / Y
#print(Q)



#n = int(input('Masukkan nilai n: '))
#for j in range(1,n):
#    S = j*(j+2)
#print('Bil ke  1 =', j = S)
#print('Bil ke  2 =, 'j = S)
#print('Bil ke  3 =', j = S)








from games import finding
from function import welcome_message, exit_message


def options():
    user_options = input('Pilih aplikasi yang ingin dijalankan:\n1. Permainan Tebak Posisi Api di Goa\n2. Warung Sederhana\nMasukkan pilihan (1/2): ')
    return user_options


def main():
    
    welcome_message('PERMAINAN TEBAK POSISI API DI GOA')
    user_options = options()
    if user_options == '1':
        finding.start()
    elif user_options == '2':
        warung.start()
    else:
        print('Pilihan tidak valid. Program dihentikan.')
    exit_message()

    
if __name__ == '__main__':
    main()



















#Konversi Suhu.
#print('1. Konversi Celcius ke Fahrenheit.')
#print('2. Konversi Fahrenheit ke Celcius.')

#pilihan_user = int(input('Masukkan pilihan Anda: '))
# f = (celcius * 9 / 5) + 32
 #  print('Hasil fahrenheit adalah: ', f,'f')
#elif pilihan_user == 2:
 #  fahrenheit = float(input('Masukkan Suhu: '))
  # c = (fahrenheit - 32) * 5 / 9
   #print('Hasil Celcius adalah: ', c,)





#baju = 30000
#celana = 45000
#topi = 15000

#jb = int(input('Masukkan jumlah Baju: '))
#jc = int(input('Masukkan jumlah Celana: '))
#jt = int(input('Masukkan jumlah Topi: '))

#harga = jb * baju + jc * celana + jt * topi
#jbr =  jb + jc + jt
#if jbr == 0:
  #  diskon = 0
#elif jbr < 20:
 #   diskon = 0.20 * harga
#else:
   # diskon = 0.30 * harga
#harga = harga - diskon
#print('Maka Hasil Belanjaannya adalah: ', harga)





   
