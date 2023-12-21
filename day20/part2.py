from collections import defaultdict
from math import lcm

mod_types = {} 
mod_outs = {}

ffmem = {}
nandmem = defaultdict(dict)

for raw_mod in open('input').readlines():
    name, outstr = raw_mod.strip().split(' -> ')
    if name[0] == '%':
        name = name[1:]
        mod_types[name] = '%'
        ffmem[name] = False
    elif name[0] == '&':
        name = name[1:]
        mod_types[name] = '&'
    else:
        mod_types[name] = name
    outs = outstr.split(', ')
    mod_outs[name] = outs
    for out in outs:
        nandmem[out][name] = False

print(mod_types)
print(mod_outs)

for n in range(1,10000):
    q = [('broadcaster', '', False)]
    while len(q) > 0:
        mod, fr, pulse = q.pop(0)
        if mod == 'th' and pulse:
            print(fr, 'high', n)
        if mod not in mod_types:
            continue
        typ = mod_types[mod]
        out = None
        if typ == '%' and not pulse:
            ffmem[mod] = not ffmem[mod]
            out = ffmem[mod]
        elif typ == '&':
            nandmem[mod][fr] = pulse
            out = not all(nandmem[mod].values())
        elif typ == 'broadcaster':
            out = pulse
        if out is not None:
            for outmod in mod_outs[mod]:
                q.append((outmod, mod, out))
print(lcm(3739, 3793, 3923, 4027))

