list_input = open('input.txt', 'r').read().split('\n')

iea_str = list_input[0]

map = [[char for char in line] for line in list_input[2:]]

def increase_infinite_size_map(map):
    new_map = []
    new_col_size = len(map[0]) + 20
    for _ in range(10):
        new_map.append(["." for _ in range(new_col_size)])
    for line in map:
        new_map.append(["."] * 10 + line + ["."] * 10)
    for _ in range(10):
        new_map.append(["." for _ in range(new_col_size)])
    return new_map

def get_line_str(old_map, x, y) -> str:
    str = ""
    for my in range(y - 1, y - 1 + 3):
        for mx in range(x - 1, x - 1 + 3):
            str += old_map[my][mx]
    return str

def to_binary(line_str) -> int:
    binary = ""
    for c in line_str:
        if c == '.':
            binary += '0'
        else:
            binary += '1'
    return int(binary, 2)

def enhance_map(map):
    increased_map = increase_infinite_size_map(map)
    enhanced_map = [['.'] * (len(increased_map[0]) - 2) for _ in range(len(increased_map) - 2)]
    for y in range(1, len(increased_map) - 1):
        for x in range(1, len(increased_map[0]) - 1):
            enhanced_map[y - 1][x - 1] = iea_str[to_binary(get_line_str(increased_map, x, y))]
    return enhanced_map

def count_light(map) -> int:
    count = 0
    for line in map:
        for el in line:
            if el == "#":
                count += 1
    return count

for i in range(25):
    print(i)
    for _ in range(2):
        map = enhance_map(map)
    map = map[16:-16]
    map = [line[16:-16] for line in map]

#print(*["".join(line) for line in map], sep='\n')
print(count_light(map))