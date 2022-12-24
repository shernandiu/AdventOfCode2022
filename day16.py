import re
from collections import deque
from math import prod
from multiprocessing import Pool

best_flow = 0


class Valve:
    def __init__(self, name: str, flow) -> None:
        self.name = name
        self.flow = int(flow)
        self.sucessors = []

    def setSuccessor(self, val: "Valve"):
        self.sucessors.append(val)

    def setSuccessor(self, vals):
        self.sucessors.extend(vals)

    def __str__(self) -> str:
        a = " ".join([x.name for x in self.sucessors])
        return f"{self.name}: flow={self.flow}; lead to {a}"


class State:
    def __init__(self, minutes_left: int, current_valve: Valve, total_flow: int, opened: set[Valve], elephant: Valve, opened_when: list = list()) -> None:
        self.minutes_left = minutes_left
        self.current_valve = current_valve
        self.total_flow = total_flow
        self.opened = opened
        self.elephant = elephant
        self.opened_when = opened_when

    def best(self):
        not_opened = [x.flow for x in valves.values() if x not in self.opened]
        not_opened.sort(reverse=True)
        return self.total_flow+sum([j*(self.minutes_left-1-i) for i, j in enumerate(not_opened[:min((self.minutes_left-1)*2, len(not_opened))])])

    def worst(self):
        not_opened = [x.flow for x in valves.values() if x not in self.opened]
        not_opened.sort()
        return self.total_flow+sum([j*(self.minutes_left-1-i) for i, j in enumerate(not_opened[:min(int((self.minutes_left-1)*1), len(not_opened))])])

    def get(self):
        return (self.minutes_left, self.current_valve, self.total_flow, self.opened, self.elephant, self.opened_when)

    def __eq__(self, __o: "State") -> bool:
        # or (self.elephant == __o.current_valve and self.current_valve == __o.elephant))
        return self.total_flow == __o.total_flow and self.opened == __o.opened and ((self.elephant == __o.elephant and __o.current_valve == self.current_valve) or (self.elephant == __o.current_valve and self.current_valve == __o.elephant))

    def __hash__(self) -> int:
        return self.current_valve.__hash__() * self.total_flow * self.elephant.__hash__()*prod([i.__hash__() for i in self.opened])

    def __str__(self) -> str:
        return f"{self.total_flow} {[a.name for a in self.opened]} {self.opened_when}"


def checkbest(st: State):
    global best_flow
    if st.total_flow > best_flow:
        print(st)
    best_flow = max(st.total_flow, best_flow)


if __name__ == "__main__":
    test = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    Valve BB has flow rate=13; tunnels lead to valves CC, AA
    Valve CC has flow rate=2; tunnels lead to valves DD, BB
    Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
    Valve EE has flow rate=3; tunnels lead to valves FF, DD
    Valve FF has flow rate=0; tunnels lead to valves EE, GG
    Valve GG has flow rate=0; tunnels lead to valves FF, HH
    Valve HH has flow rate=22; tunnel leads to valve GG
    Valve II has flow rate=0; tunnels lead to valves AA, JJ
    Valve JJ has flow rate=21; tunnel leads to valve II'''

    with open("input/day16.sql") as f:
        text = f.read()

    whatuse = text

    valves = {}
    for line in whatuse.splitlines():
        valve = Valve(*re.findall("(?<=Valve )[A-Z]{2}|(?<=rate=)\d+", line))
        valves[valve.name] = valve

    for line in whatuse.splitlines():
        ls = re.findall("[A-Z]{2}", line)
        valves[ls[0]].setSuccessor([valves[x] for x in ls[1:]])

    initial = valves['AA']

    max_valves = sum([1 for x in valves.values() if x.flow > 0])

    states = list()
    states.append(State(26, initial, 0, set(), initial))
    visited = set()
    visitedNoEle = set()

    while len(states) > 0:
        sons: list[State] = list()
        while len(states) > 0:
            st = states.pop()
            # sons.append(st)

            minutes_left, current_valve, total_flow, opened, elephant, opened_when = st.get()

            if minutes_left == 0 or len(opened) == max_valves:
                checkbest(st)
                break

            if current_valve not in opened and current_valve.flow > 0:
                new_opened = opened.copy()
                new_opened.add(current_valve)
                new_opened_when = opened_when.copy()
                new_opened_when.append((current_valve.name, 'H', 27-minutes_left, current_valve.flow, minutes_left))
                stn = State(minutes_left, current_valve, total_flow+(minutes_left-1)*current_valve.flow, new_opened, elephant, new_opened_when)
                sons.append(stn)

            flag = True
            for valve in current_valve.sucessors:
                stn = State(minutes_left, valve, total_flow, opened.copy(), elephant, opened_when)
                if stn not in visited:
                    flag = False
                    sons.append(stn)
                    visited.add(stn)
            if flag:
                checkbest(st)

        if len(sons) == 0:
            break
        best_worst = max([i.worst() for i in sons])
        [states.append(i) for i in sons if i.best() >= best_worst]

        sons = list()
        while len(states) > 0:
            st = states.pop()
            minutes_left, current_valve, total_flow, opened, elephant, opened_when = st.get()
            if len(opened) == max_valves:
                checkbest(st)
                break
            if elephant not in opened and elephant.flow > 0:
                new_opened = opened.copy()
                new_opened.add(elephant)
                new_opened_when = opened_when.copy()
                new_opened_when.append((elephant.name, 'E', 27-minutes_left, elephant.flow, minutes_left))
                stn = State(minutes_left-1, current_valve, total_flow+(minutes_left-1)*elephant.flow, new_opened, elephant, new_opened_when)
                sons.append(stn)

            flag = True
            for valve in elephant.sucessors:
                stn = State(minutes_left-1, current_valve, total_flow, opened.copy(), valve, opened_when)
                if stn not in visited:
                    sons.append(stn)
                    flag = False
                    visited.add(stn)
            if flag:
                checkbest(st)

        if len(sons) == 0:
            break
        best_worst = max([i.worst() for i in sons])
        [states.append(i) for i in sons if i.best() >= best_worst]
        # print(best_flow)

    print(best_flow)
