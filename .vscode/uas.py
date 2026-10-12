#Program Es Krim

def es_krim():
    container = [
        {'Jenis ': 'Cup', 'Harga ': 10000},
        {'Jenis ': 'Cone', 'Harga': 16000},
    ]
    
    topping = [
        {'Jenis ': 'Chocolate Sprinkle', 'Harga ': 6000},
        {'Jenis ': 'Strawberry Coulis', 'Harga ': 12000},
        {'Jenis ': 'FLake', 'Harga ':8000},
    ]
    

    total = 0
    
    print('===== MENU ES KRIM =====')
    while True:
        cup_choice = input('Pilih Wadah Es Krim (Cup/Cone): ')
        if cup_choice.lower() == 'cup':
            total += container[0]['Harga ']
            print('Wadah Cup dipilih.\n Harga: Rp 10.000')
        elif cup_choice.lower() == 'cone':
            total += container[1]['Harga']
            print('Wadah Cone dipilih.\n Harga: Rp 16.000')
        else:
            print('Pilihan tidak valid. Silahkan pilih wadah yang tersedia.')
            
            
        print('Harga per scoop: Rp. 20.000')
        scoop = int(input('Masukkan jumlah scoop yang diinginkan: '))
        total += scoop * 20000
        print(f"Jumlah scoop: {scoop} \n Harga: Rp. {scoop * 20000:,}")

        topping_choice = input('Pilih Topping: \n 1. Chocolate Sprinkle (Rp 6000)\n 2. Strawberry Coulis (Rp 12000)\n 3. Flake (Rp 8000)\n Masukkan pilihan topping: ')
        
        if topping_choice == '1':
            total += topping[0]['Harga ']
            print(f"{topping[0]['Jenis ']} dipilih.\n Harga: Rp. 6000")
        elif topping_choice == '2':
            total += topping[1]['Harga ']
            print(f"{topping[1]['Jenis ']} dipilih.\n Harga: Rp. 12000")
        elif topping_choice == '3':
            total += topping[2]['Harga ']
            print(f"{topping[2]['Jenis ']} dipilih.\n Harga: Rp. 8000")
        else:
            print('Pilihan tidak valid. Silahkan pilih topping yang tersedia.')
        break


    print(f"Total harga es krim: Rp. {total:,}")         
    return total

es_krim()


            
            
    
            
        
