
def transpose(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

def binary(grid):
    nlines = []
    for line in grid:
        n = 0
        for c in line:
            n <<= 1
            n |= 1 if c == '#' else 0
        nlines.append(n)
    return nlines

def check(line, grid):
    return grid[line-1] == grid[line]

def find_sym(grid):
    horiz = binary(grid)
    n = 0
    for i, line in enumerate(horiz):
        n ^= line
        if i > 0 and i % 2 == 1 and n == 0:
            l = int((i+1) / 2)
            if not check(l, horiz):
                continue
            return 100 * l
    n = 0
    for j, line in enumerate(reversed(horiz)):
        n ^= line
        if j > 0 and j % 2 == 1 and n == 0:
            l = len(horiz) - int((j+1) / 2)
            if not check(l, horiz):
                continue
            return 100 * l

    vert = binary(transpose(grid))
    n = 0
    for i, line in enumerate(vert):
        n ^= line
        if i > 0 and i % 2 == 1 and n == 0:
            l = int((i+1) / 2)
            if not check(l, vert):
                continue
            return l
    n = 0
    for j, line in enumerate(reversed(vert)):
        n ^= line
        if j > 0 and j % 2 == 1 and n == 0:
            l = len(vert) - int((j+1) / 2)
            if not check(l, vert):
                continue
            return l

all = open('input').readlines()

grids = []
curgrid = None
for line in all:
    if line.strip() == '':
        grids.append(curgrid)
        curgrid = None
        continue
    if curgrid == None:
        curgrid = []
    curgrid.append(line.strip())

s = 0
for grid in grids:
    c = find_sym(grid)
    if c is None:
        print('\n'.join(grid))
        exit(1)
    s += c
    print(c)
print(s)