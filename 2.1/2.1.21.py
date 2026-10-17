n = int(input())
cards = [input().split() for _ in range(n)]
order = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

for i in range(n):
    if order.index(cards[i][2]) <= order.index(cards[-1][2]):
        print(" ".join(cards[i]))