import time #Mengimpor waktu bawaan pada komputer
waktu_sekarang = time.localtime() #Mengambil data waktu lokal sekarang disimpan pada variabel waktu_sekarang
                    #time.localtime() digunakan untuk mengetahui informasi waktu seperti jam,menit,detik
detik = waktu_sekarang.tm_sec #Detik menyimpan data waktu sekarang dari komputer
while detik <= 60: #perulangan while akan terus berjalan selama nilai detik kurang sama dengan 60
    print(f"{waktu_sekarang.tm_hour}:{waktu_sekarang.tm_min}:{detik}") 
                    #Mencetak waktu saat ini dalam format jam,menit, detik
    detik += 1 #Detik akan bertambah satu persatu detik
    time.sleep(1) #menampilkan 1 detik sebelum melanjutkan kedetik selanjutnya, ada jeda waktu 1 detik
    if detik == 60: #Ketika detik sama sama dengan 60
        print("Jam praktikum sudah habis. Silahkan pulang.") #akan menampilkan tulisan
                                                             # "Jam praktikum sudah habis. Silahkan pulang."
        break #digunakan untuk menghentikan program