n = int(input())
flowers = [int(x) for x in input().split()]
q = int(input())

for _ in range(q):
    l, r = [int(x) for x in input().split()]
    print(max(flowers[l-1:r]))