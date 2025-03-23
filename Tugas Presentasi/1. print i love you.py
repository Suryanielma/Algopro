#https://www.spoj.com/problems/ILOVEYOU

#Buatlah program untuk mencetak string "I Love you x kali", 
# #dengan x adalah variabel yang mengacu pada nilai integer.
#Memasukkan
#Inputnya hanya terdiri dari satu baris yaitu bilangan x (integer).
#Keluaran
##Cetak string berdasarkan deskripsi

x = int(input()) #meminta untuk memasukkan sebuah bilangan bulat dan 
                 #menyimpannya ke dalam variabel x.
print(f"I Love you {x} times") #mencetak pesan “I Love you” sebanyak x kali. 
#f pada awal string menandakan string tersebut adalah f-string,
#untuk memasukkan nilai variabel ke dalam string.