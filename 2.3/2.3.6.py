n = int(input())
flowers = [int(x) for x in input().split()]
q = int(input())

for _ in range(q):
    l, r = [int(x) for x in input().split()]
    subr = [flowers[i] for i in range(l-1, r)]
    subr.sort()

    middle_i = int((len(subr)//2))

    if len(subr) % 2 == 0:
        print(f"{(subr[middle_i] + subr[middle_i - 1]) / 2:.2f}")
    else:
        print(f"{subr[middle_i]:.2f}")