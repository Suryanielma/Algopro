# def kali(a, b):
#    return a*b

# hasilKali = kali(10, 5)
# print(hasilKali)


# def kali(*deret):
#    hasilKali = 1
#    for nilai in deret:
#       hasilKali *= nilai
#    return hasilKali

# a = kali(1, 2)
# b = kali(1, 2, 3)
# c = kali(1, 2, 3, 5)

# print(a)
# print(b)
# print(c)


# def cetak(*produk):
#     for item in produk:
#         print("Nama produk: " + item)

# cetak("buku", "pensil", "penggaris")




def cetakkey(**produk):
   print(produk)

cetakkey(namaProduk="buku", jumlah="2")
cetakkey(namaProduk="pensil", jumlah="5")
cetakkey(namaProduk="penggaris", jumlah="3")