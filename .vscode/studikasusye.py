#Program Rental Mobil
mobil = [
    {"ID": "M001", "Merk/Tipe": "Toyota Avanza", "Tahun": 2019, "Harga/Hari": 250000, "Status": "Tersedia"},
    {"ID": "M002", "Merk/Tipe": "Honda Jazz", "Tahun": 2022, "Harga/Hari": 300000, "Status": "Tersedia"},
    {"ID": "M003", "Merk/Tipe": "Toyota Innova", "Tahun": 2020, "Harga/Hari": 400000, "Status": "Tersedia"},
    {"ID": "M004", "Merk/Tipe": "Toyota Fortuner", "Tahun": 2023, "Harga/Hari": 500000, "Status": "Tidak Tersedia"},
    {"ID": "M005", "Merk/Tipe": "Honda CR-V", "Tahun": 2021, "Harga/Hari": 250000, "Status": "Tersedia"},

]

pesanan_rental = []

while True:
    print('===== SELAMAT DATANG DI RENTAL PICES =====')
    print('1. Lihat Daftar Mobil')
    print('2. Tipe Mobil')
    print('3. Sewa Mobil')
    print('4. Kembalikan Mobil')
    print('5. Laporan')
    print('6. Keluar')

    pilihan = int(input('Masukkan pilihan Anda: '))

    if pilihan == 1:
        print('===== DAFTAR MOBIL =====')
        for item in mobil:
            for key, value in item.items():
                print(f"{key}: {value}")
            print('-' * 20)
           
        
    
    elif pilihan == 2:
        cari_mobil = input('Masukkan tipe mobil yang ingin Anda cari: ')
        print('===== HASIL PENCARIAN =====')
        ketemu = False
        for c in mobil:
            if cari_mobil.lower() in c["Merk/Tipe"].lower():
                ketemu = True
                print('Mobil ditemukan:')
                print(f"ID: {c["ID"]} ")
                print(f"Merk/Tipe: {c["Merk/Tipe"]} ")
                print(f"Tahun: {c["Tahun"]} ")
                print(f"Harga/Hari: {c["Harga/Hari"]} ")
                print(f"Status: {c["Status"]} ")
                print('-' * 20)
        
    elif pilihan == 3:
        nama_customer = input('Masukkan nama Anda: ')
        tipe_mobil = input('Masukkan tipe mobil yang ingin dipakai: ')
       
        ketemu = False

        for m in mobil:
            if tipe_mobil.lower() in m["Merk/Tipe"].lower():
            
                ketemu = True
                if m["Status"] == "Tersedia":
                    hari = int(input('Lama sewa (hari): '))
                    total = hari * m['Harga/Hari']
                    
                    pesanan_rental.append({
                        'nama': nama_customer,
                        'mobil': m['Merk/Tipe'],
                        'id_mobil': m['ID'],
                        'hari': hari,
                        'total': total
                    })
                    
                    m['Status'] = 'Tidak Tersedia'
                    print(f'Berhasil sewa {m["Merk/Tipe"]}!')
                    print(f'Total: Rp {total:,}')
                else:
                    print(f'Maaf, {m["Merk/Tipe"]} tidak tersedia')

                    
    elif pilihan == 4:
        id_mobil_kembali = input('Masukkan ID mobil yang dikembalikan: ').upper()
        for m in mobil:
            if m["ID"] == id_mobil_kembali:
                if m["Status"] == "Tidak Tersedia":
                    m["Status"] = "Tersedia"
                    print(f"Mobil {m["Merk/Tipe"]} telah dikembalikan. Terima Kasih!")
                else:
                    print(f"Mobil {m['Merk/Tipe']} belum dikembalikan.")
       
    elif pilihan == 5:
        print("===== Laporan Penyewaan Mobil ====")
        for p in pesanan_rental:
            print(f"Nama Customer: {p['nama']}")
            print(f"Mobil: {p['mobil']}")
            print(f"Lama Sewa: {p['hari']} hari")
            print(f"Total Bayar: Rp {p["total"]}")
    elif pilihan == 6:
        print('Terima kasih telah menggunakan layanan Rental Pices.')
        exit()
        break
    
            
    

        