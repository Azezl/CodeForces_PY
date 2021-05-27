n = int(input())
str1 = ""

for i in range(n):
    if (i % 2 == 0) & (i == n - 1):
        str1 = str1 + "I hate it"
    elif i % 2 == 0:
        str1 = str1 + "I hate that" + " "

    if (i % 2 == 1) & (i == n - 1):
        str1 = str1 + "I love it"
    elif i % 2 == 1:
        str1 = str1 + "I love that" + " "

print(str1)
