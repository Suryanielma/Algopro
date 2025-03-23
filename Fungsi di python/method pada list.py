# #Membuat list angka
# angka = [70, 38, 192, 23, 122, 38]

# # #Menambahkan satu elemen 44 setelah elemen terakhir list angka
# angka.append(44)

# # #Mencetak list angka
# print(angka)

# # #Menghitung jumlah elemen 38 dalam list angka
# print(angka.count(38)) #menghitung

# # #Menambahkan satu elemen list [1,2,3] setelah elemen terakhir list angka
# angka.append([1,2,3]) #menambahkan

# # #Menambahkan item-item satu persatu dari elemen list [4,5,6] setelah elemen terakhir list angka
# angka.extend([4,5,6])

# # #Mencetak list angka
# print(angka)

# # #Mengembalikan indeks pertama dimana elemen 38
# # #Meskipun ada >1 elemen 38, yang dikembalikan hanyalah indeks pertamanya saja
# print(angka.index(38))

# # #Memasukkan nilai 65 ke dalam list sebagai elemen indeks ke-2 yang baru
# # #Elemen indeks 2 yang lama bergeser ke kanan, bersama dengan elemen indeks setelahnya
# angka.insert(2, 65) #memasukkan angka 65 di indeks ke 2,

# # #Mencetak list angka
# print(angka)

# # #mengambil elemen indeks ke-8, kemudian nilainya tersimpan pada variabel ambil
# ambil = angka.pop(8)
# print(ambil)

# # #Mencetak list angka
# print(angka)

# # #Menyalin isi list angka ke dalam variabel list balik
# balik = angka.copy()

# # #Elemen dari variabel balik, urutan elemennya akan dibalik
# balik.reverse()

# # #Mencetak list angka
# print(angka)

# # #Mencetak list balik
# print(balik)

# # #Menyalin isi list angka ke dalam variabel list urut
# urut = angka.copy()

# # #Mengurutkan isi list balik dar nilai terkecil hingga nilai terbesar
# urut.sort()

# # #Mencetak list urut
# print(urut)





nilai_genap_besar = [] #membuat list kosong genap besar
nilai_genap_kecil = [] #membuat list kosong genap kecil
nilai = [37, 99, 48, 55, 12, 20, 90, 47, 21, 30, 80]
batas = 50

for i in nilai: #membaca tiap elemen
    if i > batas and i%2 == 0: #jika i lebih besar dari 50 dan habis dibagi 2 maka nilainya masuk ke nilai genap besar
        nilai_genap_besar.append(i) #nilai genap #append menambahkan nilai dipaling belakang
    elif i <= batas and i%2 == 0: #jika i lebih kecil dari 50 dan habis dibagi 2 maka nilainya masuk ke nilai genap kecil
        nilai_genap_kecil.append(i) #48 sebagai i

print(nilai_genap_besar) #90, 80
print(nilai_genap_kecil) #48, 12, 20, 30


nilai_genap_besar_sorted = nilai_genap_besar.copy()
nilai_genap_besar_sorted.sort()
print(nilai_genap_besar_sorted)

nilai_genap_kecil_sorted = nilai_genap_kecil.copy()
nilai_genap_kecil_sorted.sort()
print(nilai_genap_kecil_sorted)