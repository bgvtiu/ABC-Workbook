n, s, k = [int(x) for x in input().split()]
whs = [int(x) for x in input().split()]

pos = s
for _ in range(k):
    pos = whs[pos-1]

print(f"Location: {pos}")