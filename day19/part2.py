def parse_flows(f):
    flows = {'A':'A', 'R':'R'}
    for raw_flow in f:
        name, rest = raw_flow.split('{')
        rules = []
        for raw_rule in rest[:-2].split(','):
            if ':' in raw_rule:
                raw_cond, result = raw_rule.split(':')
                condvar = raw_cond[0]
                condop = raw_cond[1]
                condval = int(raw_cond[2:])
                rules.append({
                    'cond': {'var': condvar, 'op': condop, 'val': condval},
                    'result': result,
                })
            else:
                rules.append({'result': raw_rule})
        flows[name] = rules
    return flows

def split_range(rg, op, val):
    lo, hi = rg 
    # TODO could probably simplify this
    if op == '<':
        if hi < val:
            return rg, None
        elif lo > val:
            return None, rg
        else:
            return (lo, val-1), (val, hi)
    elif op == '>':
        if lo > val:
            return rg, None
        elif hi < val:
            return None, rg
        else:
            return (val+1, hi), (lo, val)


def num_parts(part):
    total = 1
    for c in 'xmas':
        total *= part[c][1] - part[c][0] + 1
    return total

inp = open('input').readlines()
br = inp.index('\n')
flows = parse_flows(inp[:br])

possible_parts = [{'flow':'in','rule':0,'x':(1,4000), 'm':(1,4000), 'a':(1,4000), 's':(1,4000)}]
all_possible = 0

flow = flows['in']
flowname = 'in'

while len(possible_parts) > 0:
    p = possible_parts.pop(0)
    print(possible_parts)
    if p['flow'] == 'A':
        print('accepted', p)
        all_possible += num_parts(p)
        continue
    if p['flow'] == 'R':
        continue
    rule = flows[p['flow']][p['rule']]
    if 'cond' in rule:
        range_pass, range_fail = split_range(p[rule['cond']['var']], rule['cond']['op'], rule['cond']['val'])
        if range_pass is not None:
            ppass = p.copy()
            ppass[rule['cond']['var']] = range_pass
            ppass['flow'] = rule['result']
            ppass['rule'] = 0
            possible_parts.append(ppass)
        if range_fail is not None:
            pfail = p.copy()
            pfail[rule['cond']['var']] = range_fail
            pfail['rule'] += 1
            possible_parts.append(pfail)
    else:
        p['flow'] = rule['result']
        p['rule'] = 0
        possible_parts.append(p)

print(num_parts({'flow':'in','rule':0,'x':(1,4000), 'm':(1,4000), 'a':(1,4000), 's':(1,4000)}))
print(all_possible)