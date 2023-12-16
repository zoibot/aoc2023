garbo = open('input').readlines()
seedline = garbo[0]
_, seedline = seedline.split(':')
seeds = [int(s) for s in seedline.split()]

curmap = None
maps = []
i = 1
while i < len(garbo):
    if garbo[i] == '\n':
        curmap = []
        maps.append(curmap)
        i += 2
        continue
    dest_start, source_start, length = garbo[i].split()
    curmap.append((int(dest_start), int(source_start), int(length)))
    i += 1
#NOT ACTUALLY PART 1, FORGOT TO SAVE BEFORE EDITING

minval = 4256593725
i = 0
print(len(seeds))
while i < len(seeds)-1:
    print(i)
    seed_start = seeds[i]
    seed_len = seeds[i+1]
    i+=2
    for seed in range(seed_start, seed_start + seed_len):
        curval = seed
        for map in maps:
            for (dest_start, source_start, l) in map:
                if source_start <= curval and curval < source_start+l:
                    curval = dest_start + (curval - source_start)
                    break
        minval = min(minval, curval)

#print(all_vals)
print(minval)