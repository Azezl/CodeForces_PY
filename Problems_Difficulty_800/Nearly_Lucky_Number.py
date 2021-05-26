num = list(input())

Num_Lucky_Digits = 0

for i in range(len(num)):
    if (num[i] == '4') | (num[i] == '7'):
        Num_Lucky_Digits = Num_Lucky_Digits + 1

if (Num_Lucky_Digits == 4) | (Num_Lucky_Digits == 7):
    print("YES")

else:
    print("NO")
