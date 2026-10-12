# #Program Sistem Bioskop
# film = [
#     {"ID": "F001","Judul": "Avengers: Endgame", "Genre": "Action", "Durasi": 181, "Kursi": 29, "Harga/Tiket": 50000, "Status": "Tayang"},
#     {"ID": "F002","Judul": "Spider-Man: No Way Home", "Genre": "Action", "Durasi": 148,"Kursi": 25, "Harga/Tiket": 55000, "Status": "Tayang"},
#     {"ID": "F003","Judul": "Frozen II", "Genre": "Animation", "Durasi": 103, "Kursi": 20, "Harga/Tiket": 40000,"Status": "Tayang"},
#     {"ID": "F004","Judul": "Sore", "Genre": "Fantasy", "Durasi": 95,"Kursi": 18, "Harga/Tiket": 45000, "Status": "Tayang"},        
# ]

# pemesanan_tiket = []

# while True:
#     print("=== SELAMAT DATANG DI BIOSKOP XXI ===")
#     print("1. Tampilkan Film")
#     print("2. Cari Film")
#     print("3. Pesan Tiket")
#     print("4. Batalkan Tiket")
#     print("5. Laporan")
#     print("6. Keluar")
    
#     pilihan = input('Masukkan pilihan Anda: ')
    
#     if pilihan == '1':
#         for item in film:
#             for key, value in item.items():
#                 print(f"{key}: {value}")
#             print('-' * 20)
#     elif pilihan == '2':
#         cari_judul = input('Masukkan judul film yang ingin Anda cari: ')
#         print('===== HASIL PENCARIAN =====')
#         ketemu = False
#         for f in film:
#             if cari_judul.lower() in f["Judul"].lower():
#                 ketemu = True
#                 print('Film ditemukan:')
#                 print(f"ID: {f['ID']}")
#                 print(f"Judul: {f['Judul']}")
#                 print(f"Genre: {f['Genre']}")
#                 print(f"Durasi: {f['Durasi']} menit")
#                 print(f"Kursi Tersedia: {f['Kursi']}")
#                 print(f"Harga/Tiket: Rp {f['Harga/Tiket']}")
#                 print(f"Status: {f['Status']}")
#                 print('-' * 20)
#         if not ketemu:
#             print("Film tidak ditemukan.")
#     elif pilihan == '3':
#         nama_penonton = input('Masukkan nama Anda: ')
#         film_id = input('Masukkan ID Film yang ingin Anda tonton: ').upper()
#         for f in film:
#             if f['ID'] == film_id:
#                 if f['Kursi'] > 0:
#                     pemesanan_tiket.append(
#                         {
#                             'nama_penonton': nama_penonton,
#                             'film_id': film_id,
#                             'film_judul': f['Judul'],
#                             'harga': f['Harga/Tiket']   
#                         }
#                     )
#                     f['Kursi'] -= 1
#                     print(f'Tiket berhasil dipesan untuk {f["Judul"]} dengan Harga: Rp {f["Harga/Tiket"]}') 
#                 else:
#                     print('Maaf, Kursi untuk film ini sudah penuh.')
#     elif pilihan == '4':
#         nama_penonton = input('Masukkan nama Anda: ')
#         film_id = input('Masukkan ID Film yang ingin Anda batalkan: ').upper()
#         ditemukan = False
#         for p in pemesanan_tiket:
#             if p['nama_penonton'] == nama_penonton and p['film_id'] == film_id:
#                 pemesanan_tiket.remove(p)
#                 for f in film:
#                     if f['ID'] == film_id:
#                         f['Kursi'] += 1
#                         break
#                 print(f'Tiket untuk {p["film_judul"]} berhasil dibatalkan.')
#                 ditemukan = True
#                 break
#         if not ditemukan:
#             print('Tiket tidak ditemukan untuk dibatalkan.')
#     elif pilihan == '5':
#         print('====== LAPORAN PEMESANAN TIKET ======')
#         for p in pemesanan_tiket:
#             print(f"Nama Penonton: {p['nama_penonton']}")
#             print(f"Film: {p['film_judul']}")
#             print(f"Harga: Rp {p['harga']}")
#             print('-' * 20)
#     elif pilihan == '6':
#         print("Terima kasih telah menggunakan layanan kami!")
#         break



# Buatkan kode untuk mengestimasi biaya perjalanan dengan jumlah peserta tertentu
# dengan kapasitas bus:
# bus besar : kapasitas 46, sewa/hari : 300000
# bus kecil : kapasitas 16, sewa/hari : 140000
# peserta = 250
# pendamping 7

# peserta = 300
# pendamping = 10

# peserta = 350
# pendamping 12

largebuses = int(input('Masukkan berapa bus besar yang disewa: '))
smallbuses = int(input('Masukkan berapa bus kecil yang disewa: '))

total_biaya = 0

students = int(input('Masukkan jumlah peserta: '))
teachers = int(input('Masukkan jumlah pendamping: '))

participants = students + teachers

print(f"Total murid dan pendamping: {participants} orang")
print()
largebuses = participants // 46
print(f"Number of largebuses: {largebuses}")
print()
reminder = participants % 46

smallbuses = reminder // 16

reminder = reminder // 16

if reminder > 0:
    smallbuses += 1
    print(f'Number of smallbuses: {smallbuses}')

    total_biaya = largebuses * 300000 + smallbuses * 140000
    print(f"Total biaya sewanya adalah: Rp. {total_biaya:,}")
