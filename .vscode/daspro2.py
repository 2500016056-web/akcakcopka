# menu = {
#     "espresso": 50000,
#     "americano": 60000,
#     "latte": 50000,
#     "cappuccino": 60000,
#     "macchiato": 50000,
#     "mocha": 70000,
#     "flat white": 50000
# }

# ukuran = {
#     "M": 0, 
#     "L": 20000, 
#     "XL": 30000
# }

# total = 0

# jumlah = int(input("Berapa banyak cangkir yang dipesan?"))

# for i in range(jumlah):
#     print(f" Pesanan {i+1}:  ")
    
    
#     while True:
#         jenis = input("Jenis kopi: ").lower()
#         if jenis in menu:
#             break
#         print("Tidak valid!")
    
#     while True:
#         size = input("Ukuran (M/L/XL): ").upper()
#         if size in ukuran:
#             break
#         print("Tidak valid!")
    
    
#     while True:
#         takeaway = input("Take away? (Ya/Tidak): ").lower()
#         if takeaway in ["ya", "tidak"]:
#             break
#         print("Tidak valid!")
    
    
#     harga = menu[jenis] + ukuran[size]
#     if takeaway == "ya":
#         harga += 20000
    
#     total += harga
#     print(f"Harga: Rp. {harga:,}")
# print()

# print(f"Total: Rp. {total:,}")

def tulis(s,n):
    if n == 0:
        return ""
    return " " + tulis1(s, n-1)
def tulis2(s,n):
    if n == 0:
        return ""
    return  tulis2(s, n-1) + s[n-1]
def ayo