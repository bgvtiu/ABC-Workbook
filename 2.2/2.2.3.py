n = int(input())
cards = [input().split() for _ in range(n)]

hearts = 0
for i in range(n):
    if cards[i][2] == "Hearts":
        hearts += 1

print(hearts)