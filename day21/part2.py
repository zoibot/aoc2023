import functools

def neighbors(pt):
    x,y = pt
    return [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]

def dijkstra(grid, start):
    nodes = []
    unvisited = []
    node_finder = {}

    for y, row in enumerate(grid):
        for x, c in enumerate(row.strip()):
            if (x,y) == start:
                node = [0, (x,y), False]
                nodes.append(node)
                unvisited.append(node)
                node_finder[(x,y)] = node
            elif c != '#':
                node = [999999999, (x,y), False]
                nodes.append(node)
                unvisited.append(node)
                node_finder[(x,y)] = node
    
    
    while len(unvisited) > 0:
        unvisited.sort() # ugh
        nd = unvisited.pop(0)
        if nd[0] == 999999999:
            print('unreachable', len(unvisited)+1)
            break
        for nb in neighbors(nd[1]):
            if nb not in node_finder: continue
            nnode = node_finder[nb]
            if nnode[2]: continue
            nnode[0] = min(nd[0]+1, nnode[0])
        nd[2] = True

    return node_finder

cached_big = {}
def reachable_squares(finders, steps):
    global cached_big
    parity = steps[0] % 2
    want_return = False
    if steps[0] > g*2:
        if parity in cached_big:
            return cached_big[steps[0]%2]
    r = set()
    for i in range(len(finders)):
        for d, pt, _ in finders[i].values():
            if d <= steps[i] and d % 2 == steps[i] % 2:
                r.add(pt)
    if want_return and want_return != len(r):
        print('DISCREPANCY')
        print(steps)
        exit(1)
    if steps[0] > g*2:
        if parity not in cached_big:
            cached_big[parity] = len(r)
    return len(r)


# read grid and setup

grid = open('input').readlines()

# NOTES they are square and odd, so every space is reachable except for fringes
# no that's wrong you can only get to half of each grid?
# there are "gutters" between iterations of the grid so travel is easy
# calculate reachable from corners with remainder 
# take into account distance from S to corner
w = len(grid[0].strip())
h = len(grid)
if w != h:
    print('OH NO')
    exit(1)
g = 0
start = ()
for y, row in enumerate(grid):
    for x, c in enumerate(row.strip()):
        if c != '#':
            g += 1
        if c == 'S':
            start = (x,y)
print(g,w,h)

print('prep done')

# find distances to/from start/corners

node_finder = dijkstra(grid, start)

topleft = node_finder[(0,0)][0]
topright = node_finder[(w-1, 0)][0]
bottomleft = node_finder[(0, w-1)][0]
bottomright = node_finder[(w-1, w-1)][0]
print(topleft, topright, bottomleft, bottomright)

# named for where you're starting
tl_finder = dijkstra(grid, (0,0))
tr_finder = dijkstra(grid, (w-1,0))
br_finder = dijkstra(grid, (w-1,w-1))
bl_finder = dijkstra(grid, (0,w-1))
tmid_finder = dijkstra(grid, ((w-1)/2,0))
bmid_finder = dijkstra(grid, ((w-1)/2,w-1))
lmid_finder = dijkstra(grid, (0, (w-1)/2))
rmid_finder = dijkstra(grid, (w-1, (w-1)/2))

print('dijkstra done')


# iterate steps
steps = 26501365
#steps = 100
tl_steps = steps - topleft - 2
tr_steps = steps - topright - 2
br_steps = steps - bottomright - 2
bl_steps = steps - bottomleft - 2
midsteps = steps - 65 - 1 # hardcoding based on input grid

spaces = reachable_squares([node_finder], [steps])
cur_diagonal = 1
total_grids = 1
it = 0
while tl_steps >= 0 or tr_steps >= 0 or br_steps >= 0 or bl_steps >= 0 or midsteps >= 0:
    top_spaces = reachable_squares(
            [bl_finder, br_finder, bmid_finder], [tl_steps+1, tr_steps+1, midsteps])
    right_spaces = reachable_squares(
            [tl_finder, bl_finder, lmid_finder], [tr_steps+1, br_steps+1, midsteps])
    bottom_spaces = reachable_squares(
            [tr_finder, tl_finder, tmid_finder], [br_steps+1, bl_steps+1, midsteps])
    left_spaces = reachable_squares(
            [tr_finder, br_finder, rmid_finder], [tl_steps+1, bl_steps+1, midsteps])

    tl_spaces = reachable_squares([br_finder], [tl_steps])
    tr_spaces = reachable_squares([bl_finder], [tr_steps])
    bl_spaces = reachable_squares([tr_finder], [bl_steps])
    br_spaces = reachable_squares([tl_finder], [br_steps])
    
    spaces += top_spaces + bottom_spaces + right_spaces + left_spaces
    spaces += cur_diagonal * (tl_spaces + tr_spaces + bl_spaces + br_spaces)

    tl_steps -= w
    tr_steps -= w
    bl_steps -= w
    br_steps -= w
    midsteps -= w

    total_grids += 4 + 4 * cur_diagonal
    cur_diagonal += 1
    it += 1
    if it % 1000 == 0:
        print(it)

print(spaces)
print(total_grids)




