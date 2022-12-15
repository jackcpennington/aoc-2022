import cProfile

with open("day15/input.txt", 'r') as f:
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
    jeff = 4000000
    jd = set(range(jeff+1))
    for level in range(jeff+1):
        print(level)
        not_level_beacons = []
        for sensor in sensors:
            maxd = distance(*sensor)
            delta = maxd - abs(level - sensor[1])
            if sensor[1] <= level and sensor[1] + maxd >= level \
            or sensor[1] >= level and sensor[1] - maxd <= level:
                mini, maxi = max(0, sensor[0] - delta), min(sensor[0] + delta +1, jeff +1)
                not_level_beacons.append((mini, maxi-1))

        not_level_beacons.sort(key=lambda x: x[0])

        acc = not_level_beacons[0]
        for i in not_level_beacons[1:]:
            if i[0] <= acc[1] + 1:
                acc = (acc[0], max(acc[1], i[1]))
            else:
                print("gap")

        if acc != (0, jeff):
            print("flash")
            beta = acc[1]+1
            print(level, beta)
            print(level + (beta*4000000))
            break

pr.print_stats()
