from multiprocessing import Pool

test = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''

with open('input/day21.sql') as f:
    text = f.read()

N = len(text.splitlines())

i = 1


def progress():
    global i
    print(i*100/N, end='\r')
    i += 1


class Monkey:
    def __init__(self, op, value=None) -> None:
        self.op = op
        self.value = value

    def setsons(self, left, right):
        self.left = left
        self.right = right

    def calculate(self):
        if self.value is not None:
            progress()
            return self.value

        left = self.left.calculate()
        right = self.right.calculate()
        progress()

        if type(left) == str or type(right) == str:
            return f"({left}{self.op}{right})"

        match self.op:
            case '+':
                return left+right
            case '*':
                return left*right
            case '-':
                return left-right
            case '/':
                return left//right
            case 'r':
                return '='


monkeys = {line.split(': ')[0]: line.split(': ')[1] for line in text.splitlines()}


# monkeysptrs = {key: (Monkey(None, int(value)) if len(value.split(' ')) == 1 else Monkey(value.split(' ')[1])) for key, value in monkeys.items()}
monkeysptrs = {}
for key, value in monkeys.items():
    if len(value.split(' ')) == 1:
        monkeysptrs[key] = Monkey(None, int(value))
    else:
        monkeysptrs[key] = Monkey(value.split(' ')[1])


monkeysptrs['root'] = Monkey('=')
monkeysptrs['humn'] = Monkey(None, 'x')
for key, value in monkeys.items():
    vsplit = value.split(' ')
    if len(vsplit) > 1:
        monkeysptrs[key].setsons(monkeysptrs[vsplit[0]], monkeysptrs[vsplit[2]])


print(monkeysptrs["root"].calculate())
# print(monkeysptrs["root"].calculate())
# def calculate(i):
#     j, k = i
#     monkeysptrs["humn"].value = -10_000_000+j
#     while monkeysptrs["root"].calculate() != 8226036122233:
#         monkeysptrs["humn"].value += k
#         print(monkeysptrs["humn"].value, end="\r")
#     print("***", monkeysptrs["humn"].value)


# if __name__ == "__main__":
#     p = Pool(12)
#     p.map(calculate, [(i, 12) for i in range(12)])
