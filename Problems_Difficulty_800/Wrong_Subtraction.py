input_string = input()
lst = input_string.split()

Number = int(lst[0])
Number_of_subtractions = int(lst[1])

for i in range(Number_of_subtractions):
    if Number % 10 == 0:
        Number = Number / 10
    else:
        Number = Number - 1

print(int(Number))

