import math

n = int(input())


def is_prime(num):
    for i in range(2, (int(math.sqrt(num))+1)):
        if num % i == 0:
            return 1
    return 0


while True:
    if n % 2 == 0:
        if is_prime(n) == 1:
            a = int(n/2)
            b = a
        while True:
            a = a - 1
            b = b + 1
            if (is_prime(a) & is_prime(b)) == 1:
                print(a,b)
                break
        break

    else:
        if int(n/2) % 2 == 0:
            a = int(n/2)
            b = a + 1
        else:
            a = int(n/2) + 1
            b = a - 1
        while True:
            if is_prime(b) == 1:
                print(a, b)
                break
            else:
                a = a - 2
                b = b + 2
        break
