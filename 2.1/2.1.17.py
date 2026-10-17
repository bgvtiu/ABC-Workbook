n = int(input())
flowers = [int(x) for x in input().split()]
l, r = [int(x) for x in input().split()]
growth = [int(x) for x in input().split()]

for i in range(l-1, r):
    flowers[i] += growth[i-l+1]
print(*flowers)