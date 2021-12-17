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
    while (pos_x <= x_range[1] and pos_y >= y_range[0]):
        if check_in_rectangle(pos_x, pos_y, x_range, y_range):
            break
        pos_x, pos_y = pos_x + vector[0], pos_y + vector[1]
        vector = change_velocity(vector)
    else:
        return False
    return True

counter = 0
# inch ça passe le brute force
for x in range(1, x_range[1] + 1):
    for y in range(-1000, 1000):
        if check_probe(x, y, x_range, y_range):
            counter += 1

print(counter)