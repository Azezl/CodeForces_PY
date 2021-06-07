lst = (input()).split()

for i in range(len(lst)):
    lst[i] = int(lst[i])

lst.sort()

largest = lst[3] - lst[0]
middle = lst[2] - largest
smallest = lst[0] - middle

print(smallest,middle,largest)
