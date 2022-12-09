with open('input/day9.sql') as f:
    text = f.read()

steps = [(j[0], int(j[1])) for i in text.splitlines() if (j := i.split(' '))]


def check(head, tail):
    return abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1


def compute():
    for dir, ammount in steps:
        for i in range(ammount):
            head = knots[0]
            match dir:
                case 'U':
                    knots[0] = (head[0], head[1]-1)
                case 'D':
                    knots[0] = (head[0], head[1]+1)
                case 'L':
                    knots[0] = (head[0]-1, head[1])
                case 'R':
                    knots[0] = (head[0]+1, head[1])
            for j, k in zip(range(0, nknots-1), range(1, nknots)):
                head = knots[j]
                tail = knots[k]
                if check(head, tail):
                    knots[k] = (tail[0]+(1 if head[0] > tail[0] else -1 if head[0] < tail[0] else 0),
                                tail[1]+(1 if head[1] > tail[1] else -1 if head[1] < tail[1] else 0))
            visited.add(knots[-1])


nknots = 2
knots = [(0, 0) for _ in range(nknots)]
visited = set()
compute()
print(f"1) Visited cells:{len(visited)}")
nknots = 10
knots = [(0, 0) for _ in range(nknots)]
visited = set()
compute()
print(f"2) Visited cells:{len(visited)}")
