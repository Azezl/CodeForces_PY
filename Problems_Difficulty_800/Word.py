input_string = input()
lst = list(input_string)

num_upper = 0
num_lower = 0

for i in range(len(lst)):
    if lst[i].isupper():
        num_upper = num_upper + 1
    else:
        num_lower = num_lower + 1

if num_upper > num_lower:
    print(input_string.upper())

else:
    print(input_string.lower())
