from collections import defaultdict

moduledefs = open('input').readlines()

mod_types = {}
mod_outs = {}
flipflopmem = {}
invmem = defaultdict(dict)

for moduledef in moduledefs:
    name, outstr = moduledef.strip().split(' -> ')
    outs = outstr.split(', ')
    if name[0] == '%':
        name = name[1:]
        mod_types[name] = '%'
        flipflopmem[name] = False
    elif name[0] == '&':
        name = name[1:]
        mod_types[name] = '&'
    elif name == 'broadcaster':
        mod_types[name] = name
    else:
        print('unknown module', name)
    for out in outs:
        invmem[out][name] = False 
    mod_outs[name] = outs

print(mod_types)
print(len(flipflopmem))

lo_pulses = 0
hi_pulses = 0
presses = 0
for i in range(10):
    presses += 1
    q = [('broadcaster', '', False)]
    while len(q) > 0:
        mod, fr, pulse = q.pop(0)
        if mod == 'rx' and not pulse:
            print('FOUND IT! ', n)
            exit(0)
        if pulse:
            hi_pulses += 1
        else:
            lo_pulses += 1
        if mod not in mod_types:
            continue
        typ = mod_types[mod]
        out = None
        if typ == '%' and not pulse:
            flipflopmem[mod] = not flipflopmem[mod]
            print(mod, flipflopmem[mod])
            out = flipflopmem[mod]
        elif typ == '&':
            invmem[mod][fr] = pulse
            out = not all(invmem[mod].values())
        elif typ == 'broadcaster':
            out = False
        if out is not None:
            for o in mod_outs[mod]:
                q.append((o, mod, out))
    print('------')
print(lo_pulses, hi_pulses)
print(lo_pulses*hi_pulses)