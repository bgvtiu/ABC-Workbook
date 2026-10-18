n = int(input())
seats = input().split()
e = int(input())

for _ in range(e):
    s1, s2 = [int(x) for x in input().split()]
    seats[s1-1], seats[s2-1] = seats[s2-1], seats[s1-1]

print(*seats)