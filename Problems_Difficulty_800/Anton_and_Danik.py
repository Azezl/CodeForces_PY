num = int(input())
lst = list(input())

Anton = 0
Danik = 0

for i in range(num):
    if lst[i] == 'A':
        Anton = Anton + 1
    else:
        Danik = Danik + 1

if Anton > Danik:
    print("Anton")
elif Danik > Anton:
    print("Danik")
else:
    print("Friendship")
