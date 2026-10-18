n, m = [int(x) for x in input().split()]
bids = [0 for _ in range(n)]
names = ["" for _ in range(n)]

for _ in range(m):
    s, v, i = input().split()
    v = int(v)
    i = int(i)

    if v > bids[i-1]:
        bids[i-1] = v
        names[i-1] = s

for x in range(n):
    if names[x] == "":
        print("UNSOLD")
    else:
        print(names[x])