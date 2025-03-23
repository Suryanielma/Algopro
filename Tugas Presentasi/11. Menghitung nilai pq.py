#https://www.spoj.com/submit/BSCXOR/id=32416763
#Diberikan dua nilai logika p dan q (0 atau 1) harap hitung p XOR q.

p, q = map(int, input().split())#memisahkan input berdasarkan spasi
result = p ^ q #memastikan input yang dimasukkan integer
print(result) #mencetak result