n = int(input())

input_string = ((input()).upper())

lst = []
for i in range(len(input_string)):
    lst.append(input_string[i])

if len(set(lst)) == 26:
    print('YES')

else:
    print('NO')
