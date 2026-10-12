
total_biaya = int(input("Masukkan total biaya/investasi (USD): "))
total_penjualan = int(input("Masukkan total penjualan (USD): "))


laba = total_penjualan - total_biaya
print(f"Total Biaya: USD {total_biaya}")
print(f"Total Penjualan: USD {total_penjualan}")
print(f"Laba/Rugi: USD {laba}")

if laba > 0:
    print("Status: UNTUNG")
elif laba < 0:
    print("Status: RUGI")
else:
    print("Status: IMPAS (Break Even)")

roi = (laba / total_biaya) * 100
print(f"Return on Investment (ROI): {roi:.2f}%")
