year = int(input())
year = year + 1
while True:
    num = year
    lst = []
    flag = 0
    while num > 0:
        rem = num % 10
        num = int(num / 10)
        lst.append(rem)

    if len(dict.fromkeys(lst)) == 4:
        print(year)
        break
    year = year + 1
