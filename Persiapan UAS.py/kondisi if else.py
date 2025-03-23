# for i in range(10):
#     print(i, end='')

# j = 1
# while j <100:
#     print(j, end='')
#     j  = 2 * j

# a = int(input("masukkan bilangan "))
# if a > 0 :
#     print("anda memasukkan angka positif")
# elif a == 0:
#     print("anda memasukkan angka 0")
# else:
#     ("anda memsukkan bilangna negatif")
    
# a = int(input("masukkan sebuah bilangan"))
# if a > 0:
#     print("anda memasukkan bilangan positif")
# elif a == 0:
#     ("anda memsukkan angka 0")
# else:
#     print("anda memasukkan bil.negatif")

# a = float(input("masukkan sebuah angka: "))
# if a > 0 and a %  2 == 0:
#     print("anda memasukkan bilangan positif yang habis dibagi 2")

# if not a // 1 == a /1:
#     print("anda memasukkan bilangan desimal")
# if  a  > 10 or a < -10:
#     print("nilai mutlak bilangan tersebut lebih dari 10")

# Nama = "Suryani Elmaghfrioh"
# NIM = "L200230252"
# Semester = "Satu"
# IPK = "4.00"
# Prodi = "Teknik Informatika"
# print(Nama)
# print(NIM)
# print(Semester)
# print(IPK)
# print(Prodi)

# Nama = "Suryani Elmagfiroh"
# TanggalLahir = "10 Februari 2005"
# NamaSingkat = Nama[0] + "." + Nama[2] + " " + Nama[8:]
# Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[12:]
# Password = Nama[7:11] + TanggalLahir[13:]
# print(Nama)
# print(TanggalLahir)
# print(NamaSingkat)
# print(Username)
# print(Password)

# Nama = "Suryani Elmaghfiroh"
# NIM = "L200230252"
# x = "1" + NIM[7:]
# a = int(x)
# b = len(Nama)
# print(Nama)
# print(NIM)
# print(x)
# print(a)
# print(b)

# L = [4, 2 , 3 , 6]
# for i in L:
#     Y = i**2 - 2*i + 1
#     print(i,Y)

# Bangun = {"SegiTiga"       : "L = 0.5 *a * t",
#           "Segi"          : "s ** 2",
#           "jajr genjang" : "a * t"}
# key = list(Bangun.keys())
# value = list(Bangun.values())
# Nomor = 0
# print("Nomor        | Bangun         |   Rumus")
# print(".............|................|.........|")
# for key in Bangun:
#     Nomor += 1
#     print(f'{Nomor}    |{key}|   {Bangun[key]}')

# Kesempatan = 1
# for i in range(3):
#     Kesempatan +=1
#     Password = str(input("mASUKKAN PASWORD"))
#     if Password == "Elma":
#         print("login")
#         break
#     elif Kesempatan >3:
#         print("tolak")
#     else:
#         print("cobalg")

# Waktu = ("pagi", "Siang", "Sore", "petang", "Malam")
# Nama = str(input("Masukkan nama = "))
# jam = float(input("jam  berapa sekarang? "))

# if 00.01>jam>=09.00:
#     print("Selamat", Waktu[0], Nama)
# elif 09.01>jam>=15.00:
#     print("Selamat", Waktu[1], Nama)
# elif 15.01>jam>=17.00:
#     print("Selamat", Waktu[2], Nama)
# elif 17.01>jam>19.00:
#     print("Selamat", Waktu[3], Nama)
# else:
#     print("Selamat", Waktu[4], Nama)


# Nama = str(input("Masukkan nama = "))
# NIM = str(input("Masukkan NIM = "))
# Matkul = str(input("Mata kuliah ="))

# a = int(input("a = "))
# b = int(input("b = "))
# Hasil = a*b

# print(Hasil)

Nama = str(input("Masukkan nama = "))
NIM = str(input("Masukkan NIM = "))
UTS = float(input("Masukkan nilai UTS = "))
UAS = float(input("Masukkan nilai UAS ="))
Rata_Rata = (UTS+UAS)/2

if Rata_Rata >=80:
    Nilai = "a"
elif Rata_Rata >=70:
    Nilai = "b"
elif Rata_Rata >=60:
    Nilai = "c"
elif Rata_Rata >=50:
    Nilai = "d"
else:
    Nilai = "e"

print(f'Nama saudara: {Nama}')
print(f'Nim saudara: {NIM}')
print(f'nilai rata rata: {Rata_Rata}')
print(f'nilai anda: {Nilai}')