lst = (input()).split()

r = int(lst[0])
b = int(lst[1])

days_diff = 0
days_same = 0

if r<b:
    days_diff = days_diff + r
    days_same = days_same + int((b-r)/2)

else:
    days_diff = days_diff + b
    days_same = days_same + int((r-b)/2)

print(days_diff,days_same)

