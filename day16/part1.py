grid = [row.strip() for row in open('input').readlines()]

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

def count_from_pos(x, y, d):
    grid_out = [[set() for _ in row] for row in grid]
    grid_out[y][x] = set((d,))

    tiles = [(0,0)]
    while len(tiles) > 0:
        tile = tiles.pop(0)
        obj = grid[tile[1]][tile[0]]
        directions = grid_out[tile[1]][tile[0]]
        for d in directions:
            new_ds = [d]
            if obj == '.':
                pass
            elif obj == '/':
                if d == RIGHT:
                    new_ds = [UP]
                elif d == LEFT:
                    new_ds = [DOWN]
                elif d == UP:
                    new_ds = [RIGHT]
                elif d == DOWN:
                    new_ds = [LEFT]
            elif obj == '\\':
                if d == RIGHT:
                    new_ds = [DOWN]
                elif d == LEFT:
                    new_ds = [UP]
                elif d == UP:
                    new_ds = [LEFT]
                elif d == DOWN:
                    new_ds = [RIGHT]
            elif obj == '-':
                if d == UP or d == DOWN:
                    new_ds = [LEFT, RIGHT]
            elif obj == '|':
                if d == LEFT or d == RIGHT:
                    new_ds = [UP, DOWN]
            else:
                print('uh oh')
                exit(1)
            print(new_ds)
            for new_d in new_ds:
                new_x = tile[0]+new_d[0]
                new_y = tile[1]+new_d[1]
                if new_x < 0 or len(grid_out[0]) <= new_x or new_y < 0 or len(grid_out) <= new_y:
                    continue
                if new_d not in grid_out[new_y][new_x]:
                    tiles.append((new_x, new_y))
                    grid_out[new_y][new_x].add(new_d)

    print('\n'.join(grid))
    print('\n'.join(''.join('#' if len(s)>0 else '.' for s in row) for row in grid_out))

    count = 0
    for row in grid_out:
        for s in row:
            if len(s) > 0:
                count += 1
    return count

print(count_from_pos(0,0,RIGHT))