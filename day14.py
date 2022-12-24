test = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


with open('input/day14.sql') as f:
    text = f.read()


def plotLine(x0, y0, x1, y1):
    out = []
    if x1 < x0:
        x0, x1 = x1, x0
    if y1 < y0:
        y0, y1 = y1, y0
    dx = x1-x0
    dy = y1-y0
    x = x0
    y = y0
    p = 2*dy-dx
    while x <= x1 and y <= y1:
        if p >= 0:
            out.append((x, y))
            y = y+1
            p = p+2*dy-2*dx
        else:
            out.append((x, y))
            p = p+2*dy
            x = x+1
    return out


rock = set()
for line in text.splitlines():
    choords = line.split(' -> ')
    for ori, dst in zip(choords[:-1], choords[1:]):
        x0, y0 = [int(i) for i in ori.split(',')]
        x1, y1 = [int(i) for i in dst.split(',')]
        rock.update(plotLine(x0, y0, x1, y1))


minY = max(map(lambda i: i[1], rock))
print(minY)
iteration = 0
while True:
    x, y = 500, 0
    while y < minY+1:
        # print((x, y))
        if (x, y+1) not in rock:
            y += 1
        elif (x-1, y+1) not in rock:
            x -= 1
            y += 1
        elif (x+1, y+1) not in rock:
            x += 1
            y += 1
        else:
            break
    rock.add((x, y))

    iteration += 1
    if x == 500 and y == 0:
        break

print(iteration)
