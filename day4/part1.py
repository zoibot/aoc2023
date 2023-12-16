def points(card):
    _, card = card.split(':')
    winningStr, haveStr = card.split('|')
    winning = set(int(n) for n in winningStr.split())
    matches = len([n for n in haveStr.split() if int(n) in winning])
    return 2**(matches-1) if matches > 0 else 0


cards = open('input').readlines()
print(sum(points(card) for card in cards))