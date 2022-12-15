import cProfile

with open("day15/test.txt", 'r') as f:
    nums = [line.strip().split('=') for line in f.readlines()]

sensors = []
for line in nums:
    sensor = (int(line[1].split(',')[0]),
              int(line[2].split(':')[0]),
              int(line[-2].split(',')[0]),
              int(line[-1]))
    sensors.append(sensor)

def distance(a,b,c,d):
    return abs(a - c) + abs(b - d)

with cProfile.Profile() as pr:
    jeff = 20
    jd = set(range(jeff+1))
    for level in range(50):
        print(level)
        not_level_beacons = []
        for sensor in sensors:
            maxd = distance(*sensor)
            delta = maxd - abs(level - sensor[1])
            if sensor[1] <= level and sensor[1] + maxd >= level \
            or sensor[1] >= level and sensor[1] - maxd <= level:
                mini, maxi = max(0, sensor[0] - delta), min(sensor[0] + delta +1, jeff +1)
                not_level_beacons += range(mini,maxi)
        if len(set(not_level_beacons)) < jeff+1:
            cliff = jd.difference(not_level_beacons)
            beta = cliff.pop()
            print(level, beta)
            print(level + (beta*4000000))
            break

pr.print_stats()
