inp = (input()).split()
n = int(inp[0])
k = int(inp[1])

lst = (input()).split()

num = 0

for i in range(len(lst)):
    lst[i] = int(lst[i])
    if (lst[i] + k) <= 5:
        num = num + 1

print(int(num/3))