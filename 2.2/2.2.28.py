n, r = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

b1 = []
b2 = []
A = 0

for i in range(r):
    #evaluate the function at x = i, i+1
    b1 = [abs(i-num) for num in L]
    b2 = [abs((i+1)-num) for num in L]

    #formula for area of a trapezoid, h = 1
    A += (min(b1) + min(b2)) / 2  

print(f"{A:.0f}")