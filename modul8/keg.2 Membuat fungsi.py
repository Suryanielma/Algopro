def konversi_suhu(c = 0, f = 32) : #Ini mendefinisikan fungsi konversi_suhu yang memiliki 
                                   #dua parameter opsional, c dan f, yang defaultnya adalah 0 untuk c dan 32 untuk f.
    Celcius = (9 / 5 * c) + 32
    Fahrenheit = 5 / 9 * (f - 32)
    #dua variabel diatas yaitu celcius dan fahrenheit melakukan perhitungan suhu
    if f == 32 : #Kondisi ini memeriksa apakah suhu yang diinput dalam Fahrenheit sama dengan 32.
        return(f"Suhu {c} Celcius setara dengan {Celcius} Fahrenheit") #Jika iya, maka fungsi akan mengembalikan string 
                                                                        #yang menyatakan konversi suhu dari Celcius ke Fahrenheit.
    elif c == 0 : # Kondisi ini memeriksa apakah suhu yang diinput dalam Celcius sama dengan 0.
        return(f"Suhu {f} Fahrenheit setara dengan {Fahrenheit} Celcius") # Jika iya, maka fungsi akan mengembalikan string 
                                                                        #yang menyatakan konversi suhu dari Fahrenheit ke Celcius
    else : #Jika kedua kondisi sebelumnya tidak terpenuhi, artinya nilai c dan f yang diinput tidak sama dengan nilai default, 
        return(f"Suhu {c} Celcius sama dengan {f} Fahrenheit") #maka fungsi akan mengembalikan string 
                                                            #yang menyatakan bahwa suhu dari c Celcius sama dengan f Fahrenheit.

print(konversi_suhu(c = 40)) #Menampilkan konversi suhu dari 40 Celcius ke Fahrenheit 
print(konversi_suhu(f = 95)) #Menampilkan konversi suhu dari 95 Fahrenheit ke Celcius
print(konversi_suhu(30)) #Menampilkan dari 30 Celcius ke Fahrenheit karena nilai c diberikan.
print(konversi_suhu()) #Menampilkan konversisuhu dari 0 Celcius ke 32 Fahrenheit 
                        #karena tidak ada nilai yang diberikan untuk c atau f.