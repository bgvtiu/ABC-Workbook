n = int(input())
cards = [input().split() for _ in range(n)]

face = 0
for i in range(n):
    if cards[i][0] == "King" or cards[i][0] == "Queen" or cards[i][0] == "Jack":
        face += 1

print(face)