def buy(x, y, z):
    global strawbs
    if s[x] == 7 or s[y] == 7 or s[z] == 7:
        strawbs += s[x]

n = int(input())
s = [int(x) for x in input().split()]

strawbs = 0
for i in range(n):
    if i == n-1 or len(s) == 1:
        buy(i, i-1, i-1)
    elif i == 0:
        buy(i, i+1, i+1)
    else:
        buy(i, i+1, i-1)

print(strawbs)