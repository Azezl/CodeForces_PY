n = int(input())
lst = (input()).split()

flag = 0

for i in range(n):
    if lst[i] == '1':
        print("HARD")
        flag = 1
        break

if flag == 0:
    print("EASY")
