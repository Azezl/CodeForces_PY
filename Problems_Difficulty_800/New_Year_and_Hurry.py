lst = (input()).split()

n = int(lst[0])
tem = 240 - int(lst[1])
maxi = 0
i = 5

while (tem > 0) & (n > 0):
    if int(tem/i) >= 1:
        tem = tem - i
        n = n - 1
        maxi = maxi + 1
        i = i + 5
    else:
        break

print(maxi)