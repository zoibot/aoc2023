stones = []
for line in open('input').readlines():
    raw_pos, raw_vel = line.strip().split(' @ ')
    p = tuple(int(x) for x in raw_pos.split(', '))
    v = tuple(int(x) for x in raw_vel.split(', '))
    stones.append((p, v))

zone = (7,27)
zone = (200000000000000,400000000000000)

total = 0
for i in range(len(stones)):
    for j in range(i+1, len(stones)):
        s1 = stones[i]
        s2 = stones[j]
        mat = (s1[1][0], -s2[1][0],
               s1[1][1], -s2[1][1])
        invdet = mat[0]*mat[3] - mat[1]*mat[2]
        if invdet == 0:
            #print(s1, s2, 'do not intersect')
            continue
        det = 1/invdet
        invmat = (det * mat[3], det * -mat[1],
                  det * -mat[2], det * mat[0])
        pvec = (s2[0][0] - s1[0][0], s2[0][1] - s1[0][1])
        t1 = invmat[0] * pvec[0] + invmat[1] * pvec[1]
        t2 = invmat[2] * pvec[0] + invmat[3] * pvec[1]
        if t1 < 0 or t2 < 0:
            #print(s1, s2, 'intersected in the past')
            continue
        intpt = (s1[0][0] + s1[1][0] * t1,
                 s1[0][1] + s1[1][1] * t1)
        inside = (zone[0] < intpt[0] and intpt[0] < zone[1] and 
                zone[0] < intpt[1] and intpt[1] < zone[1])
        #print(s1, s2, 'do intersect at', intpt, 'which inside', inside)
        if inside:
            total += 1

print(total)
# p1 + v1 * t1 = p2 + v2 * t2
# [p1-p2 + v1*t1 - v2*t2]
# [v1 -v2]t = [p2-p1]



