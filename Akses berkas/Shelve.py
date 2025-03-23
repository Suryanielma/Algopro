import shelve
f = shelve.open("/Users/Documents/rak.data")
f["produk"] = ["sepatu", "tas", "dompet"] #menyimpan data
f["merk"] = ("Buccheri", "Gucci", "Coach")
f["harga"] = [500000, 850000, 350000]
f.close() # menutup berkas

f = shelve.open("/Users/Documents/rak.data")  # membuka berkas
print("Produk:", f["produk"])  # membaca data
print("Harga:", f["harga"])  # akses data mirip Dictionary
print("Merk:", f["merk"])  # tidak harus urut

print(f["merk"][2])
f.close()