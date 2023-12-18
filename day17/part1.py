from heapq import *

grid = [list(int(h) for h in row.strip()) for row in open('input').readlines()]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

q = [(0, 0,0,0,(0,0),0,())]
marks = {(0,0, (0,0)): 0}

best_so_far = 10000

while len(q) > 0:
    _, x, y, heat, lastd, straights, path = heappop(q)
    for d in dirs:
        if d == (-lastd[0], -lastd[1]):
            continue # can't reverse
        xnew, ynew = x+d[0], y+d[1]
        if xnew < 0 or xnew >= len(grid[0]) or ynew < 0 or ynew >= len(grid):
            continue
        newstraights = straights + 1 if d == lastd else 0
        if newstraights >= 3:
            continue
        newheat = heat + grid[ynew][xnew]
        if (xnew,ynew,d,newstraights) in marks:
            existingheat, _ = marks[(xnew,ynew,d,newstraights)]
            if newheat >= existingheat:
                continue
        marks[(xnew,ynew,d,newstraights)] = newheat, path
        if len(grid[0])-1 == xnew and len(grid)-1 == ynew:
            if newheat < best_so_far:
                best_so_far = newheat
                print('found a way', best_so_far)
            # no need to cont
            continue
        if heat > best_so_far:
            continue # give up on this path
        prio = heat + (len(grid[0])-1-x) + (len(grid)-1-y) 
        heappush(q, (prio, xnew, ynew, newheat, d, newstraights, path)) #path+((xnew,ynew,d),)))

a = []
for d in dirs:
    for s in range(3):
        k = (len(grid[0])-1, len(grid)-1, d, s)
        if k in marks: 
            h, path = marks[k]
            print(k, h)
            a.append(h)
            #g = [r[:] for r in grid]
            #for x, y, d in path:
            #    c = '.'
            #    if d == (1,0): c = '>'
            #    if d == (0,-1): c = '^'
            #    if d == (-1,0): c = '<'
            #    if d == (0,1): c = 'V'
            #    g[y][x] = c
            #print('\n'.join(''.join(str(x) for x in r) for r in g))
print('MIN', min(a))
