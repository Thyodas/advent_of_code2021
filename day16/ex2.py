list_input = open('input.txt', 'r').read().split('\n')

def leading_zero(str):
    new = ""
    for i in range(4 - len(str)):
        new += "0"
    return new + str
binary = ""
for letter in list_input[0]:
    binary += leading_zero(str(bin(int(letter, 16)))[2:])

def evaluate(id, val_list):
    if id == 0:
        res = sum(val_list)
    elif id == 1:
        res = 1
        for val in val_list:
            res *= val
    elif id == 2:
        res = min(val_list)
    elif id == 3:
        res = max(val_list)
    elif id == 5:
        res = int(val_list[0] > val_list[1])
    elif id == 6:
        res = int(val_list[0] < val_list[1])
    elif id == 7:
        res = int(val_list[0] == val_list[1])
    return res

packet_list = []
def calc_version(binary):
    value = 0
    sum = 0
    i = 0
    version = int(binary[i:i+3], 2)
    i += 3
    id = int(binary[i:i+3], 2)
    i += 3
    if id != 4:
        val_list = []
        length_id = int(binary[i:i+1], 2)
        i += 1
        if length_id == 0:
            nb_bits = int(binary[i:i+15], 2)
            i += 15
            j = 0
            while j < nb_bits:
                res = calc_version(binary[i:])
                j += res[0]
                sum += res[1]
                i += res[0]
                val_list.append(res[2])
        else:
            nb_package = int(binary[i:i+11], 2)
            i += 11
            for _ in range(nb_package):
                res = calc_version(binary[i:])
                i += res[0]
                sum += res[1]
                val_list.append(res[2])
        value = evaluate(id, val_list)
    else:
        total = ""
        while True:
            bin_str = binary[i:i+5]
            i += 5
            total += bin_str[1:]
            if bin_str[0] == "0":
                break
        value = int(total, 2)

    return i, version + sum, value

print(calc_version(binary)[2])