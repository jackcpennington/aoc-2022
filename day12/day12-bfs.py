from collections import deque

with open("day12/input.txt", 'r') as f:
    graph = [list(line.strip()) for line in f.readlines()]

alpha = "abcdefghijklmnopqrstuvwxyz"

def bfs(graph, source, target):

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

    Q = deque()
    explored = {source}
    parents = {source: None}
    Q.append(source)


    while Q:
        v = Q.popleft()

        if v == target:
            path = [v]
            parent = parents[v]
            while parent:
                path.append(parent)
                parent = parents[parent]
            return len(path)-1, path

        for u in neighbours(*v):
            if u not in explored:
                parents[u] = v
                explored.add(u)
                Q.append(u)

    return float('inf'), -1

import cProfile

with cProfile.Profile() as pr:


    source = [(i,j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 'S'][0]
    target = [(i,j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 'E'][0]
   
    graph[source[0]][source[1]] = 'a'
    graph[target[0]][target[1]] = 'z'
    
    #for row in graph:
    #    print("".join(row))
    #print()
    
    
    steps, path = bfs(graph, source, target)
    
    print (steps)
    
    #
    #from copy import deepcopy
    #
    #graph2 = deepcopy(graph)
    #
    #for i in range(len(graph2)):
    #    for j in range(len(graph2[0])):
    #        graph2[i][j] = '.'
    #
    #path = list(reversed(path))
    #
    #for idx, (i,j) in enumerate(path[:-1]):
    #    next_step = path[idx+1]
    #    move = (next_step[0]-i, next_step[1]-j)
    #
    #    match move:
    #        case 0, 1:
    #            graph2[i][j] = '>'
    #        case 0, -1:
    #            graph2[i][j] = '<'
    #        case 1, 0:
    #            graph2[i][j] = 'v'
    #        case _:
    #            graph2[i][j] = '^'
    #
    #for row in graph2:
    #    print("".join(row))
    
    sources = [(i,j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 'a']
    stepss = [bfs(graph, source, target)[0] for source in sources]
    
    print(min(stepss))
    
    pr.print_stats()
