import math

def hitung_luas_segitiga():
    print("Menghitung Luas Segitiga")
    alas = float(input("Masukkan Alas: "))
    tinggi = float(input("Masukkan Tinggi: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas Segitiga adalah {luas}")

def hitung_luas_lingkaran():
    print("Menghitung Luas Lingkaran")
    jari_jari = float(input("Masukkan Jari-Jari: "))
    luas = math.pi * jari_jari**2
    print(f"Luas Lingkaran adalah {luas:}")

def main():
    while True:
        print("\nSelamat Datang di Program Untuk Menghitung Luas")
        print("-------------------------------------------------")
        print("Menu Pilihan")
        print("1. Segitiga")
        print("2. Lingkaran")
        print("3. Keluar")

        opsi = input("Masukkan opsi: ")

        if opsi == '1':
            hitung_luas_segitiga()
        elif opsi == '2':
            hitung_luas_lingkaran()
        elif opsi == '3':
            break
        else:
            print("Opsi tidak valid!")

        coba_lagi = input("Mau coba lagi [Y/N]? ")
        if coba_lagi.upper() != 'Y':
            break

if __name__ == "__main__":
    main()