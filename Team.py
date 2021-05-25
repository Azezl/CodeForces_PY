n=int(input())

outer = []
total = 0

for i in range(n):
    inp = input()
    inner = inp.split()
    outer.append(inner)

for i in range(n):
    sum = 0
    for j in range(3):
        sum = sum + int(outer[i][j])
    if sum >= 2 :
        total =total + 1

print(total)