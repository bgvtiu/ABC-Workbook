n, m = [int(x) for x in input().split()]
following = [0 for _ in range(n)]
followers = [0 for _ in range(n)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    following[u-1] += 1
    followers[v-1] += 1

print(*following)
print(*followers)