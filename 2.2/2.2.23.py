n = int(input())
L = [int(x) for x in input().split()]

distincts = []
for i in range(n):
  if L[i] not in distincts:
    distincts.append(L[i])

print(len(distincts))