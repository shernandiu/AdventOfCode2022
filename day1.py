with open("input/day1.sql", 'r') as f:
    elfs = [sum([int(j) for j in i.split('\n') if j]) for i in f.read().split('\n\n')]
    elfs.sort(reverse=True)
    print(f"A) max elf:    {elfs[0]}")
    print(f"B) max 3 elfs: {sum(elfs[0:3])}")
