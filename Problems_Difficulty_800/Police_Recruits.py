n = int(input())

untreated = 0
recruits = 0
lst = (input()).split()

for i in range(n):
    k = int(lst[i])
    if k > 0:
        recruits = recruits + k
    else:
        if recruits > 0:
            recruits = recruits - 1
        else:
            untreated = untreated + 1

print(untreated)
