import copy

list_input = open('input.txt', 'r').read().split('\n')

map = [[char for char in line] for line in list_input]

def move_east(map):
    col = len(map[0])
    new_map = copy.deepcopy(map)
    moved = False
    for y in range(len(map)):
        for x in range(col):
            if map[y][x] == '>':
                if map[y][(x + 1) % col] == '.':
                    new_map[y][(x + 1) % col] = '>'
                    new_map[y][x] = '.'
                    moved = True
    return moved, new_map

def move_south(map):
    lines = len(map)
    new_map = copy.deepcopy(map)
    moved = False
    for y in range(lines):
        for x in range(len(map[0])):
            if map[y][x] == 'v':
                if map[(y + 1) % lines][x] == '.':
                    new_map[y][x] = '.'
                    new_map[(y + 1) % lines][x] = 'v'
                    moved = True
    return moved, new_map

def step(map):
    moved, map = move_east(map)
    moved2, map = move_south(map)
    return moved or moved2, map

i = 0
moved = True
while moved:
    moved, map = step(map)
    i += 1

print(i)
#print(*map, sep='\n')