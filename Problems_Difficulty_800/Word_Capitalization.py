str1 = input()
lst = list(str1)
lst[0] = lst[0].upper()
str2 = ""

for i in range(len(lst)):
    str2 = str2 + lst[i]
print(str2)
