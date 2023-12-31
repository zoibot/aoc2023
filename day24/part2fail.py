import numpy as np

def isinteger(x):
    return np.equal(np.mod(x, 1), 0)

def normalize(x):
    return x / np.linalg.norm(x)

stones = []
for line in open('input').readlines():
    raw_pos, raw_vel = line.strip().split(' @ ')
    p = np.array([int(x) for x in raw_pos.split(', ')])
    v = np.array([int(x) for x in raw_vel.split(', ')])
    stones.append((p, v))

# pick t0
# find plane of line and point?
# 

t0 = 12500000
p0 = stones[0][0]
v0 = stones[0][1]
p = p0 + v0 * t0
s1 = stones[4]
while True:
    if t0 % 100000 == 0: print(t0)
    # find plane containing guessed point and next ray
    n = np.cross(s1[0]-p, s1[0]+s1[1]-p)
    # check if all other rays cross the plane at integer points
    found = True
    p1 = None
    t1 = None
    for s in stones[1:]:
        if np.dot(s[1], n) == 0:
            if np.dot(s[0] - p, n) != 0:
                found = False
                break
            continue
        d = np.dot(p-s[0], n) / np.dot(s[1], n)
        if not isinteger(d).all() or d < 0:
            found = False
            break
        if p1 is None:
            p1 = s[0] + s[1] * d
            p1 = p1.astype(int)
            t1 = int(d)

    if not found: # TODO combine continues or use function
        t0 += 1
        p += v0
        continue

    print('found!', t0)

    # we have a candidate line  p + (p - p1)*(t-t0)/t1, now test it
    rv = p1-p
    if not isinteger(rv).all():
        t0 += 1
        continue
    rv = rv.astype(int)
    rv = rv / int(t1 - t0)
    rp = p - rv*t0
    print(t0,t1,t1-t0)
    print(rp, rv)
    break




    # seems like I don't need to test at this point
    fail = False
    print('testing line', t0)
    for s in stones:
        t = np.zeros(3)
        for i in range(3):
            if s[1][i] - rv[i] == 0:
                if s[0][i] != rp[i]:
                    fail = True
                    break
                else:
                    t[i] = 0
                    continue
            t[i] = (s[0][i] - rp[i])/(s[1][i] - rv[i])
        for i in range(3):
            if t[i] != t[0] and t[i] != 0:
                fail = True
                break
        if fail:
            break
        #rp + rv * t = s[0] + s[1] * t
        #rp - s[0] = (s[1]-rv) * t
        #print(s[1], rv)
        #t = (rp - s[0])/(s[1] - rv)
        #print(t)
    if not fail:
        print('success')
        print(rp, rv)
        exit(0)
    else:
        print('fail')





# don't care about time, just one line that intersects all the lines then figure out the rest
# with the line, pick another line and find the time of intersection then get to t 0
# pick a line, march through time, try to fit line that passes current line
# no doesn't work
# new idea- big system of equations to solve for times for different lines
# rp + rv * t1 = p1 + v1 * t1
# rp + rv * t2 = p2 + v2 * t2
# [vi-rv] * [t] = [p - rp]
# (v0x - rvx) * t0 = p0x - rpx
# (v0y - rvy) * t0 = p0y - rpy
# (v1y - rvy) * t1 = p1y - rpy
# can't make it work because it's not linear - rock velocity * time are both unknown
# (t1-t0) * rvx + p0x = p1x
# rvx = p1x - p0x / t1-t0
# fixed t0 -> doesn't help. TOO MANY VARIABLES!!!!

# back to pick a line and march
# use two other lines to fix velocity?
# p0 + v0 * t0 + rv*(t1-t0) = p1 + v1 * t1
# p0-p1 + v0 * t0 + rv *t1 -rv*t0 = v1 * t1
# p1 + v1 * t1 + rv*(t2-t1) = p2 + v2 * t2


