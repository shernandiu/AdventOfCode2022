with open('input/day10.sql') as f:
    text = f.read()

instructions = [(y[0], int(y[1])) if (y := x.split(' '))[0] == 'addx' else (y[0], None) for x in text.splitlines()]

WIDTH = 40

cicle = 0
register = 1
signals = []
screen = [[]]


def compute():
    global cicle
    screen[-1].append('#' if (register-1 <= (cicle) % 40 <= register+1) else '.')
    if len(screen[-1]) == WIDTH:
        screen.append([])
    cicle += 1
    if (cicle-20) % 40 == 0:
        signals.append(cicle*register)


for i, j in instructions:
    compute()
    if i == 'noop':
        continue
    compute()
    register += j

print(sum(signals[:6]))

for i in screen:
    print(''.join(i))
