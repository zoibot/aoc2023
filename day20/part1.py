from collections import defaultdict

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

lo_pulses = hi_pulses = 0

for _ in range(1000):
    q = [('broadcaster', '', False)]
    while len(q) > 0:
        mod, fr, pulse = q.pop(0)
        if pulse:
            hi_pulses += 1
        else:
            lo_pulses += 1
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

print(hi_pulses, lo_pulses)
print(hi_pulses * lo_pulses)
