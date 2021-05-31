n = int(input())

fractions_list = (input()).split()
volume = 0.0

for i in range(n):
    volume = volume + ((int(fractions_list[i]))/n)

print(volume)