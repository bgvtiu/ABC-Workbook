n = int(input())
cards = [input().split() for _ in range(n)]

counter = 0
for i in range(1, n):
    if cards[i-1][0] == "King" or cards[i-1][0] == "Queen" or cards[i-1][0] == "Jack": 
        print(" ".join(cards[i]))
        counter +=1

if counter == 0:
    print("no cards")