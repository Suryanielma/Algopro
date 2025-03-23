import socket #mengimport modul socket
import platform #mengimport modul platform yang memberikan informasi tentang sistem yang digunakan

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuka jaringan dengan membuat object socket client 
                                                      #digunakan untuk menghubungkan client ke server
s.bind(("", 50004)) #mengikat socket ke alamat ip kosong dan port 50004
s.listen(5) # menerima koneksi dari client max.5

print ("Program Komunikasi tentang Server") #mencetak pesan untuk awal program
data = "" #variabel untuk menyimpan data yang diterima dari client

while True: #loop ketika semua bernilai benar
    komm, addr = s.accept() #menerima koneksi dari client dan menungu pesan masuk
    while data.lower() != "quit": ##loop ketika variabel data yang diterima tidak sama dengan 'quit'
        data = komm.recv(1024) #menerima pesan dari client dalam bentuk byt 1024
        data = data.decode() #mengubah pesan byte dalam bentuk string
        print ("command : ",data.encode()) #mencetak pesan yang diterima 
        if data.lower() == "machine": #jika pesan yang diterima adalah machine
            response = platform.machine() #akan merespon informasi tentang mesin yang digunakan
            komm.send(response.encode()) #Mengirim respons kembali ke client dalam bentuk byte 
                                        #setelah melakukan encode dari respons yang dihasilkan oleh perintah platform 
        elif data.lower() == "release": #jika pesan yang dierima adalah release
            response = platform.release() #akan merespon informasi tentang
            komm.send(response.encode()) #Mengirim respons kembali ke client dalam bentuk byte 
                                        #setelah melakukan encode dari respons yang dihasilkan oleh perintah platform 
        elif data.lower() == "system": #jika pesan yang dierima adalah system
            response = platform.system() #akan merespon system pada mesin
            komm.send(response.encode()) #Mengirim respons kembali ke client dalam bentuk byte 
                                        #setelah melakukan encode dari respons yang dihasilkan oleh perintah platform 
        elif data.lower() == "version": #jika pesan yang dierima adalah versy
            response = platform.version() #akan merespon versi pada mesin
            komm.send(response.encode()) #Mengirim respons kembali ke client dalam bentuk byte 
                                        #setelah melakukan encode dari respons yang dihasilkan oleh perintah platform 
        elif data.lower() == "node": #jika pesan yang dierima adalah nama penggguna pada mesin
            response = platform.node() #akan merespon nama pengguna pada mesin
            komm.send(response.encode()) #Mengirim respons kembali ke client dalam bentuk byte 
                                        #setelah melakukan encode dari respons yang dihasilkan oleh perintah platform 
        else: #jika perintah yang dimasukkan tidak sesuai
            komm.send("unknown command".encode()) #akan menampilkan "unknown command"
