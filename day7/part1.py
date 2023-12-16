from collections import defaultdict

raw_hands = open('input').readlines()
hands = []
for raw_hand in raw_hands:
    cards, strval = raw_hand.split()
    hands.append((cards, int(strval)))

cardranks = 'J23456789TQKA'
def hand_strength(hand):
    cards, _ = hand
    counts = defaultdict(int)
    strength = 1
    for c in cards:
        counts[c] += 1
        card_strength = cardranks.index(c)
        strength = 13 * strength + card_strength
    j = counts['J']
    counts['J'] = 0
    a = list(counts.values())
    a.sort(reverse=True)
    a[0] += j
    typ = 0
    print(a)
    if a[0] == 5:
        typ = 6 # five of a kind
    if a[0] == 4:
        typ = 5 # four of a kind
    if a[0] == 3:
        if a[1] == 2:
            typ = 4 # full house
        else:
            typ = 3 # three of a kind
    if a[0] == 2:
        if a[1] == 2:
            typ = 2 # two pair
        else:
            typ = 1 # one pair
    
    return strength + (typ * (13 ** 7))

hands.sort(key=hand_strength)
#print(hands)

total = 0
for rank, hand in enumerate(hands, 1):
    total += hand[1] * rank

print(total)