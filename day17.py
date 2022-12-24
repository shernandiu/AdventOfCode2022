test = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''
with open('input/day17.sql') as f:
    test = f.read()
mov = test.strip()


forms = (
    ([0, 0], [1, 0], [2, 0], [3, 0]),          # ####
    ([1, 2], [0, 1], [1, 1], [2, 1], [1, 0]),
    ([0, 0], [1, 0], [2, 0], [2, 1], [2, 2]),
    ([0, 0], [0, 1], [0, 2], [0, 3]),
    ([0, 0], [0, 1], [1, 0], [1, 1])
)

floor = -1
j = 0
tops = [0 for _ in range(7)]
rocks = set()
foo = [(i, -1) for i in range(7)]
rocks.update(foo)


def printhis(piece=[]):
    for i in range(floor+8, -1, -1):
        for j in range(7):
            print('@' if (j, i) in piece else '#' if (j, i) in rocks else '.', end='')
        print()


class Piece:
    def __init__(self, pos) -> None:
        self.position = [2, floor+4]
        self.forms = pos
        self.size = max([x[0] for x in pos])

    def mov(self, position: str):
        if position == '>':
            if self.position[0]+self.size < 6:
                self.position[0] += 1
                if any([x in rocks for x in self.get()]):
                    self.position[0] -= 1
        else:
            if self.position[0] > 0:
                self.position[0] -= 1
                if any([x in rocks for x in self.get()]):
                    self.position[0] += 1

    def down(self):
        self.position[1] -= 1

    def up(self):
        self.position[1] += 1

    def get(self):
        return ((x[0]+self.position[0], x[1]+self.position[1]) for x in self.forms)

    def getAll(self):
        return [(x[0]+self.position[0], x[1]+self.position[1]) for x in self.forms]


visited = dict()
last = []
for i in range(1_000_000_000_000):
    piece = Piece(forms[i % len(forms)])
    while all(x not in rocks for x in piece.get()):
        piece.mov(mov[j])
        piece.down()
        j = (j+1) % len(mov)

    piece.up()
    rocks.update(piece.get())
    for fo in piece.get():
        tops[fo[0]] = max(tops[fo[0]], fo[1])
    floor = max(tops)
    ceil = []
    # for k in range(floor, floor-5, -1):
    #     last = tuple([(j, k) in rocks for j in range(7)])
    #     if all(last):
    #         break
    #     ceil.append(last)
    # ceil = tuple(ceil)

    # lastL = tuple([(j, floor) in rocks for j in range(7)])
    # for a in lastL:
    #     print('a')
    #     last = []
    # else:
    #     last.append(lastL)
    # ceil = tuple(last.copy())
    foo = (i % len(forms), j)
    if foo in visited.keys():
        print(i)
        if (1e12-i) % (i-visited[foo][0]) == 0:
            print(i)
            top = max(tops)
            T = max(visited[foo][1])
            d = (1e12-i)//(i-(visited[foo][0]))
            print(top+(top-T)*d)
            break
    else:
        visited[foo] = (i, tops.copy())

    print(i, end='    \r')

# print(i)
# og = visited[foo][0]
# diff = i-visited[foo][0]
# current_tops = tops.copy()
# og_tops = visited[foo][1]
# # print(og+(1_000_000_000_000//diff-1)*diff)
# print(f"{og+((1_000_000_000_000-og)//diff-1)*diff:_}")
# print(1_000_000_000_000-og-((1_000_000_000_000-og)//diff)*diff)
# for _ in range(1_000_000_000_000-og-((1_000_000_000_000-og)//diff)*diff):
#     piece = Piece(forms[i % len(forms)])
#     while all(x not in rocks for x in piece.get()):
#         piece.mov(mov[j])
#         # printhis(piece.getAll())
#         # input()
#         piece.down()
#         j = (j+1) % len(mov)

#     piece.up()
#     rocks.update(piece.get())
#     for fo in piece.get():
#         tops[fo[0]] = max(tops[fo[0]], fo[1])
#     floor = max(tops)
#     i += 1

# # print((1_000_000_000_000-og)//diff)
# print(tops)
# print(current_tops)
# print(og_tops)
# print(og)
# print(diff)
# print(f"{((1_000_000_000_000)//diff):_}")
# print(f"{og+((1_000_000_000_000-og)//diff)*diff:_}")
# print(f"{max([c+(b-c)*((1_000_000_000_000-og)//diff)+(a-b) for a, b, c in zip(tops, current_tops, og_tops)])+1:_}")
# print(f"{max([c+(b-c)*((1_000_000_000_000-og)//diff)+(a-b) for a, b, c in zip(tops, current_tops, og_tops)])+1}")
