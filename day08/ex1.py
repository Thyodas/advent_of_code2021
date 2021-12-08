list_input = open('input.txt', 'r').read().split('\n')

output_value = [el.split(' ')[11:] for el in list_input]

size_dict = {}

for el in output_value:
    for digit in el:
        size = len(digit)
        if size not in size_dict:
            size_dict[size] = 0
        size_dict[size] += 1

print(size_dict[2] + size_dict[4] + size_dict[3] + size_dict[7])