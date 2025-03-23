#https://www.spoj.com/problems/PRF04STRING04
# Buat program yang memungkinkan pengguna memasukkan teks, lalu menghilangkan spasi dari sisi kiri dan kanan ukuran string, 
# menghapus semua 2 spasi dari dalam string itu dan mencetaknya.
#Memasukkan
#             teks teks
#Keluaran
#teks teks
#ditab texs ditab teks

input_text = input() #memasukkan sebuah string
masukan = input_text.strip() # Menghapus spasi dari sisi kiri dan kanan string
text_double_spaces = ' '.join(masukan.split()) #menghapus semua tab/spasi ganda dari string yang dimasukkan 
print( text_double_spaces) #Mencetak string yang telah dihapus spasi dari sisi kiri 
                           #dan kanan,serta spasi ganda