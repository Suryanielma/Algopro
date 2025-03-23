# file = open('/Users/Documents/myfile.bin', 'wb')

# ls_angka = [1.5, 2.8, 3.3]

# for item in ls_angka:
#    s = str(item) + '\n'
#    bt = s.encode()
#    file.write(bt)

# file.close();


ls_angka_2 = []

r = open('/Users/Documents/myfile.bin', 'rb')

for ln in r:
    x = float(ln)
    ls_angka_2.append(x)

print("List angka = ", ls_angka_2)

r.close();