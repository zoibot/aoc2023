def repeat(iter):
    while True:
        for item in iter:
            yield item

def parse_nodes(inp):
    nodes = {}
    for nodeline in inp:
        name, conns = nodeline.split('=')
        connlist = conns[2:-2].split(', ')
        nodes[name.strip()] = connlist
    return nodes

inp = open('input').readlines()

directions = inp[0]
nodes = parse_nodes(inp[2:])

cur = 'AAA'
steps = 0
for d in repeat(directions.strip()):
    if cur == 'ZZZ':
        break
    if d == 'L':
        cur = nodes[cur][0]
    elif d == 'R':
        cur = nodes[cur][1]
    steps += 1

print(steps)