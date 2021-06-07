lst = (input()).split()
k = int(lst[0])
r = int(lst[1])
i = 0
while True:
    if (k * i) % 10 == 0:
        if i != 0:
            print(i)
            break

    elif ((k * i) % 10) == r:
        print(i)
        break
    i = i + 1