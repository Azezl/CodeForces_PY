lst = (input()).split()

n = int(lst[0])
m = int(lst[1])

outer = []

for i in range(n):
    temp = []
    for j in range(m):
        temp.append('#')
    outer.append(temp)

tem = 1

while tem < n:
    if ((tem+1)/2) % 2 == 1:
        for i in range(m-1):
            outer[tem][i] = '.'
    else:
        for i in range(1,m):
            outer[tem][i] = '.'
    tem = tem + 2

ans = []

for i in range(n):
    str1 = ""
    for j in range(m):
        str1 = str1 + outer[i][j]
    ans.append(str1)

for i in range(len(ans)):
    print(ans[i])