Waktu = ('pagi', 'siang', 'sore', 'petang', 'malam') #Variabel tuple menyimpan data tentang waktu
Nama = str(input('Masukkan nama saudara')) #Memasukkan nama dengan type data string
Jam = float(input('Pukul berapa sekarang?')) #Menggunakan type float pada variabel jam, menanyakan waktu 
if 00.01 <Jam<= 09.00:  #Kondisi ketika waktu 00.01 kurang dari sama dengan jam 09.00 menunjukkan waktu pagi
    print('Selamat ', Waktu[0], Nama) #print selamat, waktu pada indeks ke 0 yaitu pagi, 
                                      #dan pengguna memasukkan namanya
elif 09.01 <Jam <=15.00:
    print('Selamat', Waktu[1], Nama)
elif 15.01 <Jam <=17.00:
    print('Selamat', Waktu[2], Nama)
elif 17.01 <Jam <=18.00:
    print('Selamat', Waktu[3], Nama)
else:                                #Jika waktu yang dimasukkan tidak sesuai dengan data di atas maka program akan
                                     #menampilkan selamat malam
    print('Selamat', Waktu[4], Nama)