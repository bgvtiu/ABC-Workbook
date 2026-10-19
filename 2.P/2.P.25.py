n = int(input())

a = 0
b = 0
for _ in range(n):
    name, verb, score = input().split()
    if name == "Alice":
        a += int(score)
    if name == "Bob":
        b += int(score)

print(f"Alice: {a}")
print(f"Bob: {b}")

if a > b:
    print("Alice wins")
elif b > a:
    print("Bob wins")
else:
    print("Draw")