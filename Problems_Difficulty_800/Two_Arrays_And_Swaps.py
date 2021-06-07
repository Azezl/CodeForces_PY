n = []
k = []
ans = []

for i in range(int(input())):
    inp = (input()).split()
    n = int(inp[0])
    k = int(inp[1])
    A = (input()).split()
    B = (input()).split()
    for j in range(int(inp[0])):
        A[j] = int(A[j])
        B[j] = int(B[j])
    A.sort()
    B.sort(reverse=True)
    a = 0
    b = 0
    while ((n > 0) & (k > 0)):
        if A[a] < B[b]:
            A[a] = B[b]
            a = a + 1
            b = b + 1
            k = k - 1
        else:
            break
        n = n - 1
    ans.append(sum(A))

for i in range(len(ans)):
    print(ans[i])
