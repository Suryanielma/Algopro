#https://www.spoj.com/problems/SMPWOW
#Diberikan bilangan bulat positif 0 < x < 50.
#Keluaran
#Cetak satu kata: Wo...ow (huruf o harus diulang sebanyak x kali).

x = int(input()) #meminta untuk memasukkan sebuah bilangan bulat dan 
                 #menyimpannya ke dalam variabel x.

if 0 < x < 50: #Melakukan validasi terhadap nilai x. 
            #memeriksa apakah x berada di antara 0 dan 50 
    result = "W" + "o" * x + "w" # mencetak pesan “Wo…ow” sebanyak x kali, 
                                 #dengan tambahan huruf “W” di awal dan huruf “w” di akhir.
    print(result) #mencetak hasilnya
else: #jika x yang dimasukkan tidak memenuhi batasan (0 sampai 50)
    print("Bilangan melewati limit") #akan mencetak tulisan tersebut
































# def print_wow(x):
#     wow = "W" + "o" * x + "w"
#     print(wow)

# # Input
# x = int(input("Masukkan bilangan bulat positif (0 < x < 50): "))
# print_wow(x)

# #mencetak hurruf o