#https://www.spoj.com/problems/PRF04STRING02
#Buat program yang memungkinkan pengguna memasukkan teks, 
# lalu menghilangkan spasi dari sisi kiri string dan mencetaknya.

input_text = input() #memasukkan sebuah string
spasi_kiri = input_text.lstrip() #Menghapus spasi dari sisi kiri string
print(spasi_kiri) #Mencetak string yang telah dihapus spasi dari sisi kiri