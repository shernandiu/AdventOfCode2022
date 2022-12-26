from queue import PriorityQueue
import heapq

from collections import deque
test = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''

with open('input/day24.sql') as f:
    text = f.read()

initial = 1
lines = text.splitlines()
end = len(lines[0])-2 + (len(lines)-1)*1j
WIDTH = len(lines[0])-2
HEIGHT = len(lines)-2
blizzards = set()
walls = set()
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '.':
            continue
        if char == '#':
            walls.add(j+i*1j)
            continue
        match char:
            case '^':
                blizzards.add((j+i*1j, -1j))
            case '>':
                blizzards.add((j+i*1j, 1))
            case 'v':
                blizzards.add((j+i*1j, 1j))
            case '<':
                blizzards.add((j+i*1j, -1))
blizzards = frozenset(blizzards)


visited = {}


def calculate(pos, cost, reached_goal, reached_start) -> int:
    if not reached_goal:
        return (abs((end-pos).real)+abs((end-pos).imag)+(WIDTH+HEIGHT)*2)*2+cost*1
    if not reached_start:
        return (abs((initial-pos).real)+abs((initial-pos).imag)+WIDTH+HEIGHT)*2+cost*1

    return (abs((end-pos).real)+abs((end-pos).imag))*2+cost*1


list_blizzars = []
list_blizzars.append(blizzards)

limit = 999999999999999999999999999999999999
pq = []
heapq.heappush(pq, (0, 0, initial.real, initial.imag, blizzards, False, False))
# pq = deque()
# pq.append((0, initial.real, initial.imag, blizzards, False, False))
visited[(initial, blizzards, False, False)] = 0
while len(pq) > 0:
    _, cost, positionX, positionY, blizzards, reached_goal, reached_start = heapq.heappop(pq)
    # cost, positionX, positionY, blizzards, reached_goal, reached_start = pq.popleft()
    print(f"{cost:5}", end='\r')
    position = complex(positionX, positionY)

    # print(cost)
    # for i in range(HEIGHT+2):
    #     for j in range(WIDTH+2):
    #         co = complex(j, i)
    #         print('v' if co in [b[0] for b in blizzards] else '#' if co in walls else 'E' if co == position else 'e' if co == end else '.', end='')
    #     print()
    # input()

    if cost+1 < len(list_blizzars):
        blizzards = list_blizzars[cost+1]
    else:
        newBliz = set()
        for pos, dir in blizzards:
            pos += dir
            if pos in walls:
                match dir:
                    case 1:
                        pos -= WIDTH
                    case -1:
                        pos += WIDTH
                    case 1j:
                        pos -= (HEIGHT)*1j
                    case -1j:
                        pos += (HEIGHT)*1j
            newBliz.add((pos, dir))
        blizzards = frozenset(newBliz)
        list_blizzars.append(blizzards)

    blizzardsSet = {b[0] for b in blizzards}
    for i in (0, -1, 1, -1j, 1j):
        if (position+i) not in walls and (position+i) not in blizzardsSet and HEIGHT+1 >= (position+i).imag >= 0:
            if cost+1 < limit and ((position+i, blizzards, reached_goal, reached_start) not in visited or visited[(position+i, blizzards, reached_goal, reached_start)] > cost+1):
                visited[(position+i, blizzards, reached_goal, reached_start)] = cost+1

                if position+i == end and not reached_start and not reached_goal:
                    reached_goal = True
                    print("Reached goal in", cost+1)

                if position+i == initial and reached_goal and not reached_start:
                    reached_start = True
                    print("Reached start in", cost+1)

                if position+i == end and reached_start and reached_goal:
                    limit = cost+1
                    print("Ended in", limit)
                    pq = [x for x in pq if x[1] <= limit-1]
                    heapq.heapify(pq)
                    continue
                    # break

                heapq.heappush(pq, (calculate(position+i, cost+1, reached_goal, reached_start), cost+1, (position+i).real, (position+i).imag, blizzards, reached_goal, reached_start))
                # pq.append((cost+1, (position+i).real, (position+i).imag, blizzards, reached_goal, reached_start))


print(limit)
