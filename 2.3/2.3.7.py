n = int(input())
flowers = [int(x) for x in input().split()]
q = int(input())

for _ in range(q):
    l, r = [int(x) for x in input().split()]

    for i in range(l-1, r):
        flowers[i] += 1
   
print(*flowers)