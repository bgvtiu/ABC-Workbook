n = int(input())
coins = [int(x) for x in input().split()]
t = int(input())

for _ in range(t):
    player, desc = input().split()
    player = int(player) - 1 #convert to zero-indexing

    if desc == "RIGHT":
        coins[player - 1] += coins[player] // 2
    else: #cyclic shifts type formula
        coins[int((player - n/2) % n)] += coins[player] // 2

    coins[player] -= coins[player] // 2

print(*coins)