k = int(input())
l_var = int(input())
m = int(input())
n = int(input())
d = int(input())

harmed = 0

for i in range(1, (d + 1)):
    if ((i % k == 0) | (i % l_var == 0) | (i % m == 0) | (i % n == 0)):
        harmed = harmed + 1
print(harmed)
