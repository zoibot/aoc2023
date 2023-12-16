def points(card):
    _, card = card.split(':')
    winningStr, haveStr = card.split('|')
    winning = set(int(n) for n in winningStr.split())
    matches = len([n for n in haveStr.split() if int(n) in winning])
    return matches

cards = open('input').readlines()
card_counts = [1]*len(cards)

for i, card in enumerate(cards):
    p = points(card)
    for j in range(i+1, i+1+p):
        card_counts[j] += card_counts[i]


print(sum(card_counts))