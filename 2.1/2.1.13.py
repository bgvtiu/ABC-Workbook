n = int(input())
flowers = [int(x) for x in input().split()]
L = []

for i in range(n):
    if i == 0:
        if flowers[i] > flowers[i+1]:
            L.append(i+1)
    elif i == n - 1:
        if flowers[i] > flowers[i-1]:
            L.append(i+1)
    else:
        if flowers[i] > flowers[i-1] and flowers[i] > flowers[i+1]:
            L.append(i+1)

if len(L) < 1:
    print('none')
else: print(*L)