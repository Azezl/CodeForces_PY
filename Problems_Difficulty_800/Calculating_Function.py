n = int(input())
even = 0
odd = 0
if n % 2 == 0:
    even = int(n / 2)
    odd = int(n / 2)

else:
    even = int(n / 2)
    odd = int(n / 2) + 1

ans = int((even * (even + 1))) - int(odd * odd)
print(ans)
