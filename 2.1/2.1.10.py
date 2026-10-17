n = int(input())
flowers = [int(x) for x in input().split()]
growth = []

for x in flowers:
    if x == min(flowers):
        x = max(flowers)
    growth.append(x)
print(*growth)