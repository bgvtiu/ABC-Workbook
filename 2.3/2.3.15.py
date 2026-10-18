v, t = [int(x) for x in input().split()]
counter = 0

x = 215
for i in range(1, t+1):
    prev_x = x
    x = (512*prev_x + 227) % 2027

while x != v:
    prev_x = x
    x = (512*prev_x + 227) % 2027
    counter += 1

print(counter)