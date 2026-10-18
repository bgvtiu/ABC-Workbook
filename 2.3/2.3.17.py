n = int(input())
paint = [int(x) for x in input().split()]
colors = [0 for _ in range(n)]

for p in paint:
    c = 1
    if n == 1:
        colors[0] = 1
    elif p == 1:
        while c == colors[p]:
            c += 1
        colors[p-1] = c
    elif p == n:
        while c == colors[p-2]:
            c += 1
        colors[p-1] = c
    else:
        while c == colors[p] or c == colors[p-2]:
            c += 1
        colors[p-1] = c

print(*colors)