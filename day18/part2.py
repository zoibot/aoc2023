from collections import defaultdict

def clean_intervals(intervals):
    #lazy cleanup
    clean = []
    i = 0
    while i < len(intervals):
        curlo, curhi = intervals[i]
        if curhi - curlo == 0:
            i += 1
            continue
        while i+1 < len(intervals) and curhi == intervals[i+1][0]:
            curhi = intervals[i+1][1]
            i += 1
        
        clean.append((curlo, curhi))
        i += 1
    return clean

def flip_interval(intervals, new_interval):
    new_intervals = []
    newlo, newhi = new_interval
    for lo, hi in intervals:
        if hi <= newlo: # this interval is completely below new one 
            new_intervals.append((lo,hi))
            continue
        elif lo >= newhi: # this interval is completely above new one
            new_intervals.append((newlo,newhi))
            newlo = newhi = 0
            new_intervals.append((lo,hi))
        elif lo > newlo: # this interval overlaps or is contained by new one
            new_intervals.append((newlo, lo))
            if hi < newhi:
                newlo = hi
            else:
                new_intervals.append((newhi, hi))
                newlo = newhi = 0
        elif newlo < hi: # this interval overlaps or contains new one
            new_intervals.append((lo, newlo))
            if hi < newhi:
                newlo = hi
            else:
                new_intervals.append((newhi, hi))
                newlo = newhi = 0
    if newhi - newlo > 0:
        new_intervals.append((newlo, newhi))

    return clean_intervals(new_intervals)

def merge_interval(xs, y):
    new_xs = []
    newlo, newhi = y
    for lo, hi in xs:
        if hi < newlo: # this interval is completely below new one 
            new_xs.append((lo,hi))
            continue
        elif lo > newhi: # this interval is completely above new one
            new_xs.append((newlo,newhi))
            newlo = newhi = 0
            new_xs.append((lo,hi))
        elif lo > newlo: # this interval overlaps or is contained by new one
            newhi = max(hi, newhi)
        elif newlo < hi: # this interval overlaps or contains new one
            newlo = lo
            newhi = max(hi, newhi)
    if newhi - newlo > 0:
        new_xs.append((newlo, newhi))
    return clean_intervals(new_xs)


def merge_intervals(xs, ys):
    for y in ys:
        xs = merge_interval(xs, y)
    return xs

def intervals_size(intervals):
    size = 0
    for (lo, hi) in intervals:
        size += hi - lo + 1
    return size

dirs = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

def parse(line):
    ds, ls, _ = line.split()
    d = dirs[ds]
    l = int(ls)
    return l, d

dirshex = {
    '2': (-1, 0),
    '0': (1, 0),
    '3': (0, -1),
    '1': (0, 1),
}
def parsehex(line):
    _, hexs = line.split('#')
    l = int(hexs[:5], 16)
    d = dirshex[hexs[5]]
    return l, d

curx, cury = 0, 0
pts = defaultdict(set)
pts[0].add(0)

for line in open('input').readlines():
    l, d = parsehex(line)
    curx += d[0] * l
    cury += d[1] * l
    pts[cury].add(curx)

rows = list(pts.items())
rows.sort()

area = 0
x_intervals = []
for i, (y, xset) in enumerate(rows[:-1]):
    if len(xset) % 2 == 1:
        print('odd number of points on line, something wrong')
        exit(1)
    xs = list(xset)
    xs.sort()

    prev_intervals = x_intervals
    for j in range(0, len(xs), 2):
        x_intervals = flip_interval(x_intervals, (xs[j], xs[j+1]))
    
    edge_width = intervals_size(merge_intervals(prev_intervals, x_intervals))
    width = intervals_size(x_intervals)

    nexty = rows[i+1][0]
    height = nexty - y - 1
    
    area += edge_width
    area += height * width
    
    #print('ROW')
    #print(x_intervals)
    #print(edge_width)
    #print(height,width)
    #print(y, area)
    #if y == -189:
    #    print(edge_width)
    #    print(merge_intervals(prev_intervals, x_intervals))
    #    print(x_intervals)

# LAST LINE
last_edge_width = intervals_size(x_intervals)
#print('last line', x_intervals, last_edge_width)
area += last_edge_width

print(area)