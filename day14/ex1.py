from collections import Counter

list_input = open('input.txt', 'r').read().split('\n')

polymer = list_input[0]

dict_pair = {}

for line in list_input[2:]:
    split = line.split(' -> ')
    if split[0] not in dict_pair:
        dict_pair[split[0]] = split[1]

def put_btw(polymer, dict_pair):
    new = []
    for i in range(len(polymer) - 1):
        new.append(polymer[i])
        btw = dict_pair[polymer[i:i+2]]
        new.append(btw)
    new.append(polymer[-1])

    return "".join(new)

for _ in range(40):
    polymer = put_btw(polymer, dict_pair)

counter = dict(Counter(polymer))
sort = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}
keys = list(sort.keys())
print(counter[keys[-1]] - counter[keys[0]])