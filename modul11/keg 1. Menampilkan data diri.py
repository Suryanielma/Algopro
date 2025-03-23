import tkinter as tk #mengimport modul thinter dan disingkat menjadi tk

root=tk.Tk() #membuat sebuah objek tk menjadi root window
root.title("Data diri Elma") #baris untuk judul dari root window
root.geometry("500x250") #ukuran root window

def close(): #fungsi close
    root.destroy()#memanggil destroy pada objek tk

tk.Label(root, text="Data diri", font=("Timesnewnormal", 22)).place(x=10)
#membuat sebuah label dengan teks “Data diri” dan font “Timesnewnormal” dengan ukuran 22. 
# Label tersebut ditempatkan pada root window pada posisi x=10 
tk.Label(root, text="Nama").place(x=10, y=40)
#Baris ini membuat sebuah label dengan teks “Nama”. Label tersebut ditempatkan pada root window pada posisi x=10 dan y=40.
tk.Label(root, text="Suryani Elmaghfiroh").place(x=160, y=40)
#Baris ini membuat sebuah label dengan teks “Suryani Elmaghfiroh”. Label tersebut ditempatkan pada root window pada posisi x=160 dan y=40.
tk.Label(root, text="NIM").place(x=10, y=70)
#sebuah label dengan teks “NIM”. Label tersebut ditempatkan pada root window pada posisi x=10 dan y=70
tk.Label(root, text="L200230252").place(x=160, y=70)
#membuat sebuah label dengan teks “L200230252”. Label tersebut ditempatkan pada root window pada posisi x=160 dan y=70.
tk.Label(root, text="Buku Favorit").place(x=10, y=100)
tk.Label(root, text="Tere Liye").place(x=160, y=100)
tk.Label(root, text="Motto").place(x=10, y=130)
tk.Label(root, text="Be gratefull for small things and every thing in beetwen").place(x=160, y=130)
tk.Button(root, text="Tutup",command = close, height=2, width=13).place(x=160, y=170)
#Baris ini membuat sebuah tombol dengan teks “Tutup”.posisi x=160 dan y=170. Ketika tombol tersebut ditekan, fungsi close() akan dipanggil

root.mainloop() # Baris ini menjalankan main loop dari GUI untuk menampilkan root window 













# import tkinter as tk

# root = tk.Tk()
# root.title("Data Diri")

# # Label dan Entry untuk Nama
# nama_label = tk.Label(root, text="Nama:")
# nama_label.grid(column=0, row=0)

# nama_entry = tk.Entry(root)
# nama_entry.grid(column=1, row=0)

# # Label dan Entry untuk Alamat
# alamat_label = tk.Label(root, text="Alamat:")
# alamat_label.grid(column=0, row=1)

# alamat_entry = tk.Entry(root)
# alamat_entry.grid(column=1, row=1)

# # Label dan Entry untuk Umur
# umur_label = tk.Label(root, text="Umur:")
# umur_label.grid(column=0, row=2)

# umur_entry = tk.Entry(root)
# umur_entry.grid(column=1, row=2)

# # Tombol Submit
# def submit():
#     nama = nama_entry.get()
#     alamat = alamat_entry.get()
#     umur = umur_entry.get()

#     print("Nama:", nama)
#     print("Alamat:", alamat)
#     print("Umur:", umur)

# submit_button = tk.Button(root, text="Submit", command=submit)
# submit_button.grid(column=1, row=3)

# # Tombol Tutup
# tutup_button = tk.Button(root, text="Tutup", command=root.quit)
# tutup_button.grid(column=0, row=3)

# # Label dengan font berukuran besar
# L = tk.Label(root, text='coba', font=('arial',24))
# L.grid(column=0, row=4)

# root.mainloop()
