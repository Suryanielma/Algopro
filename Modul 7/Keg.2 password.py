# Kesempatan = 1 #merupakan jumlah kesempatan yang akan digunakan saat memasukkan password
# for i in range(3): #Perulangan sebanyak 3 kali, hanya memiliki 3 kesempatan untuk memasukkan password yang benar
#     password = str(input('Masukkan Passowrd')) #Memasukkan password dengan type string
#     Kesempatan +=1 #Kesempatan akan bertambah 1 kali ketika pengguna memasukkan password
#     if password == 'Elma': #Memasukkan password yang akan dibuat
#         print('Anda berhasil login') #Jika password yang dimasukkan benar akan muncuk tampilan anda berhasil login
#         break #untuk menghentikan program
#     elif Kesempatan >3: # Jika kesempatan sudah lebih dari 3, print tampilan "akses anda ditolak"
#         print('Anda telah mencoba 3 kali. Akses anda ditolak')
#     else : #Jika memasukkan password yang berbeda akan muncul tampilan "Maaf, anda salah memasukkan password"
#          print('Maaf, anda salah memasukkan password ')
  

Kesempatan = 1
for i in range (3):
    Kesempatan +=1
    Pasword = str(input("masukkan password"))
    if Pasword == 'elma':
        print('login')
        break
    elif Kesempatan >3:
        print("ditolak")
    else:
        print("coba")