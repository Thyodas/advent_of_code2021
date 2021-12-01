list_input = open('input.txt', 'r').read().split('\n')

count = 0
last = 0

last = int(list_input[0])
for element in list_input[1:]:
    nb = int(element)
    if nb > last:
        count += 1
    last = nb

print(count)