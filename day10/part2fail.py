import sys

sys.setrecursionlimit(20000)

pipemap = [list(s) for s in open('input').readlines()]
marked = {}

def neighbors(coord):
    x,y = coord
    # don't need to worry about edges because the input isn't mean
    return [(x,y-1),
            (x-1,y), (x+1,y),
            (x,y+1)]

def connect_start(start):
    for n in neighbors(start):
        sym = pipemap[n[1]][n[0]]
        delta = (n[0]-start[0], n[1]-start[1])
        if sym == 'L' and (delta == (0,1) or delta == (-1,0)):
            return n
        if sym == '-' and (delta == (-1,0) or delta == (1,0)):
            return n
        if sym == '|' and (delta == (0,-1) or delta == (0,1)):
            return n
        if sym == '7' and (delta == (1,0) or delta == (0,-1)):
            return n
        if sym == 'F' and (delta == (-1,0) or delta == (0,-1)):
            return n
        if sym == 'J' and (delta == (1,0) or delta == (0,-1)):
            return n

def next_space(prev, cur):
    sym = pipemap[cur[1]][cur[0]]
    delta = (cur[0]-prev[0], cur[1]-prev[1])
    if sym == 'L':
        if delta == (0,1):
            return cur[0]+1,cur[1]
        if delta == (-1,0):
            return cur[0],cur[1]-1
    if sym == 'J':
        if delta == (0,1):
            return cur[0]-1,cur[1]
        if delta == (1,0):
            return cur[0],cur[1]-1
    if sym == '7':
        if delta == (0,-1):
            return cur[0]-1,cur[1]
        if delta == (1,0):
            return cur[0],cur[1]+1
    if sym == 'F':
        if delta == (0,-1):
            return cur[0]+1,cur[1]
        if delta == (-1,0):
            return cur[0],cur[1]+1
    if sym == '-':
        if delta == (1,0):
            return cur[0]+1,cur[1]
        if delta == (-1,0):
            return cur[0]-1,cur[1]
    if sym == '|':
        if delta == (0,1):
            return cur[0],cur[1]+1
        if delta == (0,-1):
            return cur[0],cur[1]-1
    print('OH NO')
    print(sym)
    print(delta)



def follow_pipe(start):
    length = 0
    prev = start
    cur = connect_start(start)
    print(start)
    print(pipemap[start[1]][start[0]])
    while pipemap[cur[1]][cur[0]] != 'S':
        print(cur)
        print(pipemap[cur[1]][cur[0]])
        marked[cur] = 'L'
        next = next_space(prev, cur)
        length += 1
        pipemap[cur[1]][cur[0]] = 'X'
        prev = cur
        cur = next
    return length

def expand(point, marker):
    if (point[0]<0 or point[1]<0 or point[0]>=len(pipemap[0]) or point[1]>=len(pipemap)):
        print('OUT OF RANGE')
        return
    if point in marked:
        print('MARKED')
        print(point)
        print(marked[point])
        return
    
    pipemap[point[1]][point[0]]=marker
    marked[point] = marker
    for n in neighbors(point):
        expand(n, marker)


start = None
for y, line in enumerate(pipemap):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x,y)
            break

length = follow_pipe(start)
expand((0,0), 'O')
#for i, _ in enumerate(pipemap):
#    expand((0,i), 'O')
#    expand((len(pipemap[0])-1,i), 'O')
#for i, _ in enumerate(pipemap[0]):
#    expand((i,0), 'O')
#    expand((i,len(pipemap)-1), 'O')
#print((length+1)/2)
counts = {'L':0,'I':0,'O':0}
for mark in marked.values():
    counts[mark] += 1

print(''.join(''.join(p for p in l) for l in pipemap))
print(counts)
print((len(pipemap[0])-1) * (len(pipemap)-1))