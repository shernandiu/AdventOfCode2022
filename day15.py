import re
import random
import llist
test = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''

with open('input/day15.sql') as f:
    text = f.read()

sensors = list()
beacons = set()

# target_y = 2000000
# forbidden = set()

# for line in test.splitlines():
for line in text.splitlines():
    sensorX, sensorY, beaconX, beaconY = [int(x) for x in re.findall('-*[0-9]+', line)]
    distance = abs(beaconX-sensorX)+abs(beaconY-sensorY)
    sensors.append((sensorX, sensorY, distance))
    beacons.add((beaconX, beaconY))


# for sensor_x, sensor_y, distance in sensors:
#     max_val = distance - abs(target_y-sensor_y) + sensor_x
#     min_val = -distance + abs(target_y-sensor_y) + sensor_x
#     for x in range(min_val, max_val+1):
#         if (x, target_y) not in beacons:
#             forbidden.add(x)

# print(len(forbidden))

# PART 2

min_xy = 0
# max_xy = 20
max_xy = 4_000_000
# validX = set([i for i in range(min_xy, max_xy+1)])
# validY = set([i for i in range(min_xy, max_xy+1)])


# for sensor_x, sensor_y, distance in sensors:
#     for y in range(min_xy, max_xy+1):
#         # for x in range(abs(y-sensor_y)- distance + sensor_x,distance - abs(y-sensor_y) + sensor_x + 1 ):
#         #     validX.discard(x)
#         validX.difference_update(range(max(abs(y-sensor_y) - distance + sensor_x, min_xy), min(distance - abs(y-sensor_y) + sensor_x + 1, max_xy+1)))
#     for x in range(min_xy, max_xy+1):
#         validY.difference_update(range(max(abs(x-sensor_x) - distance + sensor_y, min_xy), min(distance - abs(x-sensor_x) + sensor_y + 1, max_xy+1)))

# print(len(validX), len(validY))
# [print(b) for b in sensors]
minval, maxval = 0, 0
valid = [llist.dllist([[0, max_xy]]) for _ in range(max_xy+1)]
# random.shuffle(sensors)
for index, (sensor_x, sensor_y, distance) in enumerate(sensors):
    print(index/len(sensors)*100, end='\r')
    for y in range(max(min_xy, sensor_y-distance), min(max_xy, sensor_y+distance)+1):
        minval = abs(y-sensor_y) - distance + sensor_x
        maxval = distance-abs(y-sensor_y) + sensor_x

        # print(y, minval, maxval)
        # print(y, valid[y])

        if len(valid[y]) == 0:
            continue

        if minval > valid[y].last.value[1] or maxval < valid[y].first.value[0]:  # EL VALOR MINIMO EXCEDE EL MAXIMO DE LA LISTA
            continue
        if minval < valid[y].first.value[0]:   # EL VALOR MINIMO NO ALCANZA EL PRIMERO DE LA LISTA
            i = valid[y].first
        else:
            for i in valid[y].iternodes():
                if i.value[0] <= minval <= i.value[1]:
                    break
            else:
                for i in valid[y].iternodes():
                    if minval <= i.value[0]:
                        break
                else:
                    i = valid[y].last

        if i.value[1] < minval:
            continue

        if i.value[0] > maxval:
            continue

        if i.value[1] >= maxval:
            if maxval < i.value[1]:
                # if i.next is not None:
                #     i.next.value[0] = i.value[1]+1
                valid[y].insertafter([maxval+1, i.value[1]],  i)
            i.value[1] = minval-1
        else:
            j = i.next
            while j is not None and j.value[1] <= maxval:  # BORRAR TODOS LOS SEGMENTOS ENTREMEDIOS
                tmp = j.next
                if tmp is not None:
                    j = j.next
                    valid[y].remove(j.prev)
                else:
                    break
            i.value[1] = minval-1
            if j is not None:
                if j.value[0] <= maxval:
                    j.value[0] = maxval+1
                    if j.value[0] > j.value[1]:
                        valid[y].remove(j)

        if i.value[0] > i.value[1]:
            valid[y].remove(i)

        # print(y, valid[y])
        # print()


for i, j in enumerate(valid):
    if len(j) != 0:
        print(i, j)
