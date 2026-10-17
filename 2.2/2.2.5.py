n = int(input())
cards = []

for _ in range(n):
    words = input().split()
    value = words[0]
    cards.append(value)

counter = 0
for i in range(n):
    if cards[i] == cards[0]:
        counter += 1
print(counter)