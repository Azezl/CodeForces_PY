n = int(input())

lst = [100, 20, 10, 5, 1]
bills = 0

for i in lst:
    if int(n / i) >= 0:
        bills = bills + int(n / i)
        n = n % i

print(bills)
