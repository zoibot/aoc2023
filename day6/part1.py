import math

races = [] #redacted

optionslist = []
for race in races:
    t, d = race
    zeroa = (-t + math.sqrt(t*t - 4*d))/(-2)
    zerob = (-t - math.sqrt(t*t - 4*d))/(-2)
    leftzero = math.ceil(min(zeroa,zerob))
    rightzero = math.floor(max(zeroa,zerob))
    print(leftzero,rightzero)
    print(rightzero-leftzero+1)
    optionslist.append(rightzero-leftzero+1)

total = 1
for o in optionslist:
    total *= o

print(total)
