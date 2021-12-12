list_input = open('input.txt', 'r').read().split('\n')

graph = {}

def add(graph, parent, next):
    if parent not in graph:
        graph[parent] = []
    if next not in graph[parent]:
        graph[parent].append(next)

for line in list_input:
    splited = line.split('-')
    add(graph, splited[0], splited[1])
    add(graph, splited[1], splited[0])

def count_rec(graph, pos="start", history=[]):
    if pos == "end":
        return 1
    if pos.islower() and pos in history:
        return 0
    next_list = graph[pos]
    sum = 0
    for next in next_list:
        sum += count_rec(graph, next, history + [pos])
    return sum

print(count_rec(graph))