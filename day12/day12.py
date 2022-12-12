import heapq
with open("day12/input.txt", 'r') as f:
    graph = [list(line.strip()) for line in f.readlines()]

alpha = "abcdefghijklmnopqrstuvwxyz"

def dijikstra(graph, source, target):

    def neighbours(i, j):
        ns = set()
        if i != 0:
            ns.add(((i-1, j), graph[i-1][j]))
        if j != 0:
            ns.add(((i, j-1), graph[i][j-1]))
        if i != len(graph) - 1:
            ns.add(((i+1, j), graph[i+1][j]))
        if j != len(graph[0]) - 1:
            ns.add(((i, j+1), graph[i][j+1]))

        nss = [b for b, _ in filter(lambda z: alpha.index(z[1]) <= alpha.index(graph[i][j])+1, ns)]
        return nss
    dist = dict()
    prev = dict()
    Q = []

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            v = (i,j)
            dist[v] = float('inf')
            prev[v] = None

    dist[source] = 0
    heapq.heappush(Q, (dist[source], source))

    while Q:
        _, u= heapq.heappop(Q)

        if u == target:
            s = []
            if prev[u] != None or u == source:
                while u:
                    s.append(u)
                    u = prev[u]
            return dist[target], s

        for v in neighbours(*u):
            i, j = v
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))
    return float('inf'), prev


source = [(i,j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 'S'][0]
target = [(i,j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 'E'][0]

graph[source[0]][source[1]] = 'a'
graph[target[0]][target[1]] = 'z'

for row in graph:
    print("".join(row))

steps, path = dijikstra(graph, source, target)

from copy import deepcopy

graph2 = deepcopy(graph)

for i in range(len(graph2)):
    for j in range(len(graph2[0])):
        graph2[i][j] = '.'

path = list(reversed(path))

for idx, (i,j) in enumerate(path[:-1]):
    next_step = path[idx+1]
    move = (next_step[0]-i, next_step[1]-j)

    match move:
        case 0, 1:
            graph2[i][j] = '>'
        case 0, -1:
            graph2[i][j] = '<'
        case 1, 0:
            graph2[i][j] = 'v'
        case _:
            graph2[i][j] = '^'

for row in graph2:
    print("".join(row))

print(steps)

sources = [(i,j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 'a']
print(len(sources))
stepss = []
for idx, source in enumerate(sources):
    print(idx)
    stepss.append(dijikstra(graph, source, target)[0])

print(min(stepss))
