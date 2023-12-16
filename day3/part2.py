engine = open('input').readlines()

gears = {}
for y in range(len(engine)):
    for x in range(len(engine[y])):
        if engine[y][x].isdigit() and (x == 0 or not engine[y][x-1].isdigit()):
            number = engine[y][x]
            numberlen = 1
            for dx in range(1,4):
                if x+dx >= len(engine[y]): 
                    break
                if engine[y][x+dx].isdigit():
                    numberlen += 1
                    number += engine[y][x+dx]
                else:
                    break
        else:
            continue
        part = False
        if y > 0:
            for dx in range(max(x-1,0),min(x+numberlen+1, len(engine[y-1])-1)):
                if engine[y-1][dx] == '*':
                    gears[(y-1,dx)] = gears.get((y-1,dx), []) + [int(number)]
        if y+1 < len(engine):
            for dx in range(max(x-1,0),min(x+numberlen+1, len(engine[y+1])-1)):
                if engine[y+1][dx] == '*':
                    gears[(y+1,dx)] = gears.get((y+1,dx), []) + [int(number)]
        if x > 0:
            if engine[y][x-1] == '*':
                gears[(y,x-1)] = gears.get((y,x-1), []) + [int(number)]
        if x+numberlen+1 < len(engine[y]):
            if engine[y][x+numberlen] == '*':
                gears[(y,x+numberlen)] = gears.get((y,x+numberlen), []) + [int(number)]

geartotal = 0
for gear in gears.values():
    if len(gear) == 2:
        geartotal += gear[0]*gear[1]
print(geartotal)