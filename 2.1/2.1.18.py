n = int(input())
cards = [input() for _ in range(n)]

cards[0], cards[-1] = cards[-1], cards[0]
for i in range(n):
    print(cards[i])