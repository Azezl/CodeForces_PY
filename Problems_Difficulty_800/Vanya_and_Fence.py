lst = (input()).split()
n = int(lst[0])
h = int(lst[1])

height_list = (input()).split()
min_width = 0

for i in range(n):
    if (int(height_list[i])) > h:
        min_width = min_width + 2

    else:
        min_width =min_width + 1

print(min_width)