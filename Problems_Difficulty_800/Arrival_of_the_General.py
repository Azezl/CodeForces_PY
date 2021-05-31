n = int(input())
lst = (input()).split()

maxi = -999
mini = 9999

maxi_index = -1
mini_index = -1

for i in range(n):
    if int(lst[i]) > maxi:
        maxi = int(lst[i])
        maxi_index = i

    if int(lst[i]) <= mini:
        mini = int(lst[i])
        mini_index = i

#print(maxi_index,mini_index)
ans = (maxi_index) + (n - (mini_index + 1))

if maxi_index > mini_index:
        ans = ans - 1

print(ans)