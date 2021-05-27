n = int(input())
lst = (input()).split()
gifted_list = []
for i in range(n+1):
    gifted_list.append(0)

for i in range(n):
    temp = int(lst[i])
    gifted_list[(temp-1)] = i+1

str1 = ""
for i in range(n):
    str1 = str1 + str(gifted_list[i])+ " "

print(str1)