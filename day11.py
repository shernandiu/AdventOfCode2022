from collections import deque
from os import get_terminal_size
test = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

with open('input/day11.sql') as f:
    text = f.read()


class Monkey:
    def __init__(self, list_monkeys, text: str) -> None:
        text = text.splitlines()
        self.list_monkeys = list_monkeys

        self.items = deque([int(i) for i in text[1][text[1].find(':')+1:].split(', ')])
        self.operation = [int(i) if i.isdigit() else i for i in text[2][text[2].find('=')+2:].split(' ')]
        self.test = (int(text[3].split(' ')[-1]), int(text[4].split(' ')[-1]), int(text[5].split(' ')[-1]))
        self.inspected = 0

    def getmult(self, item):
        return item if self.operation[2] == 'old' else self.operation[2]

    def operate(self, item: dict):
        # op1 = item if self.operation[0] == 'old' else self.operation[0]
        op2 = self.operation[2]
        match self.operation[1]:
            case '+':
                for i in item.keys():
                    item[i] += op2
                    item[i] %= i
                # print(f'\t\tWorry level is added by {op2} to {out}.')
            case '*':
                if op2 == 'old':
                    for i in item.keys():
                        item[i] *= item[i]
                        item[i] %= i
                else:
                    for i in item.keys():
                        item[i] *= op2
                        item[i] %= i
                # if item % op2 == 0:
                #     return item
                # out = op1*op2
                # print(f'\t\tWorry level is multiplied by {op2} to {out}.')

    def exec(self):
        while (len(self.items) > 0):
            item = self.items.popleft()
            # print(f'\tMonkey inspects an item with a worry level of {item}.')
            # worry = self.operate(item)
            # if self.operation[1] == '+':
            #     self.list_monkeys[self.test[1 if worry % self.test[0] == 0 else 2]].give(worry)
            # else:
            #     self.list_monkeys[self.test[1 if worry % self.test[0] == 0 else 2]].give(worry)
            self.operate(item)
            self.list_monkeys[self.test[1 if item[self.test[0]] == 0 else 2]].give(item)
            # worry //= 3
            # print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {worry}.")

            # print(f"\t\tItem with worry level {worry} is thrown to monkey {self.test[0 if worry % self.test[0]==0 else 2]}.")
            self.inspected += 1

    def give(self, item: int):
        self.items.append(item)

    def parseItems(self):
        newQ = deque()
        for item in self.items:
            divisors = {}
            for i in [j.test[0] for j in self.list_monkeys]:
                divisors[i] = item % i
            newQ.append(divisors)
        self.items = newQ


ts = get_terminal_size()
list_monkeys = []
for i in text.split('\n\n'):
    list_monkeys.append(Monkey(list_monkeys, i))
[m.parseItems() for m in list_monkeys]


print(list_monkeys[0].operation)
print(list_monkeys[0].test)

for iteration in range(10_000):
    for i, monkey in enumerate(list_monkeys):
        # print(f'Monkey {i}:')
        monkey.exec()
    size = ((ts.columns-20)*iteration//10_000)
    loading_bar = '#'*(size)+'.'*(ts.columns-20-size)
    print(f"[{loading_bar}] {iteration//100}%", end='\r')
    # for i, monkey in enumerate(list_monkeys):
    # print(f'Monkey {i}: ' + ', '.join([str(j) for j in monkey.items]))
size = ((ts.columns-20))
loading_bar = '#'*(size)
print(f"[{loading_bar}] {100}%")

for i, monkey in enumerate(list_monkeys):
    print(f'Monkey {i} inspected items {monkey.inspected} times.')

times = [monkey.inspected for monkey in list_monkeys]
times.sort(reverse=True)
print(times[0]*times[1])
