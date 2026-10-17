n = int(input())
flowers = [int(x) for x in input().split()]
r, k = [int(x) for x in input().split()]

for i in range(0, r-1):
    flowers[i] = k
print(*flowers)