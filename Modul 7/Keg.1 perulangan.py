Bangun = {'Segitiga           ': 'L = 0.5 * a * t', 
        'persegi            ': 'L = S ** 2', 
        'persegi panjang    ': 'L = P * 1', 
        'lingkaran          ': 'L = pi * r ** 2', 
        'jajaran genjang    ': 'L = a * t'}
        #Data bertype dictionary yang menyimpan data key dan value, key kuncinya/nama bangun dan value nilai/rumusnya
Key = list(Bangun.keys()) #key menyimpan data list berupa bangun kunci yaitu nama dari bangunannya seperti segitiga
Value = list(Bangun.values()) #value menyimpan data list berupa nilai dari daftar rumus bangun 
Nomor = 0 #Nomor urut pada tabel dimulai dari angka 1 namun dibacanya dari angka 0, akan muncul tampilan 1 
print('No |    Nama Bangun    |    Rumus Luas    ') #Mencetak tampilan judul dengan pembatas |
print('---|-------------------|------------------') #Mencetak garis bawah pada judul 
for Key in Bangun : #mengulangi setiap kunci yang ada di dalam bangun
    Nomor +=1 #Nomor bertambah sama 1 merupakan urutan pada tabel dengan kelipatan satu
    print(f'{Nomor}  |{Key}| {Bangun[Key]}') #Mencetak semua nomor urut, nama bangunan, dan rumusnya
   




























