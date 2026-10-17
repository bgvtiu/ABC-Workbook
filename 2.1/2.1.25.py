n = int(input())
cards = [input() for _ in range(n)]

for i in range(int(n/2)):
    print(cards[i])
    print(cards[i + int(n/2)])