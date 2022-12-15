from dataclasses import dataclass
import cProfile

@dataclass
class Beacon:
    x: int
    y: int

@dataclass
class Sensor:
    x: int
    y: int
    closest: Beacon


with open("day15/test.txt", 'r') as f:
    nums = [line.strip().split('=') for line in f.readlines()]

sensors = []
for line in nums:
    beacon = Beacon(int(line[-2].split(',')[0]), int(line[-1]))
    sensor = Sensor(int(line[1].split(',')[0]), int(line[2].split(':')[0]), beacon)
    sensors.append(sensor)
    #print(sensor)


def distance(a,b):
    return abs(a.x - b.x) + abs(a.y - b.y)

with cProfile.Profile() as pr:
    jeff = 20
    #boulder = sum([i for i in range(jeff+1)])
    jd = set(range(jeff+1))
    for level in range(jeff+1):
        print(level)
        not_level_beacons = []
        for sensor in sensors:
            maxd = distance(sensor, sensor.closest)
            delta = maxd - abs(level - sensor.y)
            if sensor.y <= level and sensor.y + maxd >= level \
            or sensor.y >= level and sensor.y - maxd <= level:
                mini, maxi = max(0, sensor.x - delta), min(sensor.x + delta +1, jeff +1)
                not_level_beacons += range(mini, maxi + 1)
        print(set(not_level_beacons))
        if len(set(not_level_beacons)) <= jeff +1:
            cliff = jd.difference(not_level_beacons)
            beta = cliff.pop()
            print(level, beta)
            print(level + (beta*4000000))
            break

#pr.print_stats()
