#nama berkas: p_tcpser.py
#client TCP untuk server client p_tcpcli.py
#jika ingin menjalankan program harus membuka vscode baru
import socket

hostname = 'localhost'
pesan =  ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuat socet
s.connect((hostname, 50001)) #menghubungkan ke sisi server. memiliki addres local host 
                             #terhubung ke port yang di sesuaikan

while pesan.lower() != 'q': 
    pesan = input('kirim:')
    pesan = pesan.encode() #encode berguna untuk data bertype object
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        response = response.decode() 
        print('Balasan server:', response)
s.close()