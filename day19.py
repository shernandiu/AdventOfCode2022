import re
import gc
import multiprocessing as mp
from math import prod
test = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''

with open('input/day19.sql') as f:
    text = f.read().strip()

MAX_STEPS = 32


def check(ore, clay, obs, cost):
    return all([a >= b for a, b in zip((ore, clay, obs), cost)])


def worst(ore, obs, clay, geo, ore_rob, obs_rob, clay_rob, geo_rob, index):
    return geo+geo_rob*(MAX_STEPS-index)


def bests(ore, obs, clay, geo, ore_rob, obs_rob, clay_rob, geo_rob, index):
    return geo+sum([geo_rob+i//2 for i in range(MAX_STEPS-index)])


def compute(inpu):
    gc.enable()
    max_ore = max(x[0] for x in inpu[1:])
    id, ore_robot_cost, clay_robot_cost, obs_robot_cost, geo_robot_cost = inpu
    ore, obs, clay, geo = 0, 0, 0, 0
    ore_rob, obs_rob, clay_rob, geo_rob = 1, 0, 0, 0

    states = [[ore, obs, clay, geo, ore_rob, obs_rob, clay_rob, geo_rob]]
    # visited.add()
    for ind in range(MAX_STEPS):
        print(f"*** id: {id} index: {ind}")
        substates = set()
        print("usage:", len(states))
        while len(states) > 0:
            ore, obs, clay, geo, ore_rob, obs_rob, clay_rob, geo_rob = states.pop()
            build = [False for _ in range(4)]
            if (check(ore, clay, obs, ore_robot_cost)):
                build[0] = True
            if (check(ore, clay, obs, obs_robot_cost)):
                build[1] = True
            if (check(ore, clay, obs, clay_robot_cost)):
                build[2] = True
            if (check(ore, clay, obs, geo_robot_cost)):
                build[3] = True
            ore += ore_rob
            obs += obs_rob
            clay += clay_rob
            geo += geo_rob

            substates.add((ore, obs, clay, geo, ore_rob, obs_rob, clay_rob, geo_rob))
            if build[3]:
                st = (ore-geo_robot_cost[0], obs-geo_robot_cost[2], clay-geo_robot_cost[1], geo, ore_rob, obs_rob, clay_rob, geo_rob+1)
                if st not in substates:
                    substates.add(st)
                # del st
            else:
                if build[1] and obs_rob <= geo_robot_cost[2]:
                    st = (ore-obs_robot_cost[0], obs-obs_robot_cost[2], clay-obs_robot_cost[1], geo, ore_rob, obs_rob+1, clay_rob, geo_rob)
                    if st not in substates:
                        substates.add(st)
                    # del st
                if build[2] and obs_rob <= obs_robot_cost[1]:
                    st = (ore-clay_robot_cost[0], obs-clay_robot_cost[2], clay-clay_robot_cost[1], geo, ore_rob, obs_rob, clay_rob+1, geo_rob)
                    if st not in substates:
                        substates.add(st)
                    # del st
                if build[0] and obs_rob <= max_ore:
                    st = (ore-ore_robot_cost[0], obs-ore_robot_cost[2], clay-ore_robot_cost[1], geo, ore_rob+1, obs_rob, clay_rob, geo_rob)
                    if st not in substates:
                        substates.add(st)
                    # del st

            # del states[indexstate]
            del ore, obs, clay, geo, ore_rob, obs_rob, clay_rob, geo_rob
        best = max([worst(*x, ind) for x in substates])
        del states
        states = [x for x in substates if bests(*x, ind) >= best]
        # states = substates
        # print(states[0:10])
        gc.collect()
    print('DONE', id, max([x[3] for x in states]))
    return max([x[3] for x in states])


if __name__ == "__main__":
    id = 1
    inputs = []
    for line in text.splitlines()[:3]:
        line = line.replace(':', '. ')
        ore = "\d+(?= ore)"
        clay = "\d+(?= clay)"
        obsidian = "\d+(?= obsidian)"

        tmp = line.split('. ')[1]
        ore_robot_cost = (int(a[0]) if (a := re.search(ore, tmp)) is not None else 0, int(a[0]) if (a := re.search(clay, tmp))
                          is not None else 0, int(a[0]) if (a := re.search(obsidian, tmp)) is not None else 0)
        tmp = line.split('. ')[2]
        clay_robot_cost = (int(a[0])if (a := re.search(ore, tmp)) is not None else 0, int(a[0])if (a := re.search(clay, tmp))
                           is not None else 0, int(a[0])if (a := re.search(obsidian, tmp)) is not None else 0)
        tmp = line.split('. ')[3]
        obs_robot_cost = (int(a[0])if (a := re.search(ore, tmp)) is not None else 0, int(a[0])if (a := re.search(clay, tmp))
                          is not None else 0, int(a[0])if (a := re.search(obsidian, tmp)) is not None else 0)
        tmp = line.split('. ')[4]
        geo_robot_cost = (int(a[0])if (a := re.search(ore, tmp)) is not None else 0, int(a[0])if (a := re.search(clay, tmp))
                          is not None else 0, int(a[0])if (a := re.search(obsidian, tmp)) is not None else 0)
        inputs.append([id, ore_robot_cost, clay_robot_cost, obs_robot_cost, geo_robot_cost])
        id += 1

    print(inputs)
    # ret = map(compute, inputs)
    # p = mp.Pool(processes=12)
    p = mp.Pool()
    ret = p.map(compute, inputs)
    p.close()
    p.join()
    print(ret)
    # print(sum((i+1)*j for i, j in enumerate(ret)))

    print(prod(ret))
