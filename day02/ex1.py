list_input = open('input.txt', 'r').read().split('\n')

horizontal = 0
depth = 0

for element in list_input:
    split = element.split(' ')
    if split[0] == "up":
        depth -= int(split[1])
    elif split[0] == "down":
        depth += int(split[1])
    elif split[0] == "forward":
        horizontal += int(split[1])

print(horizontal * depth)