import re

def rreplace(s, old, new):
    li = s.rsplit(old)
    return new.join(li)

numnames = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
def sub(w):
    return numnames.get(w, str(w))


ls = open('input.txt').readlines()
vals = []
for l in ls:
    firstmatch = re.search('|'.join(numnames)+'|\d', l)
    lastmatch = re.search('.*('+'|'.join(numnames)+'|\d)', l)
    first = sub(firstmatch[0])
    last = sub(lastmatch[1])
    vals.append(int(first+last))
print(vals)
print(sum(vals))

