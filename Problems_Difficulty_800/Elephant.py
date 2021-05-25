X = int(input())

steps: int = 0
i = 5

while i > 0:
    steps = steps + int((X / i))
    X = X % i
    if X == 0:
        break
    i = i - 1

print(steps)
