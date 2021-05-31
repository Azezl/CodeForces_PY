n = input()

X_Levels = (input()).split()
Y_Levels = (input()).split()

combined_list = X_Levels + Y_Levels
flag = 0

for i in range(1, (int(n) + 1)):
    if str(i) not in set(combined_list):
        print("Oh, my keyboard!")
        flag = 1
        break

if flag == 0:
    print("I become the guy.")
