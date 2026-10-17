n = int(input())
cards = [input().split() for _ in range(n)]
suit = input()

counter = 0
for c in cards:
    if c[2] == suit:
        print(" ".join(c))
        counter +=1

if counter == 0:
    print("no cards")