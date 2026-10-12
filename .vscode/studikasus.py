#Program Sistem Klinik Sederhana

dokter = [
    {"ID": "D001", "nama": "Dr. Andi", "spesialis": "Umum", "Kuota": 20, "Biaya": 100000},
    {"ID": "D002", "nama": "Dr. Budi", "spesialis": "Gigi", "Kuota": 15, "Biaya": 150000},
    {"ID": "D003", "nama": "Dr. Citra", "spesialis": "THT", "Kuota": 10, "Biaya": 200000},
    {"ID": "D004", "nama": "Dr. Dedi", "spesialis": "Kulit", "Kuota": 12, "Biaya": 180000},
]

pemesanan = []

while True:
    print('=== SELAMAT DATANG DI KLINIK PICES ===')
    print('1. Tampilkan Dokter')
    print('2. Cari Dokter')
    print('3. Janji Temu')
    print('4. Laporan')
    print('5. Keluar')
  
    pilihan = input('Masukkan pilihan Anda: ')
    if pilihan =='1':
        print('===== DAFTAR DOKTER =====')
        for d in dokter:
            print(f'ID: {d["ID"]}')
            print(f'Nama: {d["nama"]}')
            print(f'Spesialis: {d["spesialis"]}')
            print(f'Kuota: {d["Kuota"]}')
            print(f'Biaya: {d["Biaya"]}')
            print('-'*20)
    elif pilihan == '2':
        cari_spesialis = input('Masukkan spesialis dokter yang dicari: ')
        print('===== HASIL PENCARIAN =====')
        for d in dokter:
            if d['spesialis'].lower() == cari_spesialis.lower():
                print(f'ID: {d["ID"]}')
                print(f'Nama: {d["nama"]}')
                print(f'Spesialis: {d["spesialis"]}')
                print(f'Kuota: {d["Kuota"]}')
                print(f'Biaya: {d["Biaya"]}')
                print('-'*20)
    elif pilihan == '3':
        nama_pasien = input('Masukkan nama Anda: ')
        dokter_id = input('Masukkan ID Dokter yang ingin Anda temui: ').upper()
        for d in dokter:
            if d['ID'] == dokter_id:
                if d['Kuota'] > 0:
                    pemesanan.append(
                        {
                            'nama_pasien': nama_pasien,
                            'dokter_id': dokter_id,
                            'dokter_nama': d['nama'],
                            'biaya': d['Biaya']   
                        }
                    )
                    d['Kuota'] -= 1
                    print(f'Janji temu berhasil dibuat dengan {d['nama']} dan Biaya: {d['Biaya']}') 
                else:
                    print('Maaf, Kuota dokter sudah penuh.')
    elif pilihan == '4':
        print('====== LAPORAN PEMESANAN ======')
        for p in pemesanan:
            print(f"Nama Pasien: {p['nama_pasien']}")
            print(f"Dokter: {p['dokter_nama']}")
            print(f"Biaya: {p['biaya']}")
            print('-' * 20)
            break
         
    else:
        print('Terima kasih telah menggunakan sistem kami.')
        break