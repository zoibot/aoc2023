from collections import defaultdict

def neighbors(p):
    return (p[0]-1,p[1]), (p[0]+1,p[1]), (p[0],p[1]-1), (p[0],p[1]+1)
def passable(delta, c):
    return delta == (1,0) and c == '>' or \
            delta == (-1,0) and c == '<' or \
            delta == (0,1) and c == 'v' or \
            delta == (0,-1) and c == '^'

grid = open('input').readlines()

start = None
for i, c in enumerate(grid[0]):
    if c == '.':
        start = (i, 0)

paths = defaultdict(dict)
paths[start] = {}

end = None
q = [(start, (start[0],start[1]+1), 1)]
ct = 100
while len(q) > 0:
    print(q)
    begin, cur, baselen = q.pop(0)
    prev = begin
    curlen = 0
    slope = False
    while True:
        for n in neighbors(cur):
            if n[1] < 0: continue
            if n == prev: continue
            c = grid[n[1]][n[0]]
            if c != '#':
                prev = cur
                cur = n
                curlen += 1
                break
        if c != '.':
            slope = True
        if c == '.' and slope:
            print('found node')
            paths[begin][cur] = baselen+curlen
            for n in neighbors(cur):
                c = grid[n[1]][n[0]]
                if passable((n[0]-cur[0], n[1]-cur[1]), c):
                    q.append((cur, n, 1))
            break
        if cur[1] == len(grid)-1:
            end = cur
            paths[begin][end] = baselen+curlen
            break

print(paths)

maxlens = {start: 0}
q = [start]
while len(q) > 0:
    nd = q.pop(0)
    if nd == end: continue
    l = maxlens[nd]
    for pathnd, pathlen in paths[nd].items():
        if pathnd not in maxlens or l + pathlen > maxlens[pathnd]:
            maxlens[pathnd] = l + pathlen
            q.append(pathnd)

print(maxlens)
print(maxlens[end])
