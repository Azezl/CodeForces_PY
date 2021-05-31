n = int(input())

lst = []

for i in range(n):
    temp = (input()).split()
    lst.append(temp)

ans = 0

for i in range(n):
    for j in range(n):
        if lst[i][0] == lst[j][1]:
            ans = ans + 1

print(ans)
