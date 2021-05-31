n = int(input())
cases = []
ans = []
for i in range(n):
    str1 = ""
    temp = int(input())
    factor = 1
    num = 0
    while temp > 0:
        if temp % 10 == 0:
            temp = int(temp / 10)
        else:
            k = temp % 10
            k = k * factor
            num = num + 1
            str1 = str1 + str(k) + " "
            temp = int(temp / 10)
        factor = factor * 10

    ans.append([num, str1])

for i in range(n):
    print(ans[i][0])
    print(ans[i][1])
