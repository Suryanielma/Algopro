#nama berkas: p_tcpser.py
#TCP server untuk client p_tcpcli.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuka jaringan
s.bind(("", 50004)) #menyediakan portal untuk menerima apapun dari alamat clien dari alamt port, alamt port dapat dirubah
s.listen(5) #menerima clien mak.5

print ("Server menjawab otomatis sudah siap")

data = ''
kamus = {'nama' : 'Apalah artinya sebuah nama',
         'umur': 'Saya lebih muda dari anda',
         'alamat': 'Sebuah tempat yang nyaman disebuah bukit',
         'motto': 'Malu bertanya sesat dijalan',
         'kuliah': 'program studi informatika UMS'}

error = 'pertanyaan anda tidak relevan'        
while data.lower() != 'q':
    komm, addr = s.accept() #penamaan variabel
    while data.lower() != 'q': 
        data = komm.recv(1024)
        data = data.decode()
        if data.lower() == 'q':
            s.close()
            break
        print( 'pertanyaan:', data)
        if data in kamus:
            komm.send(kamus[data].encode())
        else:
            komm.send(error.encode())