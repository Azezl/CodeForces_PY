n = int(input())
str1 = input()
answer = 0
prev = str1[0]

for i in range(n):
    if i == 0:
        continue
    if str1[i] == prev:
        answer = answer + 1
    else :
        prev = str1[i]
print(answer)

