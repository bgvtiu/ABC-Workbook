n = int(input())
flowers = [int(x) for x in input().split()]
L = []

for i in range(n):
    if i == 0:
        if flowers[i] > flowers[i+1]:
            x = flowers[i] - 2
        else: x = flowers[i]
    elif i == n - 1:
        if flowers[i] > flowers[i-1]:
            x = flowers[i] - 2
        else: x = flowers[i]
    else:
        if flowers[i] > flowers[i-1] and flowers[i] > flowers[i+1]:
            x = flowers[i]-2
        else: x = flowers[i]
    L.append(x)

print(*L)