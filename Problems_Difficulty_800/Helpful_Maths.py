str1 = input()
lst = list(str1)
newlst = []

for i in range(len(lst)):
    if i % 2 == 1:
        continue
    newlst.append(int(lst[i]))

newlst.sort()

for i in range(len(lst)):
    if i % 2 == 1:
        continue
    lst[i] = str(newlst[int(i / 2)])

str2 = ''

for i in range(len(lst)):
    str2 = str2+lst[i]
    
print(str2)
