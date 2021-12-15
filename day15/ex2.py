import heapq

list_input = open('input.txt', 'r').read().split('\n')

og_map = [[int(c) for c in list] for list in list_input]
size_line = len(list_input)
size_col = len(list_input[0])
map = [[0 for i in range(size_col * 5)] for j in range(size_line * 5)]

for y in range(size_line * 5):
    for x in range(size_col * 5):
        map[y][x] = (og_map[y % size_line][x % size_col] + x // size_col + y // size_line - 1) % 9 + 1

heap = [(0, 0, 0)]
map_hist = [[0 for _ in range(size_col * 5)] for i in range(size_line * 5)]

end = False
while not end:
    sum, x, y = heapq.heappop(heap)
    if map_hist[y][x]:
        continue
    if y == len(map) - 1 and x == len(map[0]) - 1:
        print(sum + map[y][x] - map[0][0])
        end = True
    map_hist[y][x] = 1
    for ax, ay in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= ay < len(map) and 0 <= ax < len(map[0]):
            heapq.heappush(heap, (sum + map[y][x], ax, ay))

