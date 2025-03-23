#modulhitung.py

def hitungAngka(nim):
    count = 0
    for i in nim:
        if i.isdigit() == True:
            count += int(i)
    return count

nim = 200120128

hasil_jumlah = hitungAngka(nim)
print(f"Hasil penjumlahan angka NIM {nim} adalah: {hasil_jumlah}")
# import modulHitung
# modulHitung.hitungAngka("L200230252")