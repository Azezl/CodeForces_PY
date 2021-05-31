num1 = list(input())
num2 = list(input())

str1 = ""

for i in range(len(num1)):
    if num1[i] == num2[i]:
        str1 = str1 + '0'
    else:
        str1 = str1 + '1'

print(str1)