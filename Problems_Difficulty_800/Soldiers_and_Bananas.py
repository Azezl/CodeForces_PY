input_string = input()
lst = input_string.split()

k = int(lst[0])
n = int(lst[1])
w = int(lst[2])

total_required = (k * w * (w + 1)) / 2

if n > total_required:
    print(0)
else:
    answer = total_required - n
    print(int(answer))
