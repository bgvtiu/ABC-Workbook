n = int(input())
flowers = [int(x) for x in input().split()]
L = []

for i in range(n):
    if flowers[i] == max(flowers):
        L.append(i+1)
print(*L)