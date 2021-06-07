n = int(input())
lst = (input()).split()

for i in range(len(lst)):
    lst[i] = int(lst[i])


print((max(lst) * len(lst)) - sum(lst))