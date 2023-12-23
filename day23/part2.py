from collections import defaultdict

def neighbors(p):
    return (p[0]-1,p[1]), (p[0]+1,p[1]), (p[0],p[1]-1), (p[0],p[1]+1)

grid = open('input').readlines()

start = None
for i, c in enumerate(grid[0]):
    if c == '.':
        start = (i, 0)

paths = defaultdict(dict)
paths[start] = {}

seen = set()
end = None
q = [(start, (start[0],start[1]+1), 1)]
ct = 100
while len(q) > 0:
    begin, cur, baselen = q.pop(0)
    curlen = 0
    slope = False
    while True:
        if cur in seen: break
        seen.add(begin)
        seen.add(cur)
        for n in neighbors(cur):
            if n[1] < 0: continue
            if n in seen: continue
            c = grid[n[1]][n[0]]
            if c != '#':
                cur = n
                curlen += 1
                break
        if c != '.':
            slope = True
        if c == '.' and slope:
            paths[begin][cur] = baselen+curlen
            for n in neighbors(cur):
                c = grid[n[1]][n[0]]
                if c != '#' and n not in seen:
                    q.append((cur, n, 1))
            break
        if cur[1] == len(grid)-1:
            end = cur
            paths[begin][end] = baselen+curlen
            break


#print('graph {')
#for node, pats in paths.items():
#    for pathnode, l in pats.items():
#        print('"',node,'" -- "',pathnode,'" [label=',l,']')
#print('}')

allpaths = paths.copy()
for node, paths in paths.items():
    for pathnode, l in paths.items():
        allpaths[pathnode][node] = l

def connected(nodes):
    ns = set(nodes)
    n = ns.pop()
    q = [n]
    while len(q) > 0:
        n = q.pop(0)
        for nd in allpaths[n]:
            if nd in ns:
                ns.remove(nd)
                q.append(nd)
    return len(ns) < 3 # this is kind of magic, not quite sure what's happening here


nodes = frozenset(allpaths.keys())
def longest_path(nodes, st):
    if not connected(nodes):
        return []
    if st == end:
        #print('found end', len(nodes))
        return [0]
    m = [] 
    for nxt, l in allpaths[st].items():
        if nxt in nodes:
            ln = longest_path(frozenset(node for node in nodes if node != st), nxt)
            if len(ln) != 0 and sum(ln) + l > sum(m):
                m = [l] + ln
    return m

print(start)
print(len(nodes))
x = (longest_path(nodes, start))
print(len(x))
print(x)
print(sum(x))

