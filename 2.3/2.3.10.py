p, x = [int(x) for x in input().split()]
days = 0

while p < x:
    p += int(0.01*p)
    days += 1

print(days)