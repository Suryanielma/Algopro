# def quote ():
#     """ Mengembalikan kata kata bijak """
#     kutipan = "kerja tanpa visi tidak terarah. \n"
#     + "visi tanpa kerja adalah damagog."
#     return kutipan #return merupkan nilai kembalian 

# #memanggil fungsi 
# teks = quote() #nilai kembalian disimpan di teks
# print(teks) #nilai di dlam teks di tampilkan 
# print("sekali lagi di panggil", quote())


# def tmpl_idt(nama, alamat):
#     """menampilkan identitas seseorang yang belum diketahui siapa""" #merupakan docstring
#     print('Nama:', nama)
#     print('Alamat:', alamat) #tidak memiliki nilai kembalian,
#                              #jadi tidak menampilkan apapun
# tmpl_idt("joni", 'Surakarta') #kedua argumen diisi nilai
# nama = "pandu"
# alamat = "jakarta"
# tmpl_idt(nama, alamat) #kedua argumen disi nama variabel
# nm = "yulia"
# tmpl_idt(nm, "makasar") #argumen disi nilai atau variabel


def volume(r, t):
    """mengembalikan volume tabung berjari jari r dan tinggi t"""
    pi = 3.14
    L = pi * r ** 2 #LUAS ALAS TABUNG
    V = L * t
    return V

#Memanggil fungsi, argumen diisi  nilai
vol = volume (5, 4) #5 itu r, 4 termasuk t
print("volume tabung berjari jari 5 dan tinggi 4 adalah", vol)
#memanggil fungsii, argumen berupa variabel 
jejari = 6


# #memanggil fungsi dengan satu argumen
# print(volume(5)) # terjadi error 


# #memanggil fungsi dengan tiga argumen 
# vol = volume (3, 4, 9)
# tinggi = 10
# volume (jejari, tinggi) #ketika di run error

#jadi data akan berjalan ketika diisi sesuai dengan jumlah argumennya.
