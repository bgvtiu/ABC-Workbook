n = int(input())
temps = [int(x) for x in input().split()]
l, r = [int(x) for x in input().split()]

for i in range(l-1, r):
    if temps[i] > 50:
        print(i+1)
        break
    elif i == r-1:
        print("no reaction")