grid = [list(s.strip()) for s in open('input').readlines()]

def transpose(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

expandedrows = []
for line in grid:
    if all(c != '#' for c in line):
        expandedrows.append(['M'] * len(grid[0]))
    else:
        expandedrows.append(line)


expandedrowst = transpose(expandedrows)
expandedcols = []
for line in expandedrowst:
    if all(c != '#' for c in line):
        expandedcols.append(['M'] * len(expandedrowst[0]))
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
        length = 0
        if starb[0] != star[0]:
            for i in range(star[0], starb[0], int((starb[0]-star[0])/abs(starb[0]-star[0]))):
                if expandedgrid[star[1]][i] == 'M':
                    length += 1000000
                else:
                    length += 1

        if starb[1] != star[1]:
            for i in range(star[1], starb[1], int((starb[1]-star[1])/abs(starb[1]-star[1]))):
                if expandedgrid[i][starb[0]] == 'M':
                    length += 1000000
                else:
                    length += 1
        total_len += length

print(pairs)
print(total_len)

#print('\n'.join(''.join(c) for c in expandedgrid))
