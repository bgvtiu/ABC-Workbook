#functions bc i didn't want *that* many nested layers
def avg():
    l, r = [int(x) for x in input().split()]
    return sum(flowers[l-1:r]) / len(flowers[l-1:r])

def counting():
    l, r, k = [int(x) for x in input().split()]
    counter = 0
    for i in range(l-1, r):
        if flowers[i] <= k:
            counter += 1
    return counter

def increase():
    l, r, k = [int(x) for x in input().split()]
    for i in range(l-1, r):
        flowers[i] += k

def sorting():
    sign = input()
    if sign == "+":
        flowers.sort()
    else: 
        flowers.sort(), flowers.reverse()

n = int(input())
flowers = [int(x) for x in input().split()]
q = int(input())

for _ in range(q):
    line = input()

    if line == "AVERAGE":
        print(f"{avg():.2f}")
    elif line == "COUNT":
        print(f"{counting()}")
    elif line == "INCREASE":
        increase()
    elif line == "SORT":
        sorting()