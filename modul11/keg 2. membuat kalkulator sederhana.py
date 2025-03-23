from tkinter import * #mengimpor semua kelas dan aafungsi yang ada di modul tkinter

root = Tk() #membuat sebuah objek Tk yang akan menjadi root window dari GUI
root.geometry("350x200") #ukuran root window
root.title("Kalkulator") #judul root window

def tambah(): #fungsi tambah yang nanti akan di panggil ketika tombol + ditekan
    i1 = int(input1.get())
    i2 = int(input2.get())
    n = i1 + i2
    hasil.config(text=n)

def kurang():
    i1 = int(input1.get())
    i2 = int(input2.get())
    n = i1 - i2
    hasil.config(text=n)

def kali():
    i1 = int(input1.get())
    i2 = int(input2.get())
    n = i1 * i2
    hasil.config(text=n)

def bagi():
    i1 = int(input1.get())
    i2 = int(input2.get())
    n = i1 / i2
    hasil.config(text=n)

Label(root, text="Angka 1").place (x=50, y=20) #membuat sebuah label dengan teks “Angka 1”.pada root window pada posisi x=50 dan y=20.
input1 = StringVar() #membuat sebuah objek StringVar yang akan digunakan untuk menyimpan input dari user pada field “Angka 1”.
Entry(root, textvariable=input1).place(x=100, y=20) #membuat sebuah field input yang terhubung dengan objek StringVar input1.
Label(root, text="Angka 2").place (x=50, y=40) ##membuat sebuah label dengan teks “Angka 2”.pada root window pada posisi x=50 dan y=20.
input2 = StringVar() #membuat sebuah objek StringVar yang akan digunakan untuk menyimpan input dari user pada field “Angka 2”.
Entry(root, textvariable=input2).place(x=100, y=40) #membuat sebuah field input yang terhubung dengan objek StringVar input1

Button(root, text='+', command=tambah).place(x=100, y=65) #membuat sebuah tombol dengan teks “+”. Ketika tombol tersebut ditekan, fungsi tambah() akan dipanggil. root window pada posisi x=130 dan y=65.
Button(root, text='-', command=kurang).place(x=130, y=65) #membuat sebuah tombol dengan teks “-”. Ketika tombol tersebut ditekan, fungsi kurang() akan dipanggil.
Button(root, text='x', command=kali).place(x=160, y=65) #membuat sebuah tombol dengan teks “x”. Ketika tombol tersebut ditekan, fungsi kali() akan dipanggil. 
Button(root, text=':', command=bagi).place(x=190, y=65) #membuat sebuah tombol dengan teks “:”. Ketika tombol tersebut ditekan, fungsi bagi() akan dipanggil.

Label(root, text="Hasil= ").place(x=100, y=100) #sebuah label dengan teks “Hasil=”.ditempatkan pada root window pada posisi x=100 dan y=100.
hasil = Label(root, text="") #Baris ini membuat sebuah label kosong yang akan digunakan untuk menampilkan hasil kalkulator
hasil.place(x=140, y=100) #pada root window posisi x=140 dan y=100.

Button(root, text="Tutup", command=root.destroy).place(x=150, y=150) #membuat sebuah tombol dengan teks “Tutup”. Ketika tombol tersebut ditekan, 
                        #fungsi root.destroy() akan dipanggil untuk menutup root window. pada root window pada posisi x=150 dan y=150.
root.mainloop() #menjalankan main loop dari GUI untuk menampilkan root window



# from tkinter import *

# root = Tk()
# root.geometry("400x400")
# root.title("Kalkulator")

# def tambah():
#     i1 = int(input1.get())
#     i2 = int(input2.get())
#     n = i1 + i2
#     hasil.config(text=n)

# def kurang():
#     i1 = int(input1.get())
#     i2 = int(input2.get())
#     n = i1 - i2
#     hasil.config(text=n)

# def kali():
#     i1 = int(input1.get())
#     i2 = int(input2.get())
#     n = i1 * i2
#     hasil.config(text=n)

# def bagi():
#     i1 = int(input1.get())
#     i2 = int(input2.get())
#     n = i1 / i2
#     hasil.config(text=n)

# Label(root, text="Angka 1").place (x=50, y=20)
# input1 = StringVar()
# Entry(root, textvariable=input1).place(x=100, y=20)
# Label(root, text="Angka 2").place(x=50, y=40)
# input2 = StringVar()
# Entry(root, textvariable=input2).place(x=100, y=40)

# Button(root, text='+', command=tambah).place(x=100, y=65)
# Button(root, text='-', command=kurang).place(x=130, y=65)
# Button(root, text='*', command=kali).place(x= 160, y=65)
# Button(root, text='/', command=bagi).place(x=190, y=65)

# Label(root, text="Hasil =").place(x=100, y=100)
# hasil = Label(root, text="")
# hasil.place(x=1400, y=100)

# Button(root, text="Tutup", command=root.destroy).place(x=150, y=150)
# root.mainloop()




# # import tkinter as tk

# # class Calculator:
# #     def __init__(self, master):
# #         self.master = master
# #         master.title("Kalkulator Sederhana")

# #         # Create screen widget
# #         self.screen = tk.Entry(master, width=30, font=('Arial', 24))
# #         self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# #         # Create number buttons
# #         button_list = [
# #             '7', '8', '9', '/',
# #             '4', '5', '6', '*',
# #             '1', '2', '3', '-',
# #             '0', '.', '=', '+'
# #         ]
# #         r = 1
# #         c = 0
# #         for b in button_list:
# #             cmd = lambda x=b: self.click(x)
# #             tk.Button(master, text=b, width=5, height=2, command=cmd).grid(row=r, column=c, padx=5, pady=5)
# #             c += 1
# #             if c > 3:
# #                 c = 0
# #                 r += 1

# #         # Create clear button
# #         clear_button = tk.Button(master, text='Clear', width=5, height=2, command=self.clear)
# #         clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# #         # Create delete button
# #         delete_button = tk.Button(master, text='Del', width=5, height=2, command=self.delete)
# #         delete_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# #     def click(self, key):
# #         if key == '=':
# #             # Calculate the expression
# #             result = eval(self.screen.get())
# #             self.screen.insert(tk.END, ' = ' + str(result))
# #         elif key == 'C':
# #             self.screen.delete(0, tk.END)
# #         elif key == 'CE':
# #             self.screen.delete(len(self.screen.get())-1, tk.END)
# #         else:
# #             self.screen.insert(tk.END, key)

# #     def clear(self):
# #         self.screen.delete(0, tk.END)

# #     def delete(self):
# #         self.screen.delete(len(self.screen.get())-1, tk.END)

# # root = tk.Tk()
# # my_gui = Calculator(root)
# # root.mainloop()
