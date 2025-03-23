# Nama = 'Suryani Elmaghfiroh'
# NIM = 'l200230252'
# x = '1' + NIM[7:] #Menampilkan angka 1 dan NIM indeks ke 7 sampai selesai
# a = int(x) #konversi string ke integer
# b = len(Nama) #Menghitung banyaknya data pada variabel nama

# c = 12.5 #variabel c menyimpan data 12.5
# c > b #(>) lebih dari,  data c 12.5 lebih besar dari data b 19 
# type (c > b) #Menampilkan type data c > b
# a > b and b > c # (AND)merupakan operator logika perbandingan nilai true and false
# #data a yaitu 1252 lebih besar dari data b 19 dan data b 19 lebih besar dari data c 12.5
# a > 1100 or b < 10 # (OR)merupakan operator logika perbandingan nilai true and false
# #data a 1252 lebih besar dari 1100 atau data b 19 kurang dari 10


Nama = 'Suryani Elmaghfiroh'
NIM = 252
Tinggi = 1.63
Berat = 52
TahunLahir = 2005
Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)  #tanda kurung artinya type tuple datanya tidak bisa dirubah
Data = [TahunLahir, Berat, Tinggi, NIM, Nama] #tanda kurung siku termasuk type list artinya datanya bisa dirubah
print(type(Aku)) #menampilkan type dari data variabel Data yaitu [TahunLahir, Berat, Tinggi, NIM, Nama]
print(type(Aku[0])) #menampilkan type dari data variabel Data indeksing ke 4 yaitu Nama
a = NIM % 4 ; Aku[a]
print(type(Aku[a]))
print(Aku[a:4]) #data indeks ke 4 yaitu nama di slicing indek ke a yg tadi hasilnya 0 sampai indeks ke sebelum 6 yaitu 5
print(type(Aku[4]))
# Aku[0] = 'ok'
print(type(Data)) #menampilkan type dari data variabel Data yaitu [TahunLahir, Berat, Tinggi, NIM, Nama]
print(type(Data[4])) #menampilkan type dari data variabel Data indeksing ke 4 yaitu Nama
print(Data[4][5]) #Menampilkan data indeks 4 yaitu nama dan indeks ke 5 di dalam nama 
print(Data[4][a:6]) #data indeks ke 4 yaitu nama di slicing indek ke a yg tadi hasilnya 0 sampai indeks ke sebelum 6 yaitu 5
Data[0] = 'ok'; Data #data ke 0 yaitu 2005 pada data list dirubah menjadi 'ok'
print(Data[-a]) #Menampilkan data list indeks ke -0 
print(range(a)) #range merupakan deret angka dari variabel a