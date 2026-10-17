n = int(input())
L = [int(x) for x in input().split()]

evens = []
for i in range(n):
    if L[i] % 2 == 0:
        evens.append(i)

if not evens:
    print("no even numbers")
else:
    print(max(evens))