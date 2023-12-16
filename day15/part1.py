def hasha(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

instructions = open('input').read().split(',')
print(sum(hasha(i) for i in instructions))