n = int(input())
cards = [input().split() for _ in range(n)]

counter = 0
for c in cards:
    if c[0] != cards[0][0] and c[2] != cards[0][2]:
        print(" ".join(c))
        counter += 1

if counter == 0:
    print("empty deck")