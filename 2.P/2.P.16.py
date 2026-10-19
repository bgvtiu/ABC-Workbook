n = int(input())
bit = input()
l, r = [int(x) for x in input().split()]

newbit = []
for i in range(n):
    if i < l or i > r:
        if bit[i] == "0":
            newbit.append("1")
        else:
            newbit.append("0")
    else:
        newbit.append(bit[i])

print("".join(newbit))