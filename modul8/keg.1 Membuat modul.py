Datadiri = {'NIM' : 'L20030252',
            'Nama' : 'Suryani Elmaghfiroh',
            'Alamat' : 'Jl.Mendungan kos wijaya kusuma 03',
            'TTL' : 'Koto Tinggi, 10 Februari 2005',
            'Umur' : '18 Tahun',
            'Status' : 'Mahasiswa',
            'Agama' : 'Islam'}
#Data diatas bertype dictionary yang menyimpan data key dan value, key kuncinya/NIM,Nama sampai agama dan value nilai didalamnya
def DataNIM(): #pemanggilan fungsi dengan kunci def dengan nama fungsinya yaitu DataNIM
    NIM = Datadiri['NIM'] #NIM = Datadiri dengan parameter data nim pada data dictonary 
    print('NIM = ',NIM) #Menampilkan hasil dari string NIM = dan dictonary NIM
def DataNama(): #pemanggilan fungsi dengan kunci def dengan nama fungsinya yaitu DataNama
    Nama = Datadiri['Nama'] #Nama = Datadiri dengan parameter data nama pada data dictonary
    print('Nama = ',Nama) #Menampilkan hasil dari  string Nama = dan dictonary Nama
def DataAlamat(): #pemanggilan fungsi dengan kunci def dengan nama fungsinya yaitu DataAlamat
    Alamat = Datadiri['Alamat'] #Alamat = Datadiri dengan parameter data Alamat pada data dictonary
    print('Alamat = ',Alamat)  #Menampilkan hasil dari  string Alamat = dan dictonary Alamat
def DataTTL(): #pemanggilan fungsi dengan kunci def dengan nama fungsinya yaitu DataTTL
    TTL = Datadiri['TTL'] #TTL = Datadiri dengan parameter data TTL pada data dictonary
    print('TTL = ',TTL)  #Menampilkan hasil dari  string TTL = dan dictonary TTL
def DataUmur(): #pemanggilan fungsi dengan kunci def dengan nama fungsinya yaitu DataUmur
    Umur = Datadiri['Umur'] #Umur = Datadiri dengan parameter data umur pada data dictonary
    print('Umur = ',Umur)  #Menampilkan hasil dari  string Umur = dan dictonary Umur
def DataStatus(): #pemanggilan fungsi dengan kunci def dengan nama fungsinya yaitu DataStatus
    Status = Datadiri['Status'] #Status = Datadiri dengan parameter data Status pada data dictonary
    print('Status = ',Status)  #Menampilkan hasil dari  string Status = dan dictonary Status
def DataAgama(): #pemanggilan fungsi dengan kunci def dengan nama fungsinya yaitu DataAgama
    Agama = Datadiri['Agama'] #Agama = Datadiri dengan parameter data Agama pada data dictonary
    print('Agama  = ',Agama)  #Menampilkan hasil dari  string Agama = dan dictonary Agama
print('''Pilihan yang tersedia : #Menampilkan pilihan yang tersedia dari b sampai k yaitu keluar
b menampilkan bantuan ini 
N menampilkan NIM
a menampilkan Nama
A menampilkan Alamat
c menampilkan TTL
d menampilkan Umur
D menampilkan Status
e menampilkan Agama
k keluar''')

Pilihan = ('b', 'N', 'a', 'A', 'c', 'd', 'D', 'e', 'k') #pembuatan tuple yang berisi daftar pilihan yang dapat dimasukkan 
                                                        #oleh pengguna
while Pilihan != 'k': #perulagan pilihan tidak sama dengan k
    Pilihan = input('Pilihan saudara:') #pilihan sama dengan input pilihan saudara
    if Pilihan == 'b': #jika pilihan sama sama dengan b 
        print('''Pilihan yang tersedia : #akan menampilkan pilihan yang  tersedia dari b sampai  k keluar
            b menampilkan bantuan ini 
            N menampilkan NIM
            a menampilkan Nama
            A menampilkan Alamat
            c menampilkan TTL
            d menampilkan Umur
            D menampilkan Status
            e menampilkan Agama
            k keluar''')
    elif Pilihan == 'k':#Jika pilihan sama dengan k maka
        print('Terima Kasih') #hasilnya muncul terima kasih
        break  #Menghentikan program 
    elif Pilihan == 'N': #jika pilihan sama dengan N
        DataNIM()        #akan muncul tampilan dari data nim yaitu l200230252
    elif Pilihan == 'a': #Jika pilihan sama dengan a maka
        DataNama()       #akan muncul tampilan dari data nama yaitu Suryani Elmaghfiroh
    elif Pilihan == 'A': #Jika pilihan sama dengan A maka
        DataAlamat()     #akan muncul tampilan dari data Alamat yaitu Jl.Mendungan kos wijaya kusuma 03
    elif Pilihan == 'c': #Jika pilihan sama dengan c maka
        DataTTL()        #akan muncul tampilan dari data TTL yaitu Koto Tinggi, 10 Februari 2005 
    elif Pilihan == 'd': #Jika pilihan sama dengan d maka
        DataUmur()       #akan muncul tampilan dari data Umur yaitu 18 Tahun
    elif Pilihan == 'D': #Jika pilihan sama dengan D maka
        DataStatus()    #akan muncul tampilan dari data Status yaitu Mahasiswa
    elif Pilihan == 'e': #Jika pilihan sama dengan e maka
        DataAgama()      #akan muncul tampilan dari data Agama yaitu Islam
    else: #jika pilihan tidak sesuai dengan simbol diatas maka
        print('Pilihan tidak dikenal') #akan muncul tampilan "pilihan tidak dikenal"