first = list(input())
second = list(input())

flag = -999

for i in range(len(first)):
    if (first[i].upper() < second[i].upper()):
        flag = -1
        print(flag)
        break
    elif (first[i].upper() > second[i].upper()):
        flag = 1
        print(flag)
        break

if flag == -999:
    print(0)
