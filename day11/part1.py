grid = [list(s.strip()) for s in open('input').readlines()]

def transpose(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

expandedrows = []
for line in grid:
    if all(c != '#' for c in line):
        expandedrows.append(['.'] * len(grid[0]))
        expandedrows.append(['.'] * len(grid[0]))
    else:
        expandedrows.append(line)


expandedrowst = transpose(expandedrows)
expandedcols = []
for line in expandedrowst:
    if all(c != '#' for c in line):
        expandedcols.append(['.'] * len(expandedrowst[0]))
        expandedcols.append(['.'] * len(expandedrowst[0]))
    else:
        expandedcols.append(line)

expandedgrid = transpose(expandedcols)

stars = set()
for x in range(len(expandedgrid[0])):
    for y in range(len(expandedgrid)):
        if expandedgrid[y][x] == '#':
            stars.add((x,y))

pairs = 0
total_len = 0
while len(stars) > 0:
    star = stars.pop()
    for starb in stars:
        pairs += 1
        total_len += abs(starb[0]-star[0]) + abs(starb[1]-star[1])

print(pairs)
print(total_len)

#print('\n'.join(''.join(c) for c in expandedgrid))
