class Cat:
    def __init__(self, nama, beratBadan=0):
       self.nama = nama
       while beratBadan <=0:
            print('masukkan angka positif')
            beratBadan = int(input('beratBadan:'))
            self.beratBadan = beratBadan

kucing1 = Cat("anggora", 5)
kucing2 = Cat("mila", 8)
kucing3 = Cat ("yoi", 7)

print(f"Nama : {kucing1.nama} beratBadan : {kucing1.beratBadan}")
print(f"Nama : {kucing2.nama} beratBadan : {kucing2.beratBadan}")
print(f"Nama : {kucing3.nama} beratBadan : {kucing3.beratBadan}")