score_movement = [1, 2, 3]     # X:1, Y:2, Z:3
win_lose = [0, 3, 6]        # Lose, Draw, Win
what_should_I_do = [2, 0, 1]  # 2: Lose, 0: Draw, 1: Win

total_part1 = 0
total_part2 = 0
with open("input/day2.sql", 'r') as f:
    for line in f.readlines():
        it = iter(('A', 'X'))
        oponent, mine = [ord(i) - ord(next(it)) for i in line.strip().split(' ')]  # ROCK: 0 PAPER: 1 SCISSOR: 2

        total_part1 += win_lose[(mine-oponent+1) % 3]+score_movement[mine]
        total_part2 += win_lose[mine]+score_movement[(oponent+what_should_I_do[mine]) % 3]
    print("1) Total points:", total_part1)
    print("2) Total points:", total_part2)
