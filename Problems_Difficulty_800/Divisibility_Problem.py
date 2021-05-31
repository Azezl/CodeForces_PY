n = int(input())
ans_lst = []

for i in range(n):
    temp_lst = (input()).split()
    temp = int(temp_lst[0]) % int(temp_lst[1])
    if temp == 0:
        ans_lst.append(0)
        continue
    ans_lst.append(int(temp_lst[1]) - temp)

for i in range(n):
    print(int(ans_lst[i]))
