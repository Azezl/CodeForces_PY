str1 = input()
inlist = str1.split()

n = int(inlist[0])
k = int(inlist[1])


advancers = 0
score = input()
scores = score.split()

for i in range(n):
    if int(scores[i]) == 0:
        continue
    if int(scores[i]) >= int(scores[k - 1]):
        advancers = advancers + 1

print(advancers)
