from collections import defaultdict

def blockcoords(start, end):
    a = []
    s = list(start)
    while s != list(end):
        a.append(tuple(s))
        for j in range(3):
            if s[j] != end[j]:
                s[j] += 1
    a.append(end)
    return a

blockmap = {}
blocks = []
for blockdef in open('input').readlines():
    startr, endr = blockdef.strip().split('~')
    start = tuple(int(x) for x in startr.split(','))
    end = tuple(int(x) for x in endr.split(','))
    blocks.append([start, end])

blocks.sort(key=lambda b: min(b[0][2], b[1][2]))
for i, b in enumerate(blocks):
    for coord in blockcoords(*b):
        blockmap[coord] = i


# DROP BLOCKS
for i, b in enumerate(blocks):
    print('dropping block ',i)
    dropped = 0
    if b[0][2] != b[1][2]: #column
        while (b[0][0],b[0][1],b[0][2]-1) not in blockmap and b[0][2]-1>0:
            dropped += 1
            for c in blockcoords(*b):
                del blockmap[c]
            b[0] = (b[0][0], b[0][1], b[0][2]-1)
            b[1] = (b[1][0], b[1][1], b[1][2]-1)
            for c in blockcoords(*b):
                blockmap[c] = i
    else:
        while all((c[0],c[1],c[2]-1) not in blockmap and c[2]-1>0 for c in blockcoords(*b)):
            dropped += 1
            for c in blockcoords(*b):
                del blockmap[c]
            b[0] = (b[0][0], b[0][1], b[0][2]-1)
            b[1] = (b[1][0], b[1][1], b[1][2]-1)
            for c in blockcoords(*b):
                blockmap[c] = i
    print(dropped)

#for z in range(10, 0, -1):
#    for x in range(10):
#        c = '.'
#        for y in range(10):
#            if (x,y,z) in blockmap:
#                bc = chr(ord('A') + blockmap[(x,y,z)])
#                c = bc if c == bc or c == '.' else '?'
#        print(c, end='')
#    print(' ', z)

# CHECK RESTING
resting_on = defaultdict(set) 
supporting = defaultdict(set)
for i, b in enumerate(blocks):
    if b[0][2] != b[1][2]:
        below = (b[0][0],b[0][1],b[0][2]-1)
        if below in blockmap:
            resting_on[i].add(blockmap[below])
            supporting[blockmap[below]].add(i)
    else:
        for c in blockcoords(*b):
            below = (c[0],c[1],c[2]-1)
            if below in blockmap:
                resting_on[i].add(blockmap[below])
                supporting[blockmap[below]].add(i)

# FIND TO DISINTEGRATE
t = 0
for i, b in enumerate(blocks):
    count = 0
    fallen = set([i])
    q = [i]
    while len(q) > 0:
        nextb = q.pop(0)
        for j in supporting[nextb]:
            if resting_on[j].issubset(fallen):
                if j not in fallen:
                    fallen.add(j)
                    count += 1
                    q.append(j)
    t += count

print(t)
