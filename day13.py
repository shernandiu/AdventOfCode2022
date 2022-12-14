from json import loads
from functools import cmp_to_key

test = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

with open('input/day13.sql') as f:
    text = f.read()


def compare(left: list, right: list):
    for i, j in zip(left, right):
        if type(i) == type(j) == int:
            if i != j:
                return i < j
        else:
            if type(i) == int:
                i = [i]
            if type(j) == int:
                j = [j]
            aux = compare(i, j)
            if aux is not None:
                return aux
    if len(left) != len(right):
        return len(left) < len(right)


total = 0
# for index, pair in enumerate(text.split("\n\n")):
#     i, j = pair.splitlines()
#     print(index+1, b := compare(loads(i), loads(j)))
#     total += index+1 if b else 0

# print(total)

lines = [loads(line) for line in text.splitlines() if line != '']

item1 = [[2]]
item2 = [[6]]
lines.append(item1)
lines.append(item2)
lines.sort(key=cmp_to_key(lambda a, b: -1 if compare(a, b) else 1))
print(lines)

print((lines.index(item1)+1)*(lines.index(item2)+1))
