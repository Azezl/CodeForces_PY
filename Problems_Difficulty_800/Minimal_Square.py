ans = []

for i in range(int(input())):
    inp = (input()).split()
    a = int(inp[0])
    b = int(inp[1])
    if a < b:
        if ((2*a)<b):
            a = b
            ans.append(a*a)
            continue
        tem = (2*a)*(2*a)
        ans.append((tem))
    else:
        if (2*b) < a:
            b = a
            ans.append(b*b)
            continue
        tem = (4*b*b)
        ans.append(tem)

for i in range(len(ans)):
    print(ans[i])