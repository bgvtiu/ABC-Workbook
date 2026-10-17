n = int(input())
seq = [int(x) for x in input().split()]

constant = True
nondecreasing = True
nonincreasing = True

for i in range(1, n):
    if seq[i] < seq[i-1]:
        nondecreasing = False
        break

for i in range(1, n): 
    if seq[i] > seq[i-1]:
        nonincreasing = False
        break

for i in range(1, n):
    if seq[i] != seq[i-1]:
        constant = False
        break

if constant: print("constant")
elif nondecreasing: print("nondecreasing")
elif nonincreasing: print("nonincreasing")
else: print("not sorted")