list_input = open('input.txt', 'r').read().split('\n')

count = 0
last = 0
for i in range(len(list_input)):
    sum = 0
    for element in list_input[i:i+3]:
        sum += int(element)
    if sum > last and i != 0:
        count += 1
    last = sum

print(count)
"""
last = int(sum_dict.keys()[0])
for element in sum_dict.keys()[1:]:
    if int(sum_dict[element]) > last:
        count += 1
    last = int(sum_dict[element])

print(count)"""