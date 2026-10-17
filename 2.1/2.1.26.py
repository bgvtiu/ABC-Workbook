n = int(input())
prices = [int(x) for x in input().split()]
changes = []

for i in range(1, n):
    if prices[i] - prices[i-1] > 0:
        changes.append(f"+{prices[i] - prices[i-1]}")
    else: changes.append(prices[i] - prices[i-1])
print(*changes)