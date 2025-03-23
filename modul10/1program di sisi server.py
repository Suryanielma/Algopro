#nama berkas: p_tcpser.py
#TCP server untuk client p_tcpcli.py
#jika ingin menjalankan program harus membuka vscode baru
import socket #mengimport modul socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuat jaringannya. isi object dari socet berupa 2 parameter
s.bind(("", 50001)) # "" merupakan alamat, dari object s akan dibuka jaringan komunikasinya, 
                    #yg isinya addres atau alamt, portnya 50001
s.listen(5) #melayani pelayanan jumlah 5
print ("TCP server sudah siap")
data = ''

while True: #ketika ada koneksi
    komm, addr = s.accept() #hostname dan port masuk kesini
    while data != 'Q' and data != 'q': #penambahkan koneksi 
        data = komm.recv(1024) #pesan yang akan di kirim sebanyak 1024
        data = data.decode()
        print ('Pesan client diterima:', data)
        data = data.encode()
        komm.send(data.upper()) #data dikirim balik
    s.close()
    if data == 'Q' or data == 'q':
        break