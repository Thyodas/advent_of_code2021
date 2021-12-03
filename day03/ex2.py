list_input = open('input.txt', 'r').read().split('\n')



def determine_common(list, pos):
    common = 0

    for element in list:
            if element[pos] == "0":
                common -= 1
            elif element[pos] == "1":
                common += 1

    return str(int(common >= 0))

pos = 0
list_generator = list_input.copy()
list_scrubber = list_input.copy()
for pos in range(len(list_input[0])):
    common_generator = determine_common(list_generator, pos)
    for element in list_generator.copy():
        if len(list_generator) == 1:
            break
        if element[pos] != common_generator:
            list_generator.remove(element)
    common_scrubber = determine_common(list_scrubber, pos)
    for element in list_scrubber.copy():
        if len(list_scrubber) == 1:
            break
        if element[pos] == common_scrubber:
            list_scrubber.remove(element)

print(int(list_scrubber[0], 2) * int(list_generator[0], 2))