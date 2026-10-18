n = int(input())
a = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
b = []

for i in range(n):
    node_a = a.index(i+1) + 1
    b.append(c.index(node_a) + 1)

print(*b)