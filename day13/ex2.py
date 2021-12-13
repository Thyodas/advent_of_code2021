list_input = open('input.txt', 'r').read().split('\n')

dot_list = []
instructions = []
i = 0
while list_input[i] != "":
    split = list_input[i].split(',')
    dot_list.append([int(split[0]), int(split[1])])
    i += 1
i += 1
while i < len(list_input):
    instructions.append(list_input[i])
    i += 1

x_max = 0
y_max = 0
for dot in dot_list:
    x_max = max(dot[0], x_max)
    y_max = max(dot[1], y_max)

map = [["." for j in range(x_max + 1)] for i in range(y_max + 1)]
for dot in dot_list:
    map[dot[1]][dot[0]] = "#"

def count_dot(map):
    count = 0
    for line in map:
        for el in line:
            if el == "#":
                count += 1
    return count

def folded_y(map, y):
    new_map = [el for el in map[:y]]
    to_fold = [el for el in map[y + 1:]]
    new_map.reverse()
    for j, line in enumerate(to_fold):
        for i, el in enumerate(line):
            if el == "#":
                new_map[j][i] = "#"
    return list(reversed(new_map))

def folded_x(map, x):
    new_map = [el[:x] for el in map]
    to_fold = [el[x + 1:] for el in map]
    new_map = [list(reversed(el)) for el in new_map]
    for j, line in enumerate(to_fold):
        for i, el in enumerate(line):
            if el == "#":
                new_map[j][i] = "#"
    return [list(reversed(el)) for el in new_map]

for instruction in instructions:
    split = instruction.split('=')
    if split[0] == "fold along x":
        map = folded_x(map, int(split[1]))
    elif split[0] == "fold along y":
        map = folded_y(map, int(split[1]))

for line in map:
    print(line)