num = int(input())
ans = []

for i in range(num):
    lst = (input()).split()
    x = int(lst[0])
    y = int(lst[1])
    n = int(lst[2])
    if ((n - (n % x) + y) <= n):
        ans.append((n - (n % x) + y))
    else:
        ans.append((n - (n % x) - (x - y)))

for i in range(num):
    print(ans[i])
