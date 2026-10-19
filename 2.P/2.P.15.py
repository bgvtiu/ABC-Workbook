n = int(input())
bit = input()
l, r = [int(x) for x in input().split()]

newbit = []
for i in range(l, r+1):
    if bit[i] == "0":
        newbit.append("1")
    else:
        newbit.append("0")

print(f"{bit[:l]}{"".join(newbit)}{bit[r+1:]}")