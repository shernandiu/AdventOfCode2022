from collections import defaultdict

test = '''..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............'''

with open('input/day23.sql') as f:
    text = f.read()


class Elf:
    def __init__(self, coords: complex) -> None:
        self.coords = coords
        self.preference: list = [-1j, 1j, -1, 1]
        self.next_dest = None

    def __str__(self) -> str:
        return f"{self.coords.real} {self.coords.imag}"


elves = {Elf(complex(x, y)) for y, line in enumerate(text.splitlines()) for x, char in enumerate(line) if char == '#'}


def check_round(elf: complex, elves):
    return any((elf + i+j) in elves for i in (-1, 0, 1) for j in (-1j, 0, 1j) if i != 0 or j != 0)


def check_dir(elf: complex, dir, elves):
    if dir in (-1, 1):
        return all((elf + i+dir) not in elves for i in (-1j, 0, 1j))
    return all((elf + i+dir) not in elves for i in (-1, 0, 1))


# coords = {elf.coords for elf in elves}
# for i in range(len(test.splitlines())):
#     for j in range(len(test.splitlines()[0])):
#         print('#' if complex(j, i) in coords else '.', end='')
#     print()
# print()


# for index in range(10):
#     next_step = defaultdict(lambda: [])
#     coords = {elf.coords for elf in elves}
#     for elf in elves:
#         if check_round(elf.coords, coords):
#             for i in elf.preference:
#                 if check_dir(elf.coords, i, coords):
#                     elf.next_dest = i
#                     next_step[elf.coords+i].append(elf)
#                     break
#             else:
#                 elf.next_dest = None
#         elf.preference.append(elf.preference.pop(0))
#     for elv in next_step.values():
#         if len(elv) == 1:
#             elf = elv[0]
#             elf.coords += elf.next_dest


# coordsX = {elf.coords.real for elf in elves}
# coordsY = {elf.coords.imag for elf in elves}

# print((max(coordsX)+1-min(coordsX))*(max(coordsY)+1-min(coordsY))-len(elves))
oldCoords = set()
coords = {elf.coords for elf in elves}
index = 0
while coords != oldCoords:
    index += 1
    next_step = defaultdict(lambda: [])
    oldCoords = coords
    for elf in elves:
        if check_round(elf.coords, oldCoords):
            for i in elf.preference:
                if check_dir(elf.coords, i, oldCoords):
                    elf.next_dest = i
                    next_step[elf.coords+i].append(elf)
                    break
            else:
                elf.next_dest = None
        elf.preference.append(elf.preference.pop(0))
    for elv in next_step.values():
        if len(elv) == 1:
            elf = elv[0]
            elf.coords += elf.next_dest
    coords = {elf.coords for elf in elves}


print(index)
