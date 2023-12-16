def transpose(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

def count_rocks(cols):
    total = 0
    for col in cols:
        cur_points = len(cols)
        for i, c in enumerate(col):
            if c == 'O':
                total += cur_points
                cur_points -= 1
            elif c == '#':
                cur_points = len(cols) - i - 1
    return total


rows = [r.strip() for r in open('input').readlines()]
cols = transpose(rows)

c = count_rocks(cols)
print(c)