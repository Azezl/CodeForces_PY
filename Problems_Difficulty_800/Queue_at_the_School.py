temp_lst = (input()).split()
time = int(temp_lst[1])

Queue_String = input()
lst = list(Queue_String)

for j in range(time):
    i = 0
    while i < (len(lst)-1):
        if (lst[i] == 'B') & (lst[i + 1] == 'G'):
            temp = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = temp
            i = i + 1
        i = i + 1

str1 = ""

for i in lst:
    str1 = str1 + i
print(str1)