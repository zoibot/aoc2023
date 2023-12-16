rows = open('input').readlines()


def possible(arr, groups):
    arr = arr[:arr.index('?')]
    gps = [gp for gp in arr.split('.') if len(gp) > 0]
    dgroups = groups[:]

    if len(gps) > len(groups):
        return False
    for gp in gps:
        if len(gp) > dgroups.pop(0):
            return False
    return True

def match(arr, groups):
    gps = [gp for gp in arr.split('.') if len(gp) > 0]
    dgroups = groups[:]
    if len(gps) != len(groups):
        return False
    for gp in gps:
        if len(gp) != dgroups.pop(0):
            return False
    print(arr)
    return True

def find_matches(arr, groups, remaining_spots, remaining_springs):
    if remaining_springs > remaining_spots or remaining_springs < 0:
        return 0
    if remaining_spots == 0:
        return 1 if match(arr, groups) else 0
    if not possible(arr, groups):
        return 0
    left, right = arr.split('?', 1)
    return find_matches(left+'.'+right, groups, remaining_spots-1, remaining_springs) + find_matches(left+'#'+right, groups, remaining_spots-1, remaining_springs-1)

# dumb way first

total = 0
for row in rows:
    arrangement, groupstr = row.split()
    groups = [int(x) for x in groupstr.split(',')]
    total_spots = len([c for c in arrangement if c == '?'])
    placeable_springs = sum(groups)-len([c for c in arrangement if c == '#'])
    m = find_matches(arrangement, groups, total_spots, placeable_springs)
    print(m)
    total += m

print('total', total)

