lst = []
for i in range(int(input())):
    tem = (input()).split()
    a = int(tem[0])
    b = int(tem[1])
    moves = int((abs(a - b) + 9)/10)
    lst.append(moves)

for i in lst:
    print(i)
