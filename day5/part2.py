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
for map in maps:
    map.sort(key=lambda r: r[1])


def translate_seed_range(seed_range, mp):
    range_start, range_len = seed_range
    result_ranges = []

    for rule in mp:
        dest_start, source_start, map_len = rule

        # unmapped range
        if range_start < source_start:
            result_ranges.append((range_start, min(source_start - range_start, range_len)))
            range_len -= min(source_start - range_start, range_len)
            range_start = source_start
            if range_len == 0:
                # we're done
                break

        # beginning in range
        if source_start <= range_start and range_start < source_start+map_len:
            # range contains map rule, need to break it up
            if source_start+map_len < range_start+range_len:
                result_ranges.append((dest_start+(range_start-source_start), map_len-(range_start-source_start)))
                range_len -= map_len-(range_start-source_start)
                range_start = source_start + map_len
            else: # map rule extends beyond range, we're done
                result_ranges.append((dest_start+(range_start-source_start), range_len))
                range_start = range_start+range_len
                range_len = 0
                break
        if len(result_ranges) > 0 and result_ranges[-1][1] < 0:
            print(rule)
            print(range_start, range_len)
            print(result_ranges)
            exit(1)
        if range_len < 0:
            print(rule)
            print(range_start, range_len)
            print(result_ranges)
            exit(1)
    
    # any remaining unmapped
    if range_len > 0:
        result_ranges.append((range_start, range_len))
    return result_ranges

def merge_ranges(lower, higher):
    range_start = lower[0]
    range_len = max(lower[1], higher[0]-lower[0]+higher[1])
    return (range_start,range_len)

def consolidate_ranges(ranges):
    ranges.sort(key=lambda r: r[0])
    new_ranges = []
    current_range = ranges.pop(0)
    while len(ranges) > 0:
        next_range = ranges.pop(0)
        if current_range[0]+current_range[1] >= next_range[0]:
            current_range = merge_ranges(current_range, next_range)
        else:
            new_ranges.append(current_range)
            current_range = next_range
    new_ranges.append(current_range)
    return new_ranges

def filter_empty(ranges):
    return [r for r in ranges if r[1] > 0]

def count_ranges(ranges):
    return sum(r[1] for r in ranges)

i = 0

seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
for mp in maps:
    print((seed_ranges))
    print(mp)
    next_ranges = []
    for seed_range in seed_ranges:
        next_ranges = next_ranges + translate_seed_range(seed_range, mp)
    if count_ranges(next_ranges) != count_ranges(seed_ranges):
        print('uh oh')
        exit(1)
    seed_ranges = next_ranges# filter_empty(consolidate_ranges(next_ranges))


print(min(n[0] for n in seed_ranges))
