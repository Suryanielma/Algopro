# class Segitiga: #class segitiga bkan bawaan python
#    alas = 1
#    tinggi = 2
# #menampilkan informasi dari objek
# segitiga1 = Segitiga() #sebelah kiri nama objetc segitiga1 , sebelah kanan nama class segitiga() 
# segitiga2 = Segitiga()
# # #mencetak nilai atribut alas dan tinggi dari objeck segi3 satu dan dua
# print("Alas segitiga 1 : ", segitiga1.alas) #mengakses variabel di setiap object nya
# print("Tinggi segitiga 1 : ", segitiga1.tinggi)
# print("Alas segitiga 2 : ", segitiga2.alas)
# print("Tinggi segitiga 2 : ", segitiga2.tinggi)


# class Segitiga:
#    def __init__(self, alas, tinggi): # kalo ada methodnya ada self sebagai penanda yang dibaca hanya alas dan tinggi, 
#                                     #parameternya ada 2  yaitu alas dan tinggi.
#                                     #self itu merever ke object yang sedang di eksekusi
#       self.alas = alas 
#       self.tinggi = tinggi

#    def hitungLuas(self): #jika tidak ada self nya merupkan function atau procedure 
#       return 0.5 * self.alas * self.tinggi #nilai kembalian


# #ada 3 object yaitu segitiga1,2,3
# segitiga1 = Segitiga(20, 10) #20 10 merupakan argumen #segitiga1 masuk ke self, 20 ke alas, 10 ke tinggi
# print("Alas segitiga 1 : ", segitiga1.alas)
# print("Tinggi segitiga 1 : ", segitiga1.tinggi)
# print("Luas segitiga 1 : ", segitiga1.hitungLuas()) #memangggil method hitungluas  yaitu OBJECT.METHOD()

# segitiga2 = Segitiga(3, 5)
# print("Alas segitiga 2 : ", segitiga2.alas)
# print("Tinggi segitiga 2 : ", segitiga2.tinggi)
# print("Luas segitiga 2 : ", segitiga2.hitungLuas())

# segitiga3 = Segitiga(2, 3)
# print("Alas segitiga 2 : ", segitiga3.alas)
# print("Tinggi segitiga 2 : ", segitiga3.tinggi)
# print("Luas segitiga 2 : ", segitiga3.hitungLuas())

# #mengecek o bject dari kelas mana
# print(type(segitiga1))

# #class hampir sama dengan type data
# x = 3 #x object nya classnya integer
# print(type(x))



