n = int(input())
scores = [int(x) for x in input().split()]

avg = sum(scores) / n

higher = 0
lower = 0
for s in scores:
    if s > avg:
        higher += 1
    elif s < avg:
        lower += 1

print(f"{lower} scored below average")
print(f"{higher} scored above average")