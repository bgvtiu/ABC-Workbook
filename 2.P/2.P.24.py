n = int(input())
top_player = ""
top_score = 0

for _ in range(n):
    name, score = input().split()
    if int(score) > top_score:
        top_player = name
        top_score = int(score)

print(top_player)