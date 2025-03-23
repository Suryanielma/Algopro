#https://www.spoj.com/problems/ENPRIME/
#Baca bilangan bulat X dari input dan hitung faktorial dari X.
#Faktorial adalah fungsi yang mengalikan suatu bilangan untuk 
# setiap bilangan positif yang mendahuluinya X! = X * (X-1) * (X- 2) * ... * 1
#input
#Bilangan bulat X.
#output
#Faktorial dari X.

def menghitungFaktorial(x): #menghitung faktorial dari x
    if x < 0: #jika x kurang dri 0
        return "Faktorial tidak terdefinisi untuk bilangan negatif" #akan mencetak tulisan tsb
    elif x == 0 or x == 1: #namun jika x sama dengan 0 atau x sama dengan 1
        return 1 #akan mengembalikan nilai 1
    else:
        faktorial = 1 #faktorial sam dengan 1
        for i in range(2, x + 1): #perulangan for menghitung nilai dari x
            faktorial *= i #mengalikan faktorial
        return faktorial #mengembalikan nilai faktorial
X = int(input()) #memasukkan nilai x
hasil = menghitungFaktorial(X) #menghitung hasil faktorial
print(f"{hasil}") #mencetak hsil dari faktorial yang sudah diinput.