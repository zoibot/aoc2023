def hasha(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

instructions = open('input').read().split(',')

hmap = [[] for _ in range(256)]

for inst in instructions:

    if inst[-1] == '-':
        label = inst[:-1]
        h = hasha(label)
        found = None
        for (i, (l, _)) in enumerate(hmap[h]):
            if label == l:
                found = i
        if found is not None:
            hmap[h].pop(found)
    else:
        label = inst[:-2]
        h = hasha(label)
        num = int(inst[-1])
        found = None
        for (i, (l, _)) in enumerate(hmap[h]):
            if label == l:
                found = i
        if found is not None:
            hmap[h][found] = (label,num)
        else:
            hmap[h].append((label,num))

power = 0
for boxnum, box in enumerate(hmap, 1):
    for slot, (_, lens) in enumerate(box, 1):
        power += boxnum * slot * lens

print(power)
