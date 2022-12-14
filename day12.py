from collections import deque
from queue import PriorityQueue

test = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

with open('input/day12.sql') as f:
    text = f.read()

matrix = []
for i, line in enumerate(text.splitlines()):
    matrix.append([])
    for j, char in enumerate(line):
        matrix[-1].append(ord(char)-ord('a')+1 if char not in ('S', 'E') else 0 if char == 'S' else 26)
        if char == 'S':
            initial = (i, j)
        elif char == 'E':
            END = (i, j)

# for line in matrix:
#     print(line)

HEIGHT = len(matrix)
LENGHT = len(matrix[0])


queue = PriorityQueue()
queue.put((0, initial))
visited = {}
visited[initial] = 0

print(initial)


def get_neigh(choords: tuple):
    # return [(nI, nJ) for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)) if 0 <= (nI := choords[0]+i) < HEIGHT and 0 <= (nJ := choords[1]+j) < LENGHT and (nI, nJ) not in visited]
    return [(nI, nJ) for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)) if 0 <= (nI := choords[0]+i) < HEIGHT and 0 <= (nJ := choords[1]+j) < LENGHT]


try:
    found = False
    while not found:
        path_lenght, choords = queue.get()
        # print(choords, path_lenght, matrix[choords[0]][choords[1]])
        actual = matrix[choords[0]][choords[1]]
        if actual == 1:
            path_lenght = 0
        elif choords == END:
            print(path_lenght)
            break
        for neighI, neightJ in get_neigh(choords):
            if matrix[neighI][neightJ]-actual <= 1:
                if (neighI, neightJ) not in visited.keys():
                    visited[(neighI, neightJ)] = path_lenght
                    queue.put((path_lenght+1, (neighI, neightJ)))
                elif visited[(neighI, neightJ)] > path_lenght:
                    visited[(neighI, neightJ)] = path_lenght
                    queue.put((path_lenght+1, (neighI, neightJ)))
except:
    pass
    # for i in range(HEIGHT):
    #     for j in range(LENGHT):
    #         print('#' if (i, j) in visited else text.splitlines()[i][j], end='')
    #     print()
    # print()
