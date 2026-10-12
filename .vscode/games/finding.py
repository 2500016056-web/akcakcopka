import random
from function import welcome_message 


def start(): 
    nama_user = input('Masukkan nama kamu: ')
    while nama_user == '':
        nama_user = input('Isi dulu nama anda: ')
        

    api_position = random.randint(1,5)


    bentuk_goa = "|_|"

    goa_kosong = [bentuk_goa] * 5

    goa = goa_kosong.copy() 
    goa_kosong = ' '.join(goa_kosong)

    goa[api_position - 1] = "0_0"
    goa = ' '.join(goa)

    while True:
        api_position = random.randint(1,5)


        bentuk_goa = "|_|"

        goa_kosong = [bentuk_goa] * 5

        goa = goa_kosong.copy() 
        goa_kosong = ' '.join(goa_kosong)

        goa[api_position - 1] = "0_0"
        goa = ' '.join(goa)

        print(f'''
        Halo {nama_user}! Coba perhatikan goa dibawah ini.
        {goa_kosong}
        ''' )
        print()
        try: 
            pilihan_user = int(input('Menurut kamu di goa nomor berapakah api berada? [1 / 2 / 3 / 4 / 5 ]: '))
            print()
            if  pilihan_user < 1 or pilihan_user > 5:
                continue 
        except ValueError:
                print('Input tidak valid. Silahkan masukkan angka antara 1 sampai 5.')
                continue
        
        print(f"Pilihan kamu {pilihan_user}")

        print()

        confirm_answer = input('Apakah kamu yakin dengan pilihanmu? [ya/tidak]: ')  
        while confirm_answer == '':
            confirm_answer = input('Isi dulu jawaban kamu, yakin apa tidak [ya/tidak]: ')

        print()

        if confirm_answer == 'tidak':
            print('Program Dihentikan.')
            exit()
        elif confirm_answer == 'ya': 
            if pilihan_user == api_position:
                print(f'''SELAMAT {nama_user} KAMU MENDAPATKAN API! 
        Posisi Api Berada Di: 
        {goa}, 
        Tepat seperti pilihanmu yaitu: {api_position}''')
            else:
                print(f'''Maaf, {nama_user} Kamu Salah! Posisi Api berada di 
        {goa} , 
        Yaitu: {api_position}''')
        else:
            print('Pilihan tidak valid. Silahkan ulangi programnya.')
            exit()
            
        play_again = input('Mau coba lagi? [y/n]: ')
        if play_again == 'n':
            break


    

if __name__ == "__main__":
    start()
    