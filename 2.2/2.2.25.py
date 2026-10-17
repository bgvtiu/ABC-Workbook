n, k, x = [int(x) for x in input().split()]
drop_table = [[int(x) for x in input().split()] for _ in range(n)]

mini = 0
maxi = 0

for i in range(n):
    mini += min(drop_table[i])
    maxi += max(drop_table[i])

if mini >= x:
    print("ALWAYS")
elif mini < x <= maxi:
    print("SOMETIMES")
elif maxi < x:
    print("NEVER")