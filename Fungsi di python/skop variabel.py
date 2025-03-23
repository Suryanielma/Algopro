# prodi = "Informatika"
 
# def isiKRS(nim):
#     pesanKRS = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mengisi KRS"
#     print(pesanKRS)
#     return None
 
# def cetakKHS(nim):
#     pesanKHS = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mencetak KHS"
#     print(pesanKHS)
#     return None
 
# isiKRS("ST001")
# cetakKHS("ST001")

#Pada kode diatas, terdapat variable lokal pesanKRS dan pesanKHS.
#  Variabel pesanKRS didefinisikan di fungsi isiKRS dan
#  hanya dapat diakses pada fungsi isiKRS saja. Sama halnya dengan, Variabel pesanKHS didefinisikan di fungsi cetakKHS dan
#  hanya dapat diakses pada fungsi cetakKHS saja.



# #Nah, jika kita menuliskan kode seperti di bawah ini maka akan terjadi error 
# # karena variabel pesanKRS tidak dapat diakses diluar fungsi yang mendefinisikannya, 
# # yaitu fungsi isiKRS. 
# prodi = "Informatika"
 
# def isiKRS(nim):
#     pesanKRS = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mengisi KRS"
#     print(pesanKRS)
#     return None

# def cetakKHS(nim):
#     pesanKHS = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mencetak KHS"
#     print(pesanKHS)
#     print(pesanKRS)
#     return None
 
# isiKRS("ST001")
# cetakKHS("ST001")



prodi = "Informatika"
 
def isiKRS(nim):
    pesan = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mengisi KRS"
    print(pesan)
    return None
 
def cetakKHS(nim):
    pesan = "Mahasiswa prodi " + prodi + " dengan NIM: " + nim + " telah mencetak KHS"
    print(pesan)
    return None
 
isiKRS("ST001")
cetakKHS("ST001")