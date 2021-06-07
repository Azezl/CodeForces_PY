n = int(input())

lst = (input()).split()

one_arr = []
two_arr = []
three_arr = []

for i in range(len(lst)):
    if lst[i] == '1':
        one_arr.append(i + 1)
    elif lst[i] == '2':
        two_arr.append(i + 1)
    else:
        three_arr.append(i + 1)

i = len(one_arr)
j = len(two_arr)
k = len(three_arr)

tem = min([i, j, k])

ans = []

for i in range(tem):
    str1 = str(one_arr[i]) + " " + str(two_arr[i]) + " " + str(three_arr[i]) + " "
    ans.append(str1)
print(tem)
for i in range(tem):
    print(ans[i])
