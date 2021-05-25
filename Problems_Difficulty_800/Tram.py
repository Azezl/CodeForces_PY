n = int(input())
outer_lst = []

for i in range(n):
    inner_lst = (input()).split()
    outer_lst.append(inner_lst)

maxi = -1

# Total Number Of Passengers after every given stop is defined by t
t = 0

for i in range(n):
    if i == 0:
        t = int(outer_lst[i][1])
    else:
        t = t - int(outer_lst[i][0]) + int(outer_lst[i][1])

    if t > maxi:
        maxi = t

print(maxi)
