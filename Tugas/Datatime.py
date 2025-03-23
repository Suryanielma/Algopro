from datetime import datetime

t1 = datetime(2020, 11, 2, 11, 20, 10, 34782)
t2 = datetime(1995, 10, 14)


print(str(t1))
print(str(t2))
print(abs(t2 - t1))

# untuk mengetahui selisih dari kedua objek tersebut dengan 
# #menggunakan operator min(-) karena objek tersebut menyimpan data berupa integer 