import socket

hostname = "localhost"
pesan = "" #variabel untuk menyimpan pesana yang akan di kirim keserver
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuka jaringan dengan membuat object socket client 
                                                      #digunakan untuk menghubungkan client ke server
s.connect((hostname, 50004)) #mengonekkan localhost dengan port ke 50004

while pesan.lower() != "quit": #ketika mengirimkan pesan ke server
    pesan = input("Command : ") #Meminta pengguna untuk memasukkan pesan yang akan dikirim ke server melalui input pada command
    pesan = pesan.encode() #Mengonversi pesan menjadi format byte untuk dikirim melalui socket.
    s.send(pesan) #mengirim pesan
    if pesan.lower() != "quit":#mengecek apakah pesan yang dikirim adalah "quit".
        response =  s.recv(1024) #menerima respon dari server dengan uk.1024
        response = response.decode() #Mengonversi respons dari byte ke string 
                                    #menggunakan metode decode() agar dapat dibaca.
        print ("response : ", response) #mencetak respone
s.close #menutup koneksi
