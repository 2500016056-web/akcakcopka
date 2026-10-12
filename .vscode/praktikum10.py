# Program Pemesanan Tiket Kereta Api

# Data kereta
kereta = [
    {"id": "K001", "nama": "Argo Bromo", "asal": "Jakarta", "tujuan": "Surabaya", "kursi": 50, "harga": 350000},
    {"id": "K002", "nama": "Bima", "asal": "Jakarta", "tujuan": "Yogyakarta", "kursi": 40, "harga": 250000},
    {"id": "K003", "nama": "Taksaka", "asal": "Yogyakarta", "tujuan": "Jakarta", "kursi": 45, "harga": 260000},
    {"id": "K004", "nama": "Gajayana", "asal": "Jakarta", "tujuan": "Malang", "kursi": 35, "harga": 380000}
]

pemesanan = []

print("="*55)
print("       SISTEM PEMESANAN TIKET KERETA API")
print("="*55)

lanjut = True
while lanjut:
    print("\n[1] Tampilkan Kereta")
    print("[2] Cari Kereta")
    print("[3] Pesan Tiket")
    print("[4] Laporan")
    print("[5] Keluar")
    
    menu = input("\nMasukkan pilihan: ")
    
    if menu == "1":
        print("\n" + "="*55)
        print("              DAFTAR KERETA API")
        print("="*55)
        for k in kereta:
            print(f"\nID    : {k['id']}")
            print(f"Nama  : {k['nama']}")
            print(f"Rute  : {k['asal']} → {k['tujuan']}")
            print(f"Kursi : {k['kursi']} tersedia")
            print(f"Harga : Rp {k['harga']:,}")
            print("-"*55)
    
    elif menu == "2":
        print("\n[1] Cari berdasarkan kota asal")
        print("[2] Cari berdasarkan kota tujuan")
        opsi = input("Pilihan: ")
        
        if opsi == "1":
            kota = input("Masukkan kota asal: ")
            print("\n--- Hasil Pencarian ---")
            ada = False
            for k in kereta:
                if k['asal'].lower() == kota.lower():
                    print(f"{k['id']} | {k['nama']} → {k['tujuan']} | Rp {k['harga']:,}")
                    ada = True
            if ada == False:
                print("Tidak ada kereta dari kota tersebut")
        
        elif opsi == "2":
            kota = input("Masukkan kota tujuan: ")
            print("\n--- Hasil Pencarian ---")
            ada = False
            for k in kereta:
                if k['tujuan'].lower() == kota.lower():
                    print(f"{k['id']} | {k['nama']} dari {k['asal']} | Rp {k['harga']:,}")
                    ada = True
            if ada == False:
                print("Tidak ada kereta ke kota tersebut")
    
    elif menu == "3":
        print("\n--- Pemesanan Tiket ---")
        nama = input("Nama penumpang: ")
        id_cari = input("ID kereta: ").upper()
        
        ada = False
        for k in kereta:
            if k['id'] == id_cari:
                ada = True
                
                if k['kursi'] == 0:
                    print("\nMaaf, kursi sudah habis!")
                else:
                    jml = int(input("Jumlah tiket (max 2): "))
                    
                    if jml < 1 or jml > 2:
                        print("\nJumlah tiket harus 1 atau 2!")
                    elif jml > k['kursi']:
                        print(f"\nKursi tersisa hanya {k['kursi']}!")
                    else:
                        bayar = k['harga'] * jml
                        k['kursi'] = k['kursi'] - jml
                        
                        pemesanan.append({
                            "nama": nama,
                            "kereta": k['nama'],
                            "jml": jml,
                            "bayar": bayar
                        })
                        
                        print("\n" + "="*55)
                        print("        ✓ PEMESANAN BERHASIL!")
                        print("="*55)
                        print(f"Nama     : {nama}")
                        print(f"Kereta   : {k['nama']}")
                        print(f"Rute     : {k['asal']} → {k['tujuan']}")
                        print(f"Tiket    : {jml} buah")
                        print(f"Total    : Rp {bayar:,}")
                        print("="*55)
                break
        
        if ada == False:
            print("\nID kereta tidak ditemukan!")
    
    elif menu == "4":
        if len(pemesanan) == 0:
            print("\nBelum ada transaksi.")
        else:
            jml_tiket = 0
            pendapatan = 0
            
            for p in pemesanan:
                jml_tiket = jml_tiket + p['jml']
                pendapatan = pendapatan + p['bayar']
            
            # Hitung kereta terlaris
            hitung = {}
            for p in pemesanan:
                if p['kereta'] in hitung:
                    hitung[p['kereta']] = hitung[p['kereta']] + p['jml']
                else:
                    hitung[p['kereta']] = p['jml']
            
            terlaris = ""
            terbanyak = 0
            for nama_kereta in hitung:
                if hitung[nama_kereta] > terbanyak:
                    terbanyak = hitung[nama_kereta]
                    terlaris = nama_kereta
            
            print("\n" + "="*55)
            print("            LAPORAN PENJUALAN")
            print("="*55)
            print(f"Jumlah transaksi : {len(pemesanan)}")
            print(f"Tiket terjual    : {jml_tiket}")
            print(f"Total pendapatan : Rp {pendapatan:,}")
            print(f"Kereta terlaris  : {terlaris} ({terbanyak} tiket)")
            print("="*55)
    
    elif menu == "5":
        print("\nTerima kasih telah menggunakan layanan kami!")
        lanjut = False
    
    else:
        print("\nMenu tidak valid!")
    
    if lanjut:
        input("\nTekan Enter...")

print("\n>>> Program selesai <<<\n")