import tkinter
from tkinter import Tk,ttk

#init
window = Tk()
window.geometry("300x100")
window.title("Kenalkan Diri Anda")

def tombol_click():
    '''Fungsi ini akan dipanggil oleh tombol'''
    # print("Halloo");
    # print(L1_entry.get());

    frame1 = Tk()
    frame1.title("Message")
    frame1.geometry("300x100")

    Lhallo = ttk.Label(frame1, text = ("HALLO SELAMAT DATANG"))
    Lhallo.grid(row = 0, sticky = "w", column = 0)

    L3 = ttk.Label(frame1, text = ("Nama Mahasiswa"), font = ("calibri 12 bold"))
    L3.grid(row = 3, sticky = "w", column = 0)

    L4 = ttk.Label(frame1, text = ("NIM"), font = ("calibri 12 bold"))
    L4.grid(row = 5, sticky = "w", column = 0)

    L5 = ttk.Label(frame1, text = L1_entry.get(), font = ("calibri 12 bold"))
    L5.grid(row = 3, sticky = "w", column = 1)

    L5 = ttk.Label(frame1, text = L2_entry.get(), font = ("calibri 12 bold"))
    L5.grid(row = 5, sticky = "w", column = 1)

#komponen-komponen
#1. label nama
L1 = ttk.Label(window, text = "Nama :")
L1.grid(row = 0, sticky = "w", column = 0)
#entry nama
L1_entry = ttk.Entry(window)
L1_entry.place(x = 100, y = 8)
#3. Label NIM
L2 = ttk.Label(window, text = "NIM :")
L2.grid(row = 1, sticky = "w", column = 0)
#4. Entry NIM
L2_entry = ttk.Entry(window,)
L2_entry.place(x = 100, y = 30)
#5. Tombol
tombol_sapa = ttk.Button(window, text = "Sapa!", command = tombol_click)
tombol_sapa.place(x = 200, y = 60)

#Main Loop window
window.mainloop()