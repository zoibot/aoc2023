def points(card):
    _, card = card.split(':')
    winningStr, haveStr = card.split('|')
    winning = set(int(n) for n in winningStr.split())
    matches = len([n for n in haveStr.split() if int(n) in winning])
    return matches

def card_number(card):
    name, _ = card.split(':')
    _, no = name.split()
    return int(no)

#this is dumb should do dynamic programming but i'm lazy
cards = open('input').readlines()
processed = 0
q = cards[:]
while len(q)>0:
    card = q.pop(0)
    processed += 1
    new_cards = points(card)
    if new_cards > 0:
        card_no = card_number(card)
        for i in range(card_no, card_no+new_cards):
            q.append(cards[i])


print(processed)