#https://www.spoj.com/problems/IDONTKNOW
#riddle

import random
def favourite_numbers():
    # Membuat daftar angka dari 1 hingga 20
    numbers = list(range(1, 21))
    
    # Memilih dua angka acak sebagai angka favorit
    favourite_numbers = random.sample(numbers, 2)
    
    # Mengembalikan angka favorit yang dipisahkan oleh spasi atau baris baru
    return '\n'.join(map(str, favourite_numbers))

# Menampilkan hasil
result = favourite_numbers()
print(result)