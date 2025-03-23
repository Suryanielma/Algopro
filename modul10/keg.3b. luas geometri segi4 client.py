import socket #mengimport socket

hostname = "localhost" #hostname menyimpan localhost
pesan = "" #variabel untuk menyimpan pesana yang akan di kirim keserver
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuka jaringan dengan membuat object socket client 
                                                      #digunakan untuk menghubungkan client ke server
s.connect((hostname, 50004)) #mengonekkan localhost dengan port ke 50004
a ='' #variabel a menyimpan nilai kosong yang nanti akan dimasukan sebuah nila random

print ("Menghitung luas segi empat") #menampilkan "menghitung luas segi empat" di awal program
while pesan.lower != "keluar":#ketika mengirimkan pesan ke server
    pesan = input("pesan :") #Meminta pengguna untuk memasukkan pesan yang akan dikirim ke server melalui input 'pesan'
    pesan = pesan.encode() #Mengonversi pesan menjadi format byte untuk dikirim melalui socket.
    s.send(pesan) #mengirim pesan
    if pesan.lower() == "keluar": #mengecek apakah pesan yang dikirim adalah "keluar".
        response = s.recv(1024) #menerima respon dari server dengan uk.1024
        print ("Response : -") #mencetak 'response dan akan menampilkan -
        s.close() #menutup pesan
        break #menghentikan loop
    elif pesan.lower() != "keluar": #jika pesan yang dikirim bukan "keluar".
        response = s.recv(1024).decode() # Menerima respons dari server dengan ukuran buffer 1024 bytes,
                                        # kemudian didecode menjadi string.
        print ("Response : ", response) #mencetak respon dari server
s.close() #menutup koneksi socket
