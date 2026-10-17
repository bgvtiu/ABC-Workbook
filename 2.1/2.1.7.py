q = int(input())
plates = [int(x) for x in input().split()]

odds = []
evens = []

for x in plates:
    if x % 2 == 0: evens.append(x)
    else: odds.append(x)

print(*sorted(odds))
print(*sorted(evens))