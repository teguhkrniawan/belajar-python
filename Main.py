# program list buku

list_buku = []
while True:
    print("Masukkan data buku")
    judul = input("Judul Buku\t: ")
    penulis = input("Nama Penulis\t: ")

    buku_item = [judul, penulis]
    list_buku.append(buku_item)

    print("====================")
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    is_lanjut = input("lanjut input ? [Y/N] : \t")
    if(is_lanjut == 'n' or is_lanjut == 'N'):
            break