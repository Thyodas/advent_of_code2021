list_input = open('input.txt', 'r').read().split('\n')

cuboids = []
for line in list_input:
    cuboid = []
    on_off, coord = line.split(' ')
    cuboid.append(on_off == "on")

    coord = coord.split(',')
    coord_list = [0, 0, 0]
    for i in range(3):
        nb = coord[i].split('=')[1].split('..')
        coord_list[i] = [int(nb[0]), int(nb[1]) + 1]
        if coord_list[i][0] < -50 or coord_list[i][1] > 51:
            break
    else:
        cuboid.append(coord_list)
        cuboids.append(cuboid)

on_set = set()
for on, (x_range, y_range, z_range) in cuboids:
    for x in range(*x_range):
        for y in range(*y_range):
            for z in range(*z_range):
                if on:
                    on_set.add((x, y, z))
                else:
                    on_set.discard((x, y, z))

#print(cuboids)
print(len(on_set))