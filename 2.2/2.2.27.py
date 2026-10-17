n = int(input())
dist = [int(x) for x in input().split()]
s_lvls = [int(x) for x in input().split()]

dist.sort(), s_lvls.sort()

success = True
for i in range(n):
    if dist[i] > s_lvls[i]:
        success = False
        break

if success: print("YES")
else: print("NO")