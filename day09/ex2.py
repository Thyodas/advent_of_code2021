list_input = open('input.txt', 'r').read().split('\n')

map = [[int(c) for c in line] for line in list_input]

def check(map, x, y):
    nb = map[y][x]
    if nb == 9 or nb == -1:
        return 0
    sum = 0
    map[y][x] = -1
    if y + 1 < len(map):
        sum += check(map, x, y + 1)
    if y - 1 >= 0:
        sum += check(map, x, y - 1)
    if x + 1 < len(map[0]):
        sum += check(map, x + 1, y)
    if x - 1 >= 0:
        sum += check(map, x - 1, y)
    return 1 + sum

count = []
for y in range(len(map)):
    for x in range(len(map[0])):
        count.append(check(map, x, y))

count.sort(reverse=True)
print(count[0] * count[1] * count[2])
