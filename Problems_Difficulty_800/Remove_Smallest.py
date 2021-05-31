# Erroneous Code
# Need to look into in the future
def ispossible(moves, cases):
    if len(cases) > (moves + 1):
        return 'NO'

    cases.sort()
    if len(cases) == 1:
        return 'YES'

    for j in range(1, len(cases)):
        if abs(int(cases[j]) - int(cases[j-1])) > 1:
            return 'NO'
    return 'YES'


n = int(input())

case = []
move = []

for i in range(n):
    move.append(int(input()))
    case.append((input().split()))
possible = []
for i in range(n):
    ans = ispossible(move[i], case[i])
    possible.append(ans)

for i in range(n):
    print(possible[i])
