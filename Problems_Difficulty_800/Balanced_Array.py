# NOT SOLVED
n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

ans = []

for i in range(n):
    if int(lst[i]/2) % 2 == 1:
        ans.append("NO")
    else:
        ans.append("YES")
        lst1 = []
        lst2 = []
        str1 = ""
        k = 0
        consti = 4
        for j in range(lst[i]):
            if j < int(lst[i]/2):
                tempo = (2*(consti))
                lst1.append(int(tempo))
                str1 = str1 + str(int(tempo)) + " "
                consti = consti + 4
            else:
                if j < int(3*lst[i]/4):
                    str1 = str1 + str(lst1[k]-1) + " "
                    k = k + 1
                else:
                    str1 = str1 + str(lst1[k]+1) + " "
                    k = k + 1
        ans.append(str1)

for i in range(len(ans)):
    print(ans[i])


