import shelve #mengimport modul shelve
berkas = open("L200230252", "r") #membuka berkas bernama "L200230252" dalam mode baca "r"
F = shelve.open("Elma") #membuka berkas dengan modul 'shelve' dengan nama "Elma" 
                        #kemudian berkas Elma ini menyimpan data menggunakan shelve
F["nim"] = berkas.readline() #menyimpan baris pertama dari berkas "L200230252" 
                             #kedalam kunci "nim" dalam berkas 'Elma'
F["TanggalLahir"] = berkas.readline() #menyimpan baris kedua dari berkas "L200230252" 
                             #kedalam kunci "TanggalLahir" dalam berkas 'Elma'
F["nama"] = berkas.readline()  #menyimpan baris ketiga dari berkas "L200230252" 
                             #kedalam kunci "nama" dalam berkas 'Elma'
F["kota"] = berkas.readline()  #menyimpan baris keempat dari berkas "L200230252" 
                             #kedalam kunci "kota" dalam berkas 'Elma'
berkas.close() #Menutup berkas "L200230252" setelah membaca setiap baris