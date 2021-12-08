list_input = open('input.txt', 'r').read().split('\n')

digit_value = [el.split(' ')[:10] for el in list_input]
output_value = [el.split(' ')[11:] for el in list_input]
lines = [[digit_value[i], output_value[i]] for i in range(len(digit_value))]

def get_missing_letter(digit):
    letter = ""
    total = "abcdefg"
    for le in total:
        if le not in digit:
            letter += le
    return letter

def determine_unique(digits):
    association = {2:1, 4:4, 3:7, 7:8}
    unique_dict = {1:"", 4:"", 7:"", 8:""}
    for digit in digits:
        size = len(digit)
        if size in association:
            unique_dict[association[size]] = digit
    return unique_dict

def determine_digits(digits):
    values = determine_unique(digits)
    for digit in digits:
        size = len(digit)
        missing = get_missing_letter(digit)
        if size == 6:
            if missing[0] in values[7]:
                values[6] = digit
            elif missing[0] in values[4]:
                values[0] = digit
            else:
                values[9] = digit
    for digit in digits:
        size = len(digit)
        missing = get_missing_letter(digit)
        if size == 5:
            if missing[0] not in values[7] and missing[1] not in values[7]:
                values[3] = digit
            elif get_missing_letter(values[6])[0] in digit:
                values[2] = digit
            else:
                values[5] = digit
    return values

def get_value_by_digit(value, digit):
    for key, val in value.items():
        if len(val) != len(digit):
            continue
        for le in digit:
            if le not in val:
                break
        else:
            return key

def get_line_value(line):
    digit_value = line[0]
    output_value = line[1]

    digit_dict = determine_digits(digit_value)
    result = ""
    for el in output_value:
        result += str(get_value_by_digit(digit_dict, el))
    return int(result)

sum = 0
for line in lines:
    sum += get_line_value(line)

print(sum)