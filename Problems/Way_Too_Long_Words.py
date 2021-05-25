n = int(input())
inputlist = []

for i in range(n):
    inp = input()
    inputlist.append(inp)

for i in range(n):
    if len(inputlist[i]) > 10:
        first = inputlist[i][0]
        second = inputlist[i][-1]
        leng = len(inputlist[i]) - 2
        str1 = first + str(leng) + second
        inputlist[i] = str1


for word in inputlist:
    print(word)