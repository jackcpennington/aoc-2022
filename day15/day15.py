from dataclasses import dataclass

@dataclass
class Beacon:
    x: int
    y: int

@dataclass
class Sensor:
    x: int
    y: int
    closest: Beacon


with open("day15/input.txt", 'r') as f:
    nums = [line.strip().split('=') for line in f.readlines()]

sensors = []
for line in nums:
    beacon = Beacon(int(line[-2].split(',')[0]), int(line[-1]))
    sensor = Sensor(int(line[1].split(',')[0]), int(line[2].split(':')[0]), beacon)
    sensors.append(sensor)
    #print(sensor)


def distance(a,b):
    return abs(a.x - b.x) + abs(a.y - b.y)

level = 2000000
not_level_beacons = set()
for sensor in sensors:
    print(sensor)
    maxd = distance(sensor, sensor.closest)
    if sensor.y < level and sensor.y + maxd >= level:
        delta = maxd - abs(level - sensor.y)
        for i in range(sensor.x-delta, sensor.x + delta +1):
            not_level_beacons.add(i)
    elif sensor.y > level and sensor.y - maxd <= level:
        delta = maxd - abs(level - sensor.y)
        for i in range(sensor.x-delta, sensor.x + delta +1):
            not_level_beacons.add(i)
    #print(not_level_beacons)
#print(set([s.closest.x]

beacons_removed = not_level_beacons.difference(set([s.closest.x for s in sensors if s.closest.y == level]))

print(len(beacons_removed))
