n = int(input())

lst = []
groups = 1

for i in range(n):
    lst.append(int(input()))


for i in range(1, n):
    if lst[i-1] != lst[i]:
        groups = groups + 1

print(groups)
