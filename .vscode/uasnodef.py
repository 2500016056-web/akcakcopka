container = [
    {'Jenis': 'Cup', 'Harga': 10000}, #50
    {'Jenis': 'Cone', 'Harga': 16000}, #80
]

topping = [
    {'Jenis': 'Chocolate Sprinkle', 'Harga': 6000}, #30
    {'Jenis': 'Strawberry Coulis', 'Harga': 12000}, #60
    {'Jenis': 'Flake', 'Harga': 8000}, #40
]

total = 0


while True:
    pilihan_cup = input('Pilih Wadah Es Krim (Cup/Cone): ')
    if pilihan_cup.lower() == 'cup':
        total += container[0]['Harga']
        print(f"Wadah Cup dipilih.")
        print(f"Harga: Rp. {container[0]['Harga']:,}")
    elif pilihan_cup.lower() == 'cone':
        total += container[1]['Harga']
        print(f"Wadah Cone dipilih.")
        print(f"Harga: Rp. {container[1]['Harga']:,}")
    else:
        print('Pilihan tidak valid. Silahkan pilih wadah yang tersedia.\n')
        
    
    print('Harga per scoop: Rp 20.000') #100
    scoop = int(input('Masukkan jumlah scoop yang diinginkan: '))
    total += scoop * 20000 
    print(f"Jumlah scoop: {scoop}")
    print(f"Harga: Rp {scoop * 20000:,}")

    
    print('1.Chocolate Sprinkle > Rp. 6000')
    print('2.Strawberry Coulis > Rp. 12000')
    print('3.Flake > Rp. 8000')
    print('4.Tidak pakai topping')

    pilihan_topping = input('Masukkan pilihan topping: ')

    if pilihan_topping == '1':
        total += topping[0]['Harga']
        print(f"{topping[0]['Jenis']} dipilih.")
        print(f"Harga: Rp {topping[0]['Harga']:,}")
    elif pilihan_topping == '2':
        total += topping[1]['Harga']
        print(f"{topping[1]['Jenis']} dipilih.\nHarga: Rp {topping[1]['Harga']:,}\n")
    elif pilihan_topping == '3':
        total += topping[2]['Harga']
        print(f"{topping[2]['Jenis']} dipilih.\nHarga: Rp {topping[2]['Harga']:,}\n")
    elif pilihan_topping == '4':
        print('Tidak pakai topping\n')
    else:
        print('Pilihan tidak valid. Silahkan pilih topping yang tersedia.\n')
        
    break

print(f"Total harga es krim: Rp {total:,} ") 