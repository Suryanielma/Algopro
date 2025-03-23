# x = 7
# y = 9
# x+= y
# print(x)


# jumlah = [1,2,3,4,5,6,7,8,9]
# print(jumlah[-4])

a = [(x, y)
     for x in [0, 3, 5]
     for y in [5, 4, 0]if x!=y]
print(a)