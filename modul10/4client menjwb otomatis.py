#nama berkas: p_tcpser.py
#TCP server untuk client p_tcpcli.py
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50004)) #mengonekkan localhost dengan port ke sekian

print ("mesin menjawab otomatis sudah siap")
while pesan.lower() != 'q': #ketika mengirimkan pesan ke server
    pesan = input('pertanyaan:')
    pesan = pesan.encode()
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        response = response.decode()
        print ('jawaban:', response)
s.close()