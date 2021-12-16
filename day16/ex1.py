list_input = open('input.txt', 'r').read().split('\n')

def leading_zero(str):
    new = ""
    for i in range(4 - len(str)):
        new += "0"
    return new + str
binary = ""
for letter in list_input[0]:
    binary += leading_zero(str(bin(int(letter, 16)))[2:])

class Packet:
    def __init__(self, version, type, payload=""):
        self.version = version
        self.type = type
        self.payload = payload

packet_list = []
def calc_version(binary):
    sum = 0
    i = 0
    version = int(binary[i:i+3], 2)
    i += 3
    id = int(binary[i:i+3], 2)
    i += 3
    if id != 4:
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
        else:
            nb_package = int(binary[i:i+11], 2)
            i += 11
            for _ in range(nb_package):
                res = calc_version(binary[i:])
                i += res[0]
                sum += res[1]
    else:
        total = ""
        while True:
            bin_str = binary[i:i+5]
            i += 5
            total += bin_str[1:]
            if bin_str[0] == "0":
                break

    return i, version + sum

print(calc_version(binary)[1])