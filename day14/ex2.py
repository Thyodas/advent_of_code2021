from collections import Counter

list_input = open('input.txt', 'r').read().split('\n')

polymer = list_input[0]

dict_pair = {}

for line in list_input[2:]:
    split = line.split(' -> ')
    if split[0] not in dict_pair:
        dict_pair[split[0]] = split[1]

dict_result = {k: 0 for k, v in dict_pair.items()}
for a, b in zip(polymer, polymer[1:]):
    dict_result[a + b] = polymer.count(a + b)

def put_btw():
    for key, value in list(dict_result.items()).copy():
        if value > 0:
            btw = dict_pair[key]
            dict_result[key] -= value
            dict_result[key[0] + btw] += value
            dict_result[btw + key[1]] += value

count = {}
def count_letter():
    for key, value in dict_result.items():
        if key[0] not in count:
            count[key[0]] = 0
        if key[1] not in count:
            count[key[1]] = 0
        count[key[0]] += value

for _ in range(40):
    put_btw()

count_letter()
count[polymer[-1]] += 1
sort = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
keys = list(sort.keys())

print(count[keys[-1]] - count[keys[0]])