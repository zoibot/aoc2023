
gamelines = open('input').readlines()
total = 0
gameno = 0
for gameline in gamelines:
    gameno += 1
    fail = False
    _, subsetss = gameline.split(': ')
    subsets = subsetss.split('; ')
    for subset in subsets:
        cubes = subset.split(', ')
        for cube in cubes:
            nos, color = cube.split(' ')
            color = color.strip()
            no = int(nos)
            if color == 'red' and no > 12:
                fail = True
                break
            if color == 'green' and no > 13:
                fail = True
                break
            if color == 'blue' and no > 14:
                fail = True
                break
    if not fail:
        total += gameno
    else:
        pass

print(total)