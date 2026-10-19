n = int(input())
bit = input()
l, r = [int(x) for x in input().split()]

newbit = []
changes = []
for i in range(l, r+1):
    if bit[i] == "0":
        newbit.append("1")
        changes.append(i)
    else: newbit.append(bit[i])

print(f"{bit[:l]}{"".join(newbit)}{bit[r+1:]}")

if not changes:
    print("NO CHANGES")
else: print(*changes)