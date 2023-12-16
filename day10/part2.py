import sys

sys.setrecursionlimit(20000)

pipemap = [list(s) for s in open('input').readlines()]
outmap = [['.'] * len(pipemap[0]) for _ in range(len(pipemap))]
path = []
marked = {}

def neighbors(coord):
    x,y = coord
    # don't need to worry about edges because the input isn't mean
    return [(x,y-1), # REMOVE FOR EXMPE
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
    path.append(start)
    cur = connect_start(start)
    while pipemap[cur[1]][cur[0]] != 'S':
        print(cur)
        marked[cur] = 'L'
        path.append(cur)
        next = next_space(prev, cur)
        length += 1
        outmap[cur[1]][cur[0]] = pipemap[cur[1]][cur[0]]
        prev = cur
        cur = next
    return length

def inside(pt):
    if pt in marked:
        return False
    line_start = None
    winding = 0
    for i in range(pt[0]+1,len(pipemap[0])):
        if (i,pt[1]) not in marked:
            continue
        sym = pipemap[pt[1]][i]
        if sym == '|' and line_start is None:
            winding += 1
        elif (sym == 'F' or sym == 'L') and line_start is None:
            line_start = sym
        elif sym == '-' and line_start is not None:
            pass
        elif (sym == 'J' or sym == '7') and line_start is not None:
            if sym == 'J' and line_start == 'F':
                winding += 1
            elif sym == '7' and line_start == 'L':
                winding += 1
            line_start = None
        else:
            print('BAD STATE!!!')
            print(pt[0])
            print((i, pt[1]))
            print(marked[(i, pt[1])])
            print(outmap[pt[1]][i])
            print(sym)
            print(line_start)
            print('\n'.join(''.join(p for p in l) for l in outmap))

            exit(1)
    return winding % 2 == 1




start = None
for y, line in enumerate(pipemap):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x,y)
            break

length = follow_pipe(start)

count = 0
# REPLACE START
pipemap[start[1]][start[0]] = '|'
outmap[start[1]][start[0]] = '|'
marked[start] = 'L'
for y, line in enumerate(pipemap):
    for x, c in enumerate(line):
        if inside((x,y)):
            outmap[y][x] = 'Z'
            count +=1


print('\n'.join(''.join(p for p in l) for l in outmap))
print(count)