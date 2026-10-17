n = int(input())
seq = [int(x) for x in input().split()]

min = seq[0]
for i in range(n):
    if seq[i] < min:
        min = seq[i]

print(min)