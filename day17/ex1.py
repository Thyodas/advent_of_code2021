list_input = open('input.txt', 'r').read().split('\n')

input = list_input[0][15:].split(", y=")
x_range = [int(el) for el in input[0].split("..")]
y_range = [int(el) for el in input[1].split("..")]

def check_in_rectangle(x, y, x_range, y_range):
    if x_range[0] <= x <= x_range[1]:
        if y_range[0] <= y <= y_range[1]:
            return True
    return False

def change_velocity(old_vector):
    vec_x, vec_y = old_vector
    vector = [0, 0]
    if vec_x > 0:
        vector[0] = vec_x - 1
    vector[1] = vec_y - 1
    return vector

def check_probe(vec_x, vec_y, x_range, y_range):
    pos_x, pos_y = 0, 0
    vector = [vec_x, vec_y]
    max_y = 0
    while (pos_x <= x_range[1] and pos_y >= y_range[0]):
        if check_in_rectangle(pos_x, pos_y, x_range, y_range):
            break
        pos_x, pos_y = pos_x + vector[0], pos_y + vector[1]
        vector = change_velocity(vector)
        max_y = max(max_y, pos_y)
    else:
        return (False, 0)
    return (True, max_y)

max_y = None
for x in range(1, x_range[1] + 1):
    for y in range(-100, 100):
        valid, valid_y = check_probe(x, y, x_range, y_range)
        if valid:
            if max_y is None:
                max_y = valid_y
            else:
                max_y = max(max_y, valid_y)

print(max_y)