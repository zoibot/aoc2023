
gamelines = open('input').readlines()
total = 0
for gameline in gamelines:
    _, subsetss = gameline.split(': ')
    subsets = subsetss.split('; ')
    maxred, maxgreen, maxblue = 0,0,0
    for subset in subsets:
        cubes = subset.split(', ')
        for cube in cubes:
            nos, color = cube.split(' ')
            color = color.strip()
            no = int(nos)
            if color == 'red':
                maxred = max(no, maxred)
            if color == 'green':
                maxgreen = max(no, maxgreen)
            if color == 'blue':
                maxblue = max(no, maxblue)
    total += maxred * maxblue * maxgreen

print(total)