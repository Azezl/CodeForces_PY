n = int(input())

lst = []

for i in range(n):
    temp=input()
    lst.append(temp)

initial = 0

for i in range(n):
    if '++' in lst[i]:
        initial = initial+1
    else:
        initial = initial -1

print(initial)