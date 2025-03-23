class Cat: #membuat class cat
  def __init__(self, nama, beratBadan): # method konstruktor untuk mengisialisasi class cat, terdiri dari 2 parameter nama, beratBadan
    self.nama = nama #menyimpan nilai parameter nama
    self.beratBadan = beratBadan #menyimpan nilai parameter beratBadan
  def CatInfo(self): #memberi informasi tentang cat
    info = "Nama: " + self.nama + ", Berat: " + str(int(self.beratBadan/1000)) + " kg"
    # membuat string info yang berisi nama, berat badan kucing yang diubah dari 1000(gram) menjadi kg
    return info #mengembalikan nilai string yang sudah dibuat

#membuat objek kucing dengan 2 parameter nama dan berat badannya
a = Cat("Coco", 5000)
b = Cat("Milo", 4000)
c = Cat("Neko", 4500)

#mencetak objek dengan memanggil methodnya
print(a.CatInfo())
print(b.CatInfo())
print(c.CatInfo())