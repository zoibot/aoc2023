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

def parse_parts(f):
    parts = []
    for raw_part in f:
        part = {}
        vals = raw_part[1:-2].split(',')
        for v in vals:
            n, ir = v.split('=')
            part[n] = int(ir)
        parts.append(part)
    return parts



inp = open('input').readlines()
br = inp.index('\n')
flows = parse_flows(inp[:br])
parts = parse_parts(inp[br+1:])

accepted_parts = []
for part in parts:   
    flow = flows['in']
    flowname = 'in'
    while True:
        if flow == 'A': 
            accepted_parts.append(part)
            break
        if flow == 'R':
            break
        for rule in flow:
            ok = True
            if 'cond' in rule:
                if rule['cond']['op'] == '<':
                    ok = part[rule['cond']['var']] < rule['cond']['val']
                if rule['cond']['op'] == '>':
                    ok = part[rule['cond']['var']] > rule['cond']['val']
            if ok:
                flowname = rule['result']
                flow = flows[flowname]
                break

print(accepted_parts)
total = 0
for part in accepted_parts:
    total += sum(part.values())
print(total)
