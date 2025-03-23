#https://www.spoj.com/problems/TEST
#classical
#Program Anda adalah menggunakan pendekatan brute force untuk menemukan Jawaban atas Kehidupan, 
# Alam Semesta, dan Segalanya. Lebih tepatnya... menulis ulang angka-angka kecil
#  dari input ke output. Hentikan pemrosesan input setelah membaca angka 42.
#  Semua angka yang di input adalah bilangan bulat satu atau dua digit


while True: #perulangan jika suatu kondisi bernilai benar
    number = int(input()) #membaca masukan bilangan bulat dari pengguna dan menyimpannya 
                         #ke dalam variabel number.
    print(number) #mencetak angka yang sudah dimasukan
    if number == 42: #jika angka yang dimasukkan sama dengan 42
        break #maka program akan berhenti 