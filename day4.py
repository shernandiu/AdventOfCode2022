with open("input/day4.sql", 'r') as f:
    lines = [i.strip() for i in f.readlines()]

total1, total2 = 0, 0
for line in lines:
    pairs = [[int(j) for j in i.split('-')]for i in line.split(',')]
    # Put the pair that starts before on the first place,
    # if they start at the same time, longest one first
    if pairs[0][0] > pairs[1][0] or (pairs[0][0] == pairs[1][0] and pairs[1][1] > pairs[0][1]):
        pairs[0], pairs[1] = pairs[1], pairs[0]
    # If the second pair ends before the first one, it's being completely overlapsed
    if pairs[1][1] <= pairs[0][1]:
        total1 += 1
    # If the second pair starts before the first one ends, it's being overlapsed
    if pairs[0][1] >= pairs[1][0]:
        total2 += 1

print(f"1) Total: {total1}")
print(f"2) Total: {total2}")
