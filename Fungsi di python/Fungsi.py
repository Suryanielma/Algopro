# print("Hi Albert")
# print("Nice to see you!")

# print("Hi Bryan")
# print("Nice to see you!") 

# print("Hi Charlie")
# print("Nice to see you!") 


# def greetAlbert(): #Penggunaan fungsi pda greetAlbert
#    print("Hi Albert")
#    print("Nice to see you!")

# def greetBryan():
#    print("Hi Bryan")
#    print("Nice to see you!")

# def greetCharlie():
#    print("Hi Charlie")
#    print("Nice to see you!")

# print(greetAlbert()) #memanggil program greetAlbert hasilnya akan none karena tidak ad anilai kembalian
# greetAlbert()


# produk = ["kemeja", "sepatu", "celana", "kaos", "topi"] #list Ada 5 elemen 
 
# def elemenAwalAkhirProduk(): # nama fungsi elemenawalkkhirproduk mengembalikan sebuah nilai harus menggunakan return
#    """Mengembalikan elemen awal dan akhir dari list produk"""
#    return [produk[0], produk[len(produk)-1]] #mencetak hsilnya #return bisa diubah apa saja

# print(elemenAwalAkhirProduk()) #memanggil kunci dan di print kembali ada  nilainyai


# def luasSegitiga(alas, tinggi):
#    """Mengembalikan luas segitiga dengan dengan input alas dan tinggi"""
#    luas = 0.5 * alas * tinggi
#    return luas 3mengembalikan nilai
# print(luasSegitiga(5,10)) #tidak megembalikan nilai /none
# #JIKA SUATU FUNGSI TIDAK MEMILIKI RETURN ARTINYA TIDAK MEMILIKI OUTPUT


# def luas_segi4(pj, lb):
#     """ mengembalikan luas segi empat dengan panjang pj dan lebar lb """
#     luas = pj * lb #dimasukkan kedalam variabel luas
#     return luas

# p = 4.5
# l = 3.5
# luas = luas_segi4(p, l) #memanggil fungsi def dari luas_segi4 dan memasukkan nilai p l
# print("Luas segi empat dengan panjang", p, "dan lebar", l, "adalah", luas)


# def kel_ling(r): #fungsi mengitung keliling lingkaran 
#     """ mengembalikan keliling lingkaran yang berjari-jari r """
#     pi = 3.14159
#     return 2 * pi * r
# kl = kel_ling(10)
# print(kl)

# def luasLingkaran(r): #fungsi mengitung keliling lingkaran 
#     """ mengembalikan keliling lingkaran yang berjari-jari r """
#     pi = 3.14159
#     return pi * r ** 2
# ls = luasLingkaran(20)
# print(ls)

# def luasLingkaran(r=7): #default nilai, jika tidak memasukkan nilai maka yg dipakai angka 7 
#     """ mengembalikan keliling lingkaran yang berjari-jari r """
#     pi = 3.14159
#     return pi * r ** 2
# ls = luasLingkaran() #statemennya kosong
# print(ls)


# def infoMhs(namaDepan, namaBelakang=""): 
#    return "Nama : "+ str(namaDepan) + " " + str(namaBelakang) #tanda petik 2 untuk spasi jarak nama pertama dan kedua

# print(infoMhs("Andi", "Setiawan"))
# print(infoMhs("Budianto"))


# def infoMhs(nim, alamat, namaDepan, namaBelakang = ""): #parameter defoltnya (="") harus di letakkan di belakang
#     return "Nama : " + str(namaDepan) + " " + str(namaBelakang) + ", NIM: " + nim + ", Alamat: " + alamat 

# print(infoMhs("ST001", "Solo", "Andi", "Setiawan"))
# print(infoMhs("ST002", "Jogja", "Budi"))


 #jjika yang di print tidak sesuai urutan return bisa memasukkan parameter pada key seperti nama= nim=
# def infoMhs(nim, alamat, namaDepan, namaBelakang = ""): #parameter defoltnya (="") harus di letakkan di belakang
#     return "Nama : " + str(namaDepan) + " " + str(namaBelakang) + ", NIM: " + nim + ", Alamat: " + alamat 

# print(infoMhs(nim="ST001", alamat="Solo", namaDepan="Andi", namaBelakang="Setiawan"))
# print(infoMhs(nim="ST002", alamat="Jogja", namaDepan="Budi"))
# print(infoMhs(namaDepan="Elma", nim="l200230252", alamat="bumiayu", namaBelakang="firoh"))