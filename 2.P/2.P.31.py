def many_append(L):
    global shuffled
    for c in L:
        shuffled.append(c)

n = int(input())
c = [input() for _ in range(n)]

t = int(input())
for _ in range(t):
    l, r = [int(x) for x in input().split()]

    shuffled = []
    many_append(c[l-1:r]), many_append(c[:l-1]), many_append(c[r:])
    c = shuffled.copy()

for card in c:
    print(card)