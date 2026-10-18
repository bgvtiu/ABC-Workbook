n, m = [int(x) for x in input().split()]
ballots = [int(x) for x in input().split()]
votes = [0 for _ in range(n)]

for i in range(m):
    votes[ballots[i]-1] += 1

print(*votes)