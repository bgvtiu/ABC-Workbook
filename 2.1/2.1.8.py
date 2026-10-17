n = int(input())
flowers = [int(x) for x in input().split()]
growth = []

for x in flowers:
    x += 1
    growth.append(x)
print(*growth)