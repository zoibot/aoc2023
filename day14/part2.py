def transpose(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

def printgrid(grid):
    print('\n'.join(''.join(r) for r in grid))

def hashgrid(grid):
    return hash('\n'.join(''.join(r) for r in grid))
    
def rotate_left(grid):
    return [[grid[i][len(grid[0])-j-1] for i in range(len(grid))] for j in range(len(grid[0]))]
def rotate_right(grid):
    return [[grid[len(grid)-i-1][j] for i in range(len(grid))] for j in range(len(grid[0]))]

def move_rocks(rows):
    newrows = []
    for row in rows:
        newrow = []
        for i, c in enumerate(row):
            if c == 'O':
                newrow.append('O')
            elif c == '#':
                newrow += ['.'] * (i - len(newrow))
                newrow.append('#')
        newrow += ['.'] * (len(row) - len(newrow))
        newrows.append(newrow)
    return newrows

def cycle(grid):
    for i in range(4):
        grid = move_rocks(grid)
        grid = rotate_right(grid)
    return grid

def count_rocks(cols):
    total = 0
    for col in cols:
        for i, c in enumerate(col):
            if c == 'O':
                total += len(cols) - i
    return total



grid = [list(r.strip()) for r in open('input').readlines()]

printgrid(grid)

grid = rotate_left(grid)

# ex period is 7

# period is 14
# 1203 1765392523445905906
# 1204 5578142794113700278
# 1205 5813071404277986048
# 1206 4538550838987884766
# 1207 -1362557874858958707
# 1208 -7099492285558888722
# 1209 -6041795084565714978
# 1210 3574454136618857799
# 1211 -5664711891649825798
# 1212 -892710487658179338
# 1213 6620024487586182307
# 1214 -6181989558307100062
# 1215 -8677098436270831426
# 1216 -4186533225099449741

for i in range(1000):
    print(i, hashgrid(grid), count_rocks(grid))
    grid = cycle(grid)
print()
printgrid(rotate_right(grid))
print(count_rocks(grid))

