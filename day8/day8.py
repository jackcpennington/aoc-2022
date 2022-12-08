with open("day8/input.txt", 'r') as f:
    trees = [list(map(int, line.strip())) for line in f.readlines()]

vis = 0
scenics = []
for x, row in enumerate(trees):
    for y, tree in enumerate(row):
        north, east, south, west = [-1], [-1], [-1], [-1]
        ns, es, ss, ws = 0,0,0,0 
        if x != 0:
            north = [r[y] for r in trees[:x]][::-1]
        if x != len(trees)-1:
            south = [r[y] for r in trees[x+1:]]
        if y != 0:
            west = [x for x in row[:y]][::-1]
        if y != len(row)-1:
            east = [x for x in row[y+1:]]

        if tree > max(north) or tree > max(east) or tree > max(south) or tree > max(west):
            vis += 1

        for t in north:
            if t == -1:
                break
            if t >= tree:
                ns += 1
                break
            ns += 1

        for t in east:
            if t == -1:
                break
            if t >= tree:
                es += 1
                break
            es += 1

        for t in south:
            if t == -1:
                break
            if t >= tree:
                ss += 1
                break
            ss += 1

        for t in west:
            if t == -1:
                break
            if t >= tree:
                ws += 1
                break
            ws += 1

        scenics.append(ns*es*ss*ws)

print(vis)
print(max(scenics))
