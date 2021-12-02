list_input = open('input.txt', 'r').read().split('\n')

horizontal = 0
depth = 0
aim = 0

for element in list_input:
    split = element.split(' ')
    if split[0] == "up":
        aim -= int(split[1])
    elif split[0] == "down":
        aim += int(split[1])
    elif split[0] == "forward":
        horizontal += int(split[1])
        depth += aim * int(split[1])

print(horizontal * depth)