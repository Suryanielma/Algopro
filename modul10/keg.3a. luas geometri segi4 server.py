import socket #mengimport socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuka jaringan dengan membuat object socket client 
                                                      #digunakan untuk menghubungkan client ke server
s.bind(("",50004)) #menyediakan portal untuk menerima apapun dari alamat clien dari alamt port, alamt port dapat dirubah
s.listen(5) #menerima koneksi dari clien mak.5

print ("server siap") #mencetak server siap pada awal program
perintah = "" #menyimpan variabel kosong
a = '' #varibael menyimpan nilai a yang nanti diminta oleh client

while perintah != "keluar": #loop ketika perintah tidak sama dengan "keluar"
    komm, addr = s.accept() #Memulai loop dalam koneksi untuk menerima perintah dari klien.
    while perintah != "keluar": #Loop ketika perintah tidak sama dengan "keluar"
        item = komm.recv(1024).decode().lower().split(" = ") #Menerima pesan dari klien, mendecode pesan dari format byte menjadi string,
                                        #mengonversi semua huruf menjadi huruf kecil, dan memisahkan pesan dengan "=".
        perintah = item[0] #mengampil perintah dari pedan yang diterima pada indeks ke 0
        if perintah == "keluar": #jika perintah sama sama dengan "keluar"
            komm.send("done".encode()) #mengirim pesan "done"
            s.close() #menutup perintah
            break #menghentikan sistem
        print ("pesan : ", perintah)
        if len(item) == 2: #Mengecek apakah pesan memiliki dua bagian, 
                        #yaitu nama perintah dan nilai parameter.
            if perintah == "alas": #jika perintah sama sama dengan alas
                a = int(item[1]) #variabel a menyimpan nilai integer indek 1
                komm.send("parameter dicatat".encode()) #mengirim pesan kembali ke client 'parameter dicatat'
            else: #jka perintah  yang dimasukkan tidak sesuai
                komm.send("parameter harap disesuaikan".encode()) #akan mengirim pesan kepda client 'parameter harap disesuaikan'
        elif perintah == "hitung": #ketika perintah sama sama dengan 'hitung'
            L = int(a * a) #L = integer (a kali a)
            response = "Luas persegi empat dengan sisi {} adalah {}".format(a, L)
            #responnya 'luas persegi empat dengan sisi {parameter di sisi terserah client}
            #adalah {hasil dari hitung} formatnya a, L
            komm.send(response.encode()) #Mengirim pesan kembali ke client 'response'
        else: #jika pesan yang dimasukkan tidak sesuai dengan kode yang sudah dibuat
            komm.send("parameter harap disesuaikan".encode()) #akan mengirim pesan kepada clien 'parameter harap disesuaikan'
