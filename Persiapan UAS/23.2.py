def fungsi1(n):
    if n == 1:
        return 1
    else:
        return n*fungsi1(n-1)#untuk menghitung faktorial
print(fungsi1(8))



# def fungsi2(data):
#     out = dict()
#     for d in data:
#         out [d] = out.get(d, 0) + 1
#     return out 
# print(fungsi2("UMS SOLO"))
    