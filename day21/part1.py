from heapq import *

def neighbors(pt):
    x,y = pt
    return [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]

grid = open('input').readlines()

nodes = []
unvisited = []
node_finder = {}

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '.':
            node = [999999999, (x,y), False]
            nodes.append(node)
            unvisited.append(node)
            node_finder[(x,y)] = node
        elif c == 'S':
            node = [0, (x,y), False]
            nodes.append(node)
            unvisited.append(node)
            node_finder[(x,y)] = node

while len(unvisited) > 0:
    unvisited.sort()
    nd = unvisited.pop(0)
    for nb in neighbors(nd[1]):
        if nb not in node_finder: continue
        nnode = node_finder[nb]
        if nnode[2]: continue
        nnode[0] = min(nd[0]+1, nnode[0])
    nd[2] = True

reachable = 0
for node in nodes:
    if node[0] <= 64 and node[0] % 2 == 0:
        reachable += 1

print(reachable)

