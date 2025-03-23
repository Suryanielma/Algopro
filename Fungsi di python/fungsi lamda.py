# nilaiKuadrat = lambda nilai : nilai**2
# print(nilaiKuadrat(3))


# hasilKali = lambda x,y : x*y
# print(hasilKali(x=3,y=2))


# hasil = lambda x, y : print(x)

# hasil = lambda x, y : x*y*y



def factorial(angka):
    # base case
    if angka == 1 or angka == 0:
       return (angka)

    # recursive case
    else:
       return (angka*factorial(angka-1)) #step reduction
 
bil = int(input("Masukan Bilangan : "))
print("Nilai faktorial dari "+ str(bil) + " adalah : " + str(factorial(bil)))