# Jelaskan tiap baris kode maksud dari kode di bawah ini. 
# Kemudian buatlah sebuah tiga buah objek dari class tersebut dengan argument yang berbeda-beda

class Cat: #Mendefinisikan sebuah class bernama "Cat".
    def __init__(self, nama, beratBadan=0): # __init__ untuk menginisialisasi objek Cat. Menerima dua parameter
        #nama dan berat_badan (default-nya 0).
        self.nama = nama #Menyimpan nilai nama pada self.nama
        while beratBadan <= 0: #Perulangan while memastikan berat_badan yang dimasukkan tidak kurang dari 0.
            print("Enter a positive number!") #Mencetak pesan jika beratBadan kurang dari 0.
            beratBadan = int(input("Enter beratBadan: ")) #Mengambil input baru untuk beratBdan jika kurang dari 0.
        self.beratBadan = beratBadan #Menetapkan nilai beratBadan 

#Membuat 3 objek kucing
cat1 = Cat("LOLY", 7) 
cat2 = Cat("KATTY", 10)
cat3 = Cat("PII", 15)

print(f"Nama :{cat1.nama}, berat badan : {cat1.beratBadan}")
print(f"Nama : {cat2.nama}, berat badan : {cat2.beratBadan}")
print(f"Nama : {cat3.nama}, berat badan : {cat3.beratBadan}")