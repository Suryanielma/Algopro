berkas = open("L200230252", "r") #membuka berkas bernama "L200230252" dengan mode "r" untuk mmembaca berkas datanya
nim = berkas.readline() #nim = berkas.readline digunakan untuk membaca baris pertama pada berkas teks yang sudah dibuat, 
                                #kemudian disimpan pada variabel nim
TanggalLahir = berkas.readline() #membaca baris kedua dari berkas teks dan disimpan kedalam variabel TanggalLahir
nama = berkas.readline() #membaca baris ketiga dari berkas teks dan disimpan kedalam variabel nama
kota = berkas.readline() #membaca baris keempat dari berkas teks dan disimpan kedalam variabel kota
print(nama) #menampilkan isi dari variabel nama dari berkas 
print(kota +","+ TanggalLahir) #menampilkan isi data dari variabel kota ditambah tanda koma (,)
                              # ditambah dengan isi data variabel TanggalLahir dari berkas teks
print(nim) #menampilkan isi data variabel nim dari berkas 
berkas.close() #menutup berkas