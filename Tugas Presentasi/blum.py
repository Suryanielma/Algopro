#https://www.spoj.com/problems/DIVSUM

t = int(input())
for i in range(t):
    n = int(input())
    divisors = [j for j in range(1, n) if n % j == 0]
    print(sum(divisors))
