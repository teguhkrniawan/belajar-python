# IF ELSE STATEMENT

print("PILIH OPERATOR BERIKUT, DENGAN KETIKKAN ANGKA")
print("1. TAMBAH")
print("2. KURANG")

pilihan_user = int(input("PILIHAN SAYA :\t"))

if pilihan_user > 2:
        print("TIDAK ADA PILIHAN TERSEBUT")
if pilihan_user == 1:
        angka1 = int(input("ANGKA 1 : "))
        angka2 = int(input("ANGKA 2 : "))
        result = angka1 + angka2
        print("HASIL TAMBAH : ", result)
if pilihan_user == 2:
        angka1 = int(input("ANGKA 1 : "))
        angka2 = int(input("ANGKA 2 : "))
        result = angka1 - angka2
        print("HASIL KURANG : ", result)