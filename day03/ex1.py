list_input = open('input.txt', 'r').read().split('\n')

common = [0 for i in range(len(list_input[0]))]

for element in list_input:
    for (i, digit) in enumerate(element):
        if digit == "0":
            common[i] -= 1
        elif digit == "1":
            common[i] += 1

gamma = ""
epsilon = ""
for nb in common:
    gamma += str(int(nb > 0))
    epsilon += str(int(nb <= 0))

print(int(gamma, 2) * int(epsilon, 2))