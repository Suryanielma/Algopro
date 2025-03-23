Nama = 'Suryani Elmaghfiroh'
NIM = 'l200230252'
x = '1' + NIM[7:] #Menampilkan angka 1 dan NIM indeks ke 7 sampai selesai
a = int(x) #konversi string ke integer
b = len(Nama) #Menghitung banyaknya data pada variabel nama

c = 12.5 #variabel c menyimpan data 12.5
c > b #(>) lebih dari,  data c 12.5 lebih besar dari data b 19 
type (c > b) #Menampilkan type data c > b
a > b and b > c # (AND)merupakan operator logika perbandingan nilai true and false
#data a yaitu 1252 lebih besar dari data b 19 dan data b 19 lebih besar dari data c 12.5
a > 1100 or b < 10 # (OR)merupakan operator logika perbandingan nilai true and false
#data a 1252 lebih besar dari 1100 atau data b 19 kurang dari 10
print(c > b)
print(type(c > b))
print(a > b and b > c)
print(a > 1100 or b < 10)