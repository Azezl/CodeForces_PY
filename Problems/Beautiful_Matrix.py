outer = []

for i in range(5):
    inner = input().split()
    outer.append(inner)

r=0
c=0
for i in range(5):
    for j in range(5):
        if outer[i][j] == '1':
            r = i
            c = j
            break

moves = abs(r-2)+abs(c-2)

print(moves)


