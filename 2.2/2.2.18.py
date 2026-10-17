n, x = [int(x) for x in input().split()]
players = [input().split() for _ in range(n)]
winner = []

for i in range(n):
    if players[i][1] == str(x):
        winner.append(players[i][0])

if len(winner) == 1:
    print(*winner)
else:
    print("no winner")