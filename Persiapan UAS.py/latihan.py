# S = 'ini adalah sebuah string'
# P = "string ini diuis dengan tanda kutip ganda"
# D = """tANDDA KUTIP 3 untuk menulis kata yang oanjang 
#         berbaris baris"""
# print(S)


# S = 'Aku bisa dipanggil Elma'
# print(S[:4]) + S[10:]

# Nama = "Suryani Elmaghfiroh"
# NIM = "L200230252"
# Umur = "18 Tahun"
# IPK = 4.00
# Status = "Mahasiswa"
# print(Nama)
# print(NIM)
# print(Umur)
# print(IPK)
# print(Status)

# Nama = "Suryani Elmaghfiroh"
# TanggalLahir = '10 Februari 2005'
# NamaSingkat = Nama[1] +"." + Nama[8:12]
# Username = Nama[8] + TanggalLahir[3:5] + TanggalLahir[12:]
# password = Nama[:3] + TanggalLahir[13:]
# print(Nama)
# print(TanggalLahir)
# print(NamaSingkat)
# print(Username)
# print(password)

waktu = {'pagi', 'siang', 'sore','petang', 'malam'}
Nama = list(input("masukkan nama"))
jam = float(input("jam berapa ?"))

if 00.01 <jam<09.00:
    print('selamat', waktu[0], Nama)
elif 09.01<jam<=15.00:
    print("selamat", waktu[1], Nama)
elif 15.01<jam<=17.00:
    print("selamat", waktu[2], Nama)
elif 17.01<jam<=19.00:
    print("selamat", waktu[3], Nama)
else:
    print("selamat", waktu[4], Nama )