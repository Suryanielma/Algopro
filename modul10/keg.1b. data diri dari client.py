#nama berkas: p_tcpser.py
#TCP server untuk client p_tcpcli.py
import socket #mengimport modul socket

hostname = 'localhost' #hostname menyimpan localhost
pesan = '' #variabel untuk menyimpan pesana yang akan di kirim keserver

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuka jaringan dengan membuat object socket client 
                                                      #digunakan untuk menghubungkan client ke server
s.connect((hostname, 50010)) #mengonekkan localhost dengan port ke 50010

while pesan.lower() != 'Keluar': #ketika mengirimkan pesan ke server
    pesan = input('perintah:') #mengambil input dari pengguna sebagai pesan yang akan di kirim ke server
                                #akan menampilkan perintah: pada terminal
    pesan = pesan.encode() #Meng-encode pesan menjadi format byte untuk dikirim melalui socket.
    s.send(pesan) #mengirim pesan
    if pesan.lower() != 'Keluar': #jika pesan yang dikirim bukan 'Keluar', client akan menunggu respons dari server.
        response = s.recv(1024) #Menerima respons dari server dengan ukuran mak.1024 byte.
        response = response.decode() #Mendecode respons yang diterima dari server ke dalam bentuk string.
        print ('jawaban:', response) #mencetak 'jawaban' pada saat di terminal
s.close() #menutup koneksi