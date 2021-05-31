guest = input()
host = input()

pile = input()

lst = []

for i in range(len(pile)):
    lst.append(pile[i])

flag = 0

for i in range(len(guest)):
    if guest[i] not in lst:
        flag = 1
        break

    if guest[i] in lst:
        lst.remove(guest[i])

for i in range(len(host)):
    if host[i] not in lst:
        flag = 1
        break

    if host[i] in lst:
        lst.remove(host[i])


if len(lst) != 0:
    flag = 1

if flag == 1:
    print('NO')

else:
    print('YES')