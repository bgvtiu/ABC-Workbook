n = int(input())
cards = [input() for _ in range(n)]
l, r = [int(x) for x in input().split()]

for c in cards[l-1: r]:
    print(c)
for c in cards[:l-1]:
    print(c)
for c in cards[r:]:
    print(c)