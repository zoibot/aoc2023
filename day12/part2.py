from collections import namedtuple, defaultdict

rows = open('input').readlines()


State = namedtuple('State', ['curgroupprogress', 'curgroup', 'remaininggroups'])

def march_one(n, states):
    new_states = defaultdict(int)
    for state, count in states.items():
        if n == '.' or n == '?':
            if state.curgroup == state.curgroupprogress:
                new_state = State(curgroupprogress=0, curgroup=0, remaininggroups=state.remaininggroups)
                new_states[new_state] += count
        if n == '#' or n == '?':
            if state.curgroup > state.curgroupprogress:
                new_state = State(curgroupprogress=state.curgroupprogress+1, curgroup=state.curgroup, remaininggroups=state.remaininggroups)
                new_states[new_state] += count
            elif state.curgroup == 0:
                if len(state.remaininggroups) > 0:
                    new_state = State(curgroupprogress=1, curgroup=state.remaininggroups[0], remaininggroups=state.remaininggroups[1:])
                    new_states[new_state] += count
    return new_states

def march(arr, groups):
    initial_state = State(
        curgroupprogress=0,
        curgroup=0,
        remaininggroups=tuple(groups),
    )
    states = defaultdict(int)
    states[initial_state] = 1
    for n in arr:
        states = march_one(n, states)
    goodstates = defaultdict(int)
    t=0
    for state, count in states.items():
        if len(state.remaininggroups) == 0 and (state.curgroup == state.curgroupprogress):
            t += count
    return t

total = 0
for row in rows:
    sarrangement, groupstr = row.split()
    sgroups = [int(x) for x in groupstr.split(',')]
    arrangement = '?'.join([sarrangement]*5)
    groups = sgroups * 5
    m = march(arrangement, groups)
    total += m

print('total', total)

