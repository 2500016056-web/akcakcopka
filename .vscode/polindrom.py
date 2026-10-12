

kata = input("Masukkan kata: ")
panjang = len(kata)

polindrom = True
for i in range(panjang):
    if kata[i] != kata[panjang - 1 - i]:
        polindrom = False
        break

if polindrom:
    print("Kata tersebut adalah POLINDROM")
else:
    print("Kata tersebut BUKAN polindrom")
    
    