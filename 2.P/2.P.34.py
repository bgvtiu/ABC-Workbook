n, m = [int(x) for x in input().split()]
present = [0 for _ in range(n)]

for _ in range(m):
    a = int(input())
    c = [int(x) for x in input().split()]

    for i in range(a):
        present[c[i]-1] += 1

g_count = 0
g_noodles = []
sg_count = 0
sg_noodles = []

for i in range(n):
    if present[i] == m:
        sg_count += 1
        sg_noodles.append(i+1)
        g_count += 1
        g_noodles.append(i+1)
    elif present[i] >= m/2:
        g_count += 1
        g_noodles.append(i+1)

print(g_count), print(*g_noodles)
print(sg_count), print(*sg_noodles)