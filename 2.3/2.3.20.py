def gossip(x, y):
    if secret[x] == True and secret[y] == False:
        secret[y] = True

m, n = [int(x) for x in input().split()]
secret = [False for _ in range(m)]
secret[0] = True

for _ in range(n):
    u, v = [int(x) for x in input().split()]
    gossip(u, v), gossip(v, u)

print(secret.count(True))