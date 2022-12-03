from string import ascii_letters

scores = dict([(j, i+1)for i, j in enumerate(ascii_letters)])

with open("input/day3.sql", 'r') as f:
    lines = [i.strip() for i in f.readlines()]
    # PART 1
    total = 0
    for line in lines:
        char, = set(line[:len(line)//2]) & set(line[len(line)//2:])
        total += scores[char]
    print(f"1) Total score: {total}")
    # PART 2
    total = 0
    for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
        common, = set(l1) & set(l2) & set(l3)
        total += scores[common]
    print(f"2) Total score: {total}")
