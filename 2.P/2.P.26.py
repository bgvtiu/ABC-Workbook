n, s = [int(x) for x in input().split()]

log = []
for i in range(n):
    log.append(input().split())

for i in range(n):
    x = log[i][0]
    action = log[i][1]

    if action == "enter":
        s += int(x)
    elif action == "leave":
        s -= int(x)

    if s == 0:
        print(f"hour {i+1} is free")
        break

    if i == n-1:
        print("always occupied")