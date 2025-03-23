import tkinter as tk #mengimport modul thinter dan disingkat menjadi tk

def hitung_luas(): #fungsi hitung luas yang akan di jalankan  ketiika dipanggil
    try:#mengeksekusi ketika ada kode yang salah
        sisi = float(entry_sisi.get()) #Mengambil nilai dari suatu entri yang diasumsikan sebagai entry_sisi dan mengonversinya menjadi nilai float 
        luas = sisi ** 2 #rumus luas segi empat
        label_hasil.config(text=f'Luas Segi Empat: {luas}', font=("thimesnewnormal", 12, "bold")) 
        #untuk menampilkan hasil perhitungan luas segi empat. Teks yang ditampilkan berupa pesan yang menyertakan nilai luas yang telah dihitung
    except ValueError: #jika kkode yang dimasukkan salah
        label_hasil.config(text='Masukkan nilai numerik!') #akan menampilkan hasil "masukkan nilai numerik!"

#Membuat window
window = tk.Tk() # Baris ini membuat sebuah objek Tk yang akan menjadi root window dari GUI.
window.title('Aplikasi Hitung Luas Segi Empat') # judul dari root window
window.geometry('750x350') #ukuran root window
                
judul = tk.Label(window, text="Luas Segi Empat", font=("thimesnewnormal", 20, "bold")).place (x=20, y=20) #membuat sebuah label dengan teks “Luas Segi Empat”
deskripsi = tk.Label (window, text="Segi Empat merupakan bentuk geometri dua dimensi yang memiliki empat sisi sama panjang.""", 
                      font=("thimesnewnormal",12)).place(x=20, y=70) #membuat sebuah label dskripsi 

#Membuat entry untuk memasukkan panjang sisi
label_sisi = tk.Label (window, text='sisi: ', font=("thimesnewnormal", 12, "bold")) #membuat sebuah label dengan teks “sisi:”.pada root window pada posisi x=20 dan y=120.
label_sisi.grid(row=0, column=0, padx=20, pady=120) #menempatkan label pada grid row=0 dan column=0 pada root window dengan jarak padding x=20 dan y=120.
entry_sisi = tk.Entry(window) #Baris ini membuat sebuah field input untuk memasukkan panjang sisi segi empat. Field input tersebut ditempatkan pada root window pada posisi x=20 dan y=120.
entry_sisi.grid(row=0, column=1, padx=20, pady=120) #menempatkan entry pada grid row=0 dan column=1 pada root window dengan jarak padding x=20 dan y=120.

# Tombol untuk menghitung luas
tombol_hitung = tk.Button (window, text="Hitung Luas", command=hitung_luas) # Membuat tombol dengan teks "Hitung Luas" dan menetapkan fungsi hitung_luas() 
                                                                            #sebagai fungsi yang akan dipanggil ketika tombol ini ditekan.
tombol_hitung.grid(row=1, column=0, pady=0)#menempatkan tombolhitung pada grid row=1 dan column=0 pada root window dengan jarak padding y=0.


# Label untuk menampilkan hasil luas
label_hasil = tk.Label (window, text="") #membuat sebuah label kosong yang akan digunakan untuk menampilkan hasil luas segi empat
label_hasil.grid(row=1, column=1, pady=1)#menempatkan label grid  row=1 dan column=1 pada root window dengan jarak padding y=1

# Menjalankan loop window.mainloop()
window.mainloop()














# import tkinter as tk
# def hitung_luas():
#     try:
#         sisi = float(entry_sisi.get())
#         luas = sisi * 2
#         label_hasil.config(text=f'Luas Persegi : {Luas}', font=("thimesnewnormal", 12, "bold"))
#     except ValueError:
#         Label_hasil.config(text=("Masukkan nnilai numerik!"))

# #membuat window
# window = tk.Tk()
# window.title("Aplikasi hitung luas persegi")
# window.geometry("700x350")

# judul = tk.Label(window, text="Luas Segi Empat", font=("thimesnewnormal",20,"bold")).place(x=20, y=20)
# deskripsi = tk.Label(window, text="""
# Segi empat merupakan bentuk geometri dua dimensi yang memiliki empat sisi sama panjang.""", font=("thimesnewnormal",12)).place(x=20, y=80)

# #Membuat entry untuk memasukkan sisi segi empat
# label_sisi = tk.Label(window, text="sisi:", font=("thimesnewnormal", 12, "bold"))
# label_sisi.grid(row=0, column=0, padx=20, pady=150)
# entry_sisi = tk.Entry(window)
# entry_sisi.grid(row=0, column=1, padx=20, pady=150)

# #Tombol untuk menghitung luas
# tombol_hitung = tk.Button(window, text="Hitung luas", command=hitung_luas)
# tombol_hitung.grid(row=1, column=0, pady=0)

# #Label untuk  menampilkan hasil luas
# Label_hasil = tk.Label(window, text="")
# Label_hasil.grid(row=1, column=1, pady=0)

# #menjalankan lop utama
# window.mainloop()
