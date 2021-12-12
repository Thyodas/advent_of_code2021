from collections import Counter

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

def invalid(list, item):
    multiple = False
    counter = Counter(list)
    for i in list:
        if i.islower() and counter[i] >= 2:
            multiple = True
            break
    if counter[item] >= 1 and multiple:
        return True
    return False

def count_rec(graph, pos="start", history=[]):
    if pos == "end":
        return 1
    if pos == "start" and len(history) != 0:
        return 0
    if pos.islower() and invalid(history, pos):
        return 0
    next_list = graph[pos]
    sum = 0
    for next in next_list:
        sum += count_rec(graph, next, history + [pos])
    return sum

print(count_rec(graph))