n = int(input())
lst = (input()).split()

maxi = int(lst[0])
mini = int(lst[0])

amazing = 0

for i in range(1, n):
    if int(lst[i]) > maxi:
        amazing = amazing + 1
        maxi = int(lst[i])
    elif int(lst[i]) < mini:
        amazing = amazing + 1
        mini = int(lst[i])

print(amazing)
