from collections import defaultdict

with open("day9/input.txt", 'r') as f:
    nums = [line.strip().split(" ") for line in f.readlines()]

h = t = (0,0)
visited = set()

for dirr, dist in nums:
    dist = int(dist)
    for _ in range(dist):
        match dirr:
            case 'R':
                h = (h[0], h[1]+1)
            case 'U':
                h = (h[0]-1, h[1])
            case 'L':
                h = (h[0], h[1]-1)
            case 'D':
                h = (h[0]+1, h[1])

        h_neighbours = [(h[0]+x, h[1]+y) for x in range(-1,2) for y in range(-1,2)]

        if t not in h_neighbours:
            tt = (t[0] + h[0], t[1] + h[1])
            t = (h[0] if tt[0]%2 != 0 else tt[0]//2,
                h[1] if tt[1]%2 != 0 else tt[1]//2)
        visited.add(t)

print(len(visited))


t = [(0,0) for _ in range(10)]
visited = set()

for dirr, dist in nums:
    dist = int(dist)
    for _ in range(dist):
        match dirr:
            case 'R':
                t[0] = (t[0][0], t[0][1]+1)
            case 'U':
                t[0] = (t[0][0]-1, t[0][1])
            case 'L':
                t[0] = (t[0][0], t[0][1]-1)
            case 'D':
                t[0] = (t[0][0]+1, t[0][1])

        for i in range(1,10):
            neighbours = [(t[i-1][0]+x, t[i-1][1]+y) for x in range(-1,2) for y in range(-1,2)]

            if t[i] not in neighbours:
                tt = (t[i][0] + t[i-1][0], t[i][1] + t[i-1][1])
                t[i] = (t[i-1][0] if tt[0]%2 != 0 else tt[0]//2,
                        t[i-1][1] if tt[1]%2 != 0 else tt[1]//2)

        visited.add(t[-1])

print(len(visited))
