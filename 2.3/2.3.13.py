dir = input()
coords = [0, 0]

for i in range(len(dir)):
    if dir[i] == "U":
        coords[1] += 1
    if dir[i] == "D":
        coords[1] -= 1
    if dir[i] == "L":
        coords[0] -= 1
    if dir[i] == "R":
        coords[0] += 1

    print(*coords)