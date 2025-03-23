import shelve #mengimport modul shelve
F = shelve.open("Elma") #membuka berkas dengan modul 'shelve' dengan nama "Elma" 
                        #kemudian berkas Elma ini menyimpan data menggunakan shelve
print(F["nim"]) #mencetak isi dari kunci "nim" dalam berkas Elma. 
                #Perintah ini akan mencetak nilai yang disimpan dalam kunci tersebut.
print(F["TanggalLahir"])  #mencetak isi dari kunci "TanggalLahir" dalam berkas Elma. 
                          #Perintah ini akan mencetak nilai yang disimpan dalam kunci tersebut.
print(F["nama"]) #mencetak isi dari kunci "nama" dalam berkas Elma. 
                #Perintah ini akan mencetak nilai yang disimpan dalam kunci tersebut.
print(F["kota"])  #mencetak isi dari kunci "kota" dalam berkas Elma. 
                #Perintah ini akan mencetak nilai yang disimpan dalam kunci tersebut.
F.close() #menutup berkas Elma yang telah dibuka dengan shelve.open()