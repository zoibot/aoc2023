pipemap = open('input').readlines()

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
        next = next_space(prev, cur)
        length += 1
        prev = cur
        cur = next
    return length

start = None
for y, line in enumerate(pipemap):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x,y)
            break

length = follow_pipe(start)
print((length+1)/2)