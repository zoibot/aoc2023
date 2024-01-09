import random
from collections import defaultdict, namedtuple
from copy import deepcopy

Node = namedtuple('Node', ['name', 'size'])
Edge = namedtuple('Edge', ['a', 'b'])

nodes = {}
edges = []
for component in open('input').readlines():
    name, connections = component.strip().split(': ')
    nodes[name] = Node(name, 1)
    for conn in connections.split(' '):
        e = Edge(name, conn)
        edges.append(e)
        nodes[conn] = Node(conn, 1)

    
def karger(edges, nodes):
    es = edges.copy()
    v = nodes.copy()
    while len(v) > 2:
        re = random.choice(es)
        es = [e for e in es if e != re]
        anode = v[re.a]
        bnode = v[re.b]
        newnode = Node(re.a + '|' + re.b, anode.size + bnode.size)
        v[newnode.name] = newnode

        newedges = []
        for e in es:
            if e.a == re.a or e.a == re.b:
                newedges.append(e.b)
            elif e.b == re.a or e.b == re.b:
                newedges.append(e.a)

        es = [e for e in es if e.a != re.a and e.a != re.b and e.b != re.a and e.b != re.b]
        for ne in newedges:
            es.append(Edge(newnode.name, ne))

        del v[re.b]
        del v[re.a]
    return len(es), v

c = 0
while c != 3:
    print(c)
    c, n = karger(edges, nodes)

print(c, n)
nks = list(n.keys())
n0 = n[nks[0]].size
n1 = n[nks[1]].size
print(n0, n1, n0 * n1)