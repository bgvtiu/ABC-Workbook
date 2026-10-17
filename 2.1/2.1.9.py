n = int(input())
flowers = [int(x) for x in input().split()]
pruned = []

for x in flowers:
    if x > 5:
        x -= 5
    pruned.append(x)
print(*pruned)