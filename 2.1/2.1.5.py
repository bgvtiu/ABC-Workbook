q = int(input())
nums = [int(input()) for _ in range(q)]

for x in nums:
    if x % 2 == 0:
        print('EVEN')
    else:
        print('ODD')