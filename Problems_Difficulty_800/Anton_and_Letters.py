input_string = input()

lst = []

for i in range(len(input_string)):
    if input_string[i] not in {'{', ' ', ',','}'}:
        lst.append(input_string[i])

print(len(set(lst)))
