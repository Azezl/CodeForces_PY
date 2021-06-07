lst = (input()).split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

lst.sort()

dist = abs(lst[1]-lst[0]) + abs(lst[2] - lst[1])

print(int(dist))