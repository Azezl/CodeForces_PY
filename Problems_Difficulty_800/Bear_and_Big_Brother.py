input_string = input()
lst = input_string.split()
a = int(lst[0])
b = int(lst[1])

Number_of_years = 0
while a <= b:
    a = a * 3
    b = b * 2
    Number_of_years = Number_of_years + 1

print(Number_of_years)
