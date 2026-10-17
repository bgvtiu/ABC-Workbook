n = int(input())
colors = []

for _ in range(n):
    words = input().split()
    if words[2] == "Diamonds" or words[2] == "Hearts":
        colors.append("red")
    else: colors.append("black")

counter = 0
for i in range(n):
    if 0 == i: 
        if len(colors) != 1 and colors[i] == colors[i+1]:
            counter += 1
    elif i+1 == n: 
        if len(colors) != 1 and colors[i] == colors[i-1]:
            counter += 1
    else:
        if colors[i] == colors[i+1] and not(colors[i] == colors[i-1]):
            counter += 1
        if colors[i] == colors[i-1] and not(colors[i] == colors[i+1]):
            counter += 1

print(counter)