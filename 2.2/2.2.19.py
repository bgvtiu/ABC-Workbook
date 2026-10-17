n = int(input())
L = [int(x) for(x) in input().split()]

not_zero = []
for num in L:
    if num != 0:
        not_zero.append(num)

print(min(not_zero))