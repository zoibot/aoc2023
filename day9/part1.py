def derive(seq):
    return [b-a for (a,b) in zip(seq, seq[1:])]

def derivations(seq):
    derivations = [seq]
    curseq = seq
    while not all(x == 0 for x in curseq):
        nextseq = derive(curseq)
        derivations.append(nextseq)
        curseq = nextseq
    return derivations

def extrapolate(seq):
    last = 0
    for seq in reversed(derivations(seq)):
        last = seq[-1] + last
    return last

seqs = [[int(x) for x in l.split()] for l in open('input').readlines()]


#for seq in seqs:
#   print(extrapolate(seq))

print(sum(extrapolate(seq) for seq in seqs))