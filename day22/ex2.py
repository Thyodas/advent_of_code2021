list_input = open('input.txt', 'r').read().split('\n')

class Cube:
    def __init__(self, x_range, y_range, z_range, is_on=True):
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range
        self.is_on = is_on

    def __repr__(self):
        return f"| {'On' if self.is_on else 'Off' }, {self.x_range}, {self.y_range}, {self.z_range} |"

    def __getitem__(self, dimension: int) -> list[int]:
        if dimension == 0:
            return self.x_range
        elif dimension == 1:
            return self.y_range
        else:
            return self.z_range

    @staticmethod
    def overlaps(cuboid_a, cuboid_b) -> bool:
        for dimension in range(3):
            if not (cuboid_a[dimension][0] <= cuboid_b[dimension][1] \
            and cuboid_a[dimension][1] >= cuboid_b[dimension][0]):
                return False
        return True

    def get_volume(self):
        volume = (abs(self.x_range[1] - self.x_range[0]) + 1) * (abs(self.y_range[1] - self.y_range[0]) + 1) * (abs(self.z_range[1] - self.z_range[0]) + 1)
        return volume

    def get_overlapping_cube(self, other_cube):
        if not Cube.overlaps(self, other_cube):
            return None

        new_x_range = [max(self.x_range[0], other_cube.x_range[0]), min(self.x_range[1], other_cube.x_range[1])]
        new_y_range = [max(self.y_range[0], other_cube.y_range[0]), min(self.y_range[1], other_cube.y_range[1])]
        new_z_range = [max(self.z_range[0], other_cube.z_range[0]), min(self.z_range[1], other_cube.z_range[1])]

        new_cube = Cube(new_x_range, new_y_range, new_z_range, other_cube.is_on)
        return new_cube

cuboids = []
for line in list_input:
    cuboid = []
    on_off, coord = line.split(' ')
    coord = coord.split(',')
    coord_list = [0, 0, 0]
    for i in range(3):
        nb = coord[i].split('=')[1].split('..')
        coord_list[i] = [int(nb[0]), int(nb[1])]
    cube = Cube(*coord_list, on_off == "on")
    cuboids.append(cube)

def overlaps(cuboid_a, cuboid_b) -> bool:
    for dimension in range(3):
        if not (cuboid_a[dimension][0] <= cuboid_b[dimension][1] \
        and cuboid_a[dimension][1] >= cuboid_b[dimension][0]):
            return False
    return True


processed_cubes = []
for current_cube in cuboids:
    new_cubes = []
    for other_cube in processed_cubes:
        overlapping_cube = current_cube.get_overlapping_cube(other_cube)
        if overlapping_cube is not None:
            overlapping_cube.is_on = not other_cube.is_on
            new_cubes.append(overlapping_cube)

    if current_cube.is_on:
        processed_cubes.append(current_cube)
    processed_cubes.extend(new_cubes)

total_on = 0
for cube in processed_cubes:
    if cube.is_on:
        total_on += cube.get_volume()
    else:
        total_on -= cube.get_volume()

print(total_on)