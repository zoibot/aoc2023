engine = open('input').readlines()

parttotal = 0
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
                if not engine[y-1][dx].isdigit() and engine[y-1][dx] != '.':
                    part = 'top'
                    break
        if y+1 < len(engine):
            for dx in range(max(x-1,0),min(x+numberlen+1, len(engine[y+1])-1)):
                if not engine[y+1][dx].isdigit() and engine[y+1][dx] != '.':
                    part = 'bottom'
                    break
        if x > 0:
            if not engine[y][x-1].isdigit() and engine[y][x-1] != '.':
                part = 'left'
        if x+numberlen+1 < len(engine[y]):
            if not engine[y][x+numberlen].isdigit() and engine[y][x+numberlen] != '.':
                part = 'right'
        if part:
            if number=='977':
                print(part, number)
            num = int(number)
            parttotal += num
print(parttotal)
