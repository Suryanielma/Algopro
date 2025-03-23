#https://www.spoj.com/problems/FUCT_IF_SEC2TIME
#Masukkan bilangan bulat positif apa pun yang menjelaskan total detik. 
# Anda harus mengubah total detik menjadi waktu dalam format "hh:mm:ss".
#input
#Berisi total detik.
#output
#Cetak waktu dalam format "hh:mm:ss".

def seconds_to_time(seconds):
    if seconds < 0: #jika second kurang dari 0
        return "total detik harus bilangan positif" #akan mengasilkan tulisan tersebut
    else: #jika input yang dimasukan tidak negatif
        m, s = divmod(seconds, 60) #Fungsi divmod mengambil dua argumen, detik dan 60, 
                                    #dan mengembalikan tupel (m, s) 
        h, m = divmod(m, 60) #menghitung jam dan menit yang tersisa. 
        return f"{h:02d}:{m:02d}:{s:02d}" #mengembalikan string berformat yang mewakili waktu dalam format "hh:mm:ss".
        # F-string memformat jam, menit, dan detik sebagai bilangan bulat dua digit (:02d)

seconds = int(input()) #membaca masukan bilangan bulat dari pengguna, mewakili jumlah total detik.
print(seconds_to_time(seconds)) ##dan mencetak waktu yang dihasilkan dalam format "jj:mm:ss".
                                #Memanggil fungsi detik_ke_waktu dengan input detik yang disediakan 