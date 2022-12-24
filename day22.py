import re
test = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''

test_mode = False

CHUNK_SIZE = 4 if test_mode else 50
#
if test_mode:
    cube = {(2, 0, 2): (1, 1, 1),  # A
            (2, 1, 0): (3, 2, 1),  # B
            (2, 0, 0): (3, 2, 2),  # C
            (1, 1, 1): (2, 2, 0),  # D
            (2, 0, 3): (0, 1, 1),  # E
            (0, 1, 2): (3, 2, 3),  # F
            (0, 1, 1): (2, 2, 3),  # G
            }
else:
    cube = {(1, 0, 2): (0, 2, 0),  # A
            (1, 1, 2): (0, 2, 1),  # B
            (1, 0, 3): (0, 3, 0),  # C
            (0, 3, 0): (1, 2, 3),  # D
            (2, 0, 0): (1, 2, 2),  # E
            (2, 0, 3): (0, 3, 3),  # F
            (2, 0, 1): (1, 1, 2),  # G
            }

tmp = list(cube.items())
for (i1, j1, d1), (i2, j2, d2) in tmp:
    cube[(i2, j2, (d2+2) % 4)] = (i1, j1, (d1+2) % 4)

with open('input/day22.sql') as f:
    text = f.read()

table = {}
for i, line in enumerate((test if test_mode else text).splitlines()[:-1]):
    for j, char in enumerate(line):
        if char != ' ':
            table[(j, i)] = 0 if char == '.' else 1

# print(table)
instructions = [int(i) if i.isdigit() else i for i in re.findall("\d+|[R,L]", (test if test_mode else text).splitlines()[-1])]

# print(instructions)
position = (min([i for i, j in table if j == 0]), 0)
# Vertical_tps = {}
# Horizontal_tps = {}
# for i in range(max([len(x) for x in (test if test_mode else text).splitlines()[:-2]])):
#     minRow = min([k for j, k in table if j == i])
#     maxRow = max([k for j, k in table if j == i])
#     Vertical_tps[(i, minRow-1)] = (i, maxRow)
#     Vertical_tps[(i, maxRow+1)] = (i, minRow)
# for i in range(len((test if test_mode else text).splitlines()[:-2])):
#     minCol = min([j for j, k in table if k == i])
#     maxCol = max([j for j, k in table if k == i])
#     Horizontal_tps[(minCol-1, i)] = (maxCol, i)
#     Horizontal_tps[(maxCol+1, i)] = (minCol, i)

# tps = Vertical_tps.keys() | Horizontal_tps.keys()

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
direction = 0

# print(tps)

for char in instructions:
    print(char)
    if char == 'R':
        direction += 1
        direction %= 4
        continue
    if char == 'L':
        direction -= 1
        direction %= 4
        continue

    # i==int
    i, j = position
    for _ in range(char):
        # PART 1
        # if (i+dirI, j+dirJ) in tps:
        #     newI, newJ = (Horizontal_tps if direction % 2 == 0 else Vertical_tps)[(i+dirI, j+dirJ)]

        dirI, dirJ = directions[direction]
        newI, newJ = i+dirI, j+dirJ
        newDir = direction
        if (newI, newJ) not in table:
            newIChunk, newJChunk, newDir = cube[(i//CHUNK_SIZE, j//CHUNK_SIZE, direction)]
            newI, newJ = (newI % CHUNK_SIZE)-(CHUNK_SIZE-1)/2, (newJ % CHUNK_SIZE)-(CHUNK_SIZE-1)/2
            for _ in range((newDir-direction) % 4):
                newI, newJ = -newJ, newI
            newI, newJ = newIChunk*CHUNK_SIZE+(newI+(CHUNK_SIZE-1)/2), newJChunk*CHUNK_SIZE+(newJ+(CHUNK_SIZE-1)/2)
            newI, newJ = int(newI), int(newJ)
        # else:
            # newI, newJ = i+dirI, j+dirJ
        if table[(newI, newJ)] == 0:
            i, j = newI, newJ
            direction = newDir
        else:
            break

    position = (i, j)
    print(position)
print((position[1]+1), (position[0]+1), direction)
print((position[1]+1)*1000+(position[0]+1)*4+direction)
