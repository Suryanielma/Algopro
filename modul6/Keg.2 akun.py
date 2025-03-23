#Program Akun
#Dibuat oleh Suryani Elmaghfiroh L200230252
Nama = 'Suryani Elmaghfiroh'
TanggalLahir = '10 Februari 2005'
NamaSingkat = Nama[0] + "." + Nama[8:] #[8:] urutan ke 8 sampai akhir datanya
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[12:] #
Password = Nama[:3] + TanggalLahir[12:15]
print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)