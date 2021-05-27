n = int(input())
outer_list = []

for i in range(n):
    inner_list = (input()).split()
    outer_list.append(inner_list)

num_free_rooms = 0

for i in range(n):
    if ((int(outer_list[i][1]))-(int(outer_list[i][0]))) >= 2:
        num_free_rooms = num_free_rooms + 1

print(num_free_rooms)