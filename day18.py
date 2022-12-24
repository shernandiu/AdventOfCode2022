test = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''

with open('input/day18.sql') as f:
    text = f.read()

cubes = set()

[cubes.add(tuple(int(x) for x in line.split(','))) for line in text.splitlines()]
x_max = max([x[0] for x in cubes])
y_max = max([x[1] for x in cubes])
z_max = max([x[2] for x in cubes])
x_min = min([x[0] for x in cubes])
y_min = min([x[1] for x in cubes])
z_min = min([x[2] for x in cubes])


def find_neigh(x, y, z, visited):
    visited.add((x, y, z))
    if x > x_max or y > y_max or z > z_max or x < x_min or y < y_min or z < z_min:
        return True
    if (x, y, z) in cubes:
        return False

    for i, j, k in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        if (x+i, y+j, z+k) not in visited:
            if find_neigh(x+i, y+j, z+k, visited):
                return True
    return False


calculated = {}
area = 0
for cube in cubes:
    x, y, z = cube
    sides = 6
    for i, j, k in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        if (x+i, y+j, z+k) in cubes:
            sides -= 1
        elif (x+i, y+j, z+k) in calculated:
            sides -= calculated[(x+i, y+j, z+k)]
        else:
            if not find_neigh(x+i, y+j, z+k, set()):
                calculated[(x+i, y+j, z+k)] = 1
                sides -= 1
            else:
                calculated[(x+i, y+j, z+k)] = 0

    area += sides

print(area)
