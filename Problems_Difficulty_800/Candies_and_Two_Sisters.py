n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

ans = []

for i in range(len(lst)):
    if lst[i] == 0 | lst[i] == 1 | lst[i] == 2:
        ans.append(lst[i])

    else:
        temp = lst[i] - (int(lst[i]/2)+1)
        ans.append(temp)

for i in ans:
    print(i)