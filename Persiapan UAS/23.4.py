# import csv
# with open('barang.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

import csv

data = [
    ['SKU','Nama Barang', 'Stok', 'Harga' ],
    ['A01','Kertas A3 isi 20', 3, 7000 ],
    ['A02','Kertas A4 isi 20', 23, 4000 ],
    ['A03','Buku Tulis 40 Halaman', 20, 5000 ],
    ['B01','Mug Wisuda Kecil', 0, 10000 ],
    ['B02','Mug Wisuda Sedang', 10, 15000 ],
    ['B03','Mug Wisuda Besar', 31, 20000 ],
    ['C01','Permen Kopiko', 0, 7000 ],
    ['C02','coca cola 330ml', 24, 9000 ],
    ['C03','pepsi 330ml', 100, 7000 ]
]

with open('data.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(data[0])
    write.writerows(data[1:])
print(file)

#Gawe file csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f'{header}')

    # Mencetak barang dengan stok habis
    for row in reader:
        if int(row[2]) == 0:  # Kolom stok berada di indeks 2
            print(row)

    #data barang yang harganya paling mahal
    max_price = 0
    max_price_item = None
    for row in reader:
        harga = int(row[3])  # Kolom harga berada di indeks 3
        if harga > max_price:
            max_price = harga
            max_price_item = row
            print(row)
    print(f'\nBarang paling mahal:\n{max_price_item}')

#Cetak barang stok habis dan harga paling tinggi