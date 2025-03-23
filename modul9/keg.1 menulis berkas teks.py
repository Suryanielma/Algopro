#Membuat berkas dengan nama nim
berkas = open("L200230252", "w") #membuka berkas bernama "L200230252" dengan mode "w" berkas diakses untuk menyimpan data
berkas.write("L200230252\n") #menulis type data string yaitu L200230252 ke dalam berkas pada baris pertama
                             #simbol \n digunakan agar isi berkas ketika di run tampilannya per baris aatau bias juga
                            #menampilkan baris baru
berkas.write("10-02-2005\n") #menulis type data string 10-02-2005 ke dalam berkas pada baris ke dua
berkas.write("Suryani Elmaghfiroh\n") #menulis type data string yaitu Suryani Elmaghfiroh ke dalam berkas pada baris ketiga
berkas.write("Koto Tinggi\n") #menulis type data string yaitu Koto Tinggi ke dalam berkas pada baris ke empat
berkas.close() #menutup berkas