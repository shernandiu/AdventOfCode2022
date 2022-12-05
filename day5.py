with open('input/day5', 'r') as f:
    lines = [i.replace('\n', '') for i in f.readlines()]

stacks1: list[list] = []

for i, line in enumerate(lines):
    line = line.strip()
    if line[0].isdigit():
        [stacks1.append([]) for _ in range(int(line.split(' ')[-1]))]
        for line2 in lines[i-1::-1]:
            [stacks1[j].append(k.strip('[]')) for j, k in enumerate(line2.replace('    ', ' ').split(' ')) if k != '']
        break

stacks2 = [x[:] for x in stacks1]

for line in lines[i+2:]:    # PART 1
    how_much, origin, dest = [int(i) for i in [j for j in line.split(' ') if j.isdigit()]]
    [stacks1[dest-1].append(stacks1[origin-1].pop()) for _ in range(how_much)]

    stacks2[dest-1].extend(stacks2[origin-1][len(stacks2[origin-1])-how_much:])
    del stacks2[origin-1][len(stacks2[origin-1])-how_much:]

print('1) Last crates', ''.join([i[-1] for i in stacks1]))
print('2) Last crates', ''.join([i[-1] for i in stacks2]))
