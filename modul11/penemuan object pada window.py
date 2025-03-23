import tkinter as tk

root = tk.Tk() #ttk modul membuat mengakses digit tema tkk
root.title("aplikasi dengan beberapa widget")

# Label dan Entry untuk Nama
nama_label = tk.Label(root, text="Nama Mahasiswa:")
nama_label.grid(column=0, row=0)

nama_entry = tk.Entry(root)
nama_entry.grid(column=1, row=0)

# Label dan Entry untuk NIM
nim_label = tk.Label(root, text="NIM:")
nim_label.grid(column=0, row=1)

nim_entry = tk.Entry(root)
nim_entry.grid(column=1, row=1)



# Tombol Submit
def submit():
    nama = nama_entry.get()
    nim = nim_entry.get()

    print("Nama Mahasiswa:", nama)
    print("NIM:", nim)


submit_button = tk.Button(root, text="Hello", command=submit)
submit_button.grid(column=1, row=3)

root.mainloop()