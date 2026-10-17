n = int(input())
flowers = [int(x) for x in input().split()]
growth = [int(x) for x in input().split()]

for i in range(n):
    flowers[i] += growth[i]
print(*flowers)