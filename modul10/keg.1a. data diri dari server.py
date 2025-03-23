#nama berkas: p_tcpser.py
#TCP server untuk client p_tcpcli.py
import socket #mengimport socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuka jaringan dengan membuat object socket client 
                                                      #digunakan untuk menghubungkan client ke server
s.bind(("", 50010)) #menyediakan portal untuk menerima apapun dari alamat client dari alamat port, alamt port dapat dirubah
                    #disini port 50001
s.listen(5) #menerima koneksi dari clien mak.5

print ("Program komunikasi tentang data diri") #mencetak program komunukasi tentang data diri. nanti muncul pada awal program 

data = '' #variabel data yang akan menyimpan data yang diterima dari client
kamus = {'Nama' : 'Suryani Elmaghfiroh',
         'NIM': 'L200230252',
         'Angkatan': '2023',
         'Keluar': 'Siap!!'} #sebuah kamus dictonary

error = 'Maaf perintah tidak dimengerti'#pesan ketika perintah tidak ditemukan dalam kamus 
while data.lower() != 'Keluar': #loop ketika variabel data yang diterima tidak sama dengan 'keluar'
    komm, addr = s.accept() #penamaan variabel, menerima permintaan koneksi
    while data.lower() != 'Keluar': #loop ketika variabel data yang diterima tidak sama dengan 'keluar'
        data = komm.recv(1024) #menerima data dari client dalam uk.max 1024
        data = data.decode() #mendecode data yang diterima dari client
        if data.lower() == 'Keluar': #jika data yng diterima adalah keluar
            s.close() #menutup data
            break #menghentikan loop
        print( 'perintah:', data) 
        if data in kamus: #jika perintah dari client ada di dalam kamus
            komm.send(kamus[data].encode()) #server akan  mengirimkan nilai dari kamus
        else:  #jika perintah dari client tidak ada di dalam kamus
            komm.send(error.encode()) #akan error