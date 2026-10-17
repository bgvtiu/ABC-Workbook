n = int(input())
prices = [int(x) for x in input().split()]
quantities = [int(x) for x in input().split()]

for i in range(n):
    prices[i] *= quantities[i]

print(sum(prices))