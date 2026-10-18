n, m = [int(x) for x in input().split()]
friends = [0 for _ in range(n)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]

    friends[u-1] += 1
    friends[v-1] += 1

print(*friends)