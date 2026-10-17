n = int(input())
seq = [int(x) for x in input().split()]

test_d = seq[1] - seq[0]
good = True

for i in range(1, n):
    if seq[i] - seq[i-1] != test_d:
        good = False
        print("NO")
        break

if good:
    print("YES")
    print(f"initial term: {seq[0]}")
    print(f"common difference: {test_d}")