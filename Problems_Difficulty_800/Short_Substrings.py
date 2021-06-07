n = int(input())
lst = []
for i in range(n):
    lst.append(input())

ans = []
for i in range(n):
    str1 = lst[i][0:2]
    for j in range(2, len(lst[i]), 2):
        if lst[i][j - 1] == lst[i][j]:
            str1 = str1 + lst[i][j + 1]
        else:
            str1 = str1 + lst[i][j:j + 2]
    ans.append(str1)
for i in range(n):
    print(ans[i])
