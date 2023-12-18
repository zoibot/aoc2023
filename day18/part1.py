from PIL import Image

def print_dug(dug):
    minx = min(p[0] for p in dug)
    maxx = max(p[0] for p in dug)
    miny = min(p[1] for p in dug)
    maxy = max(p[1] for p in dug)
    grid = []
    for y in range(miny, maxy+1):
        row = ''
        for x in range(minx, maxx+1):
            row += '#' if (x,y) in dug else '.'
        grid.append(row)
    print('\n'.join(grid))


def show_dug(dug):
    minx = min(p[0] for p in dug)
    maxx = max(p[0] for p in dug)
    miny = min(p[1] for p in dug)
    maxy = max(p[1] for p in dug)
    im = Image.new('1', (maxx-minx+1, maxy-miny+1))
    for y in range(miny, maxy+1):
        row = ''
        for x in range(minx, maxx+1):
            if (x,y) in dug:
                im.putpixel((x-minx,y-miny), 1)
    im.show()
        


dirs = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

curx, cury = 0, 0
dug = set(((0,0),))

for line in open('input').readlines():
    ds, ls, _ = line.split() # color doesn't make sense. corners? original pit?
    d = dirs[ds]
    l = int(ls)
    for _ in range(l):
        curx += d[0]
        cury += d[1]
        dug.add((curx,cury))

#show_dug(dug)
print()

fulldug = set(dug)

minx = min(p[0] for p in dug)
maxx = max(p[0] for p in dug)
miny = min(p[1] for p in dug)
maxy = max(p[1] for p in dug)
# fill in center (could have just done flood fill lol oh well)
for y in range(miny, maxy+1):
    in_border = False
    border_up = False
    inside = False
    for x in range(minx, maxx+1):
        if (x,y) in dug:
            if not in_border:
                in_border = True
                border_up = (x,y-1) in dug
        else:
            if in_border:
                in_border = False
                if (border_up and (x-1,y+1) in dug) or (not border_up and (x-1,y-1) in dug):
                    inside = not inside
            if inside:
                fulldug.add((x,y))

#show_dug(fulldug)

print(len([_ for pt in fulldug if pt[1] <= -189]))

print(len(fulldug))