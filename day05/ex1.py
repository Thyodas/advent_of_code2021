list_input = open('input.txt', 'r').read().split('\n')

table = []
for line in list_input:
    current = []
    set = line.split(" -> ")
    for i in range(2):
        xy = []
        split = set[i].split(",")
        xy.append(int(split[0]))
        xy.append(int(split[1]))
        current.append(xy)
    table.append(current)


max_x = 0
max_y = 0
for line in table:
    for xy in line:
        if max_x < xy[0]:
            max_x = xy[0]
        if max_y < xy[1]:
            max_y = xy[1]

max_x += 1
max_y += 1

print(max_x, max_y)
map = [[0 for j in range(max_x)] for i in range(max_y)]

for set in table:
    x1 = set[0][0]
    y1 = set[0][1]
    x2 = set[1][0]
    y2 = set[1][1]
    if y1 == y2:
        y = y1
        for x in range(x1, x2 + 1):
            map[y][x] += 1
        for x in range(x2, x1 + 1):
            map[y][x] += 1
    elif x1 == x2:
        x = x1
        for y in range(y1, y2 + 1):
            map[y][x] += 1
        for y in range(y2, y1 + 1):
            map[y][x] += 1

nb_intersect = 0
for line in map:
    for nb in line:
        if nb > 1:
            nb_intersect += 1

print(nb_intersect)