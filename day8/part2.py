from math import lcm #TODO

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

cur_nodes = [node for node in nodes.keys() if node[2] == 'A']

first_paths = [0] * len(cur_nodes)
steps = 0
for d in repeat(directions.strip()): # might need LCM of cycles
    if all(node[2] == 'Z' for node in cur_nodes):
        break
    for i, node in enumerate(cur_nodes):
        if node[2] == 'Z':
            if first_paths[i] == 0:
                first_paths[i] = steps
    if all(x > 0 for x in first_paths):
        print(first_paths)
        break
    if d == 'L':
        cur_nodes = [nodes[node][0] for node in cur_nodes]
    elif d == 'R':
        cur_nodes = [nodes[node][1] for node in cur_nodes]
    steps += 1

print(steps)
print(lcm(*first_paths))