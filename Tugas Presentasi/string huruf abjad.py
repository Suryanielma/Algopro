#https://www.spoj.com/problems/MOZPAS

# 7 2 
# 5 1

a, b = map(int, input().split())
string = 'abcdefghijklmnopqrstuvwxyz'
result = string[:b] * (a // b) + string[:a % b]
print(result)

