n = int(input())
sides = 0

for i in range(n):
    temp = input()

    if temp == "Tetrahedron":
        sides = sides + 4

    elif temp == "Cube":
        sides = sides + 6

    elif temp == "Octahedron":
        sides = sides + 8

    elif temp == "Dodecahedron":
        sides = sides + 12

    else:
        sides = sides + 20

print(sides)