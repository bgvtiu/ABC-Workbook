def mix(x, y):
  if (x == "A" and y == "B") or (x == "B" and y == "A") or (x == "C" and y == "C"):
    return "A"
  if (x == "A" and y == "C") or (x == "B" and y == "B") or (x == "C" and y == "A"):
    return "B"
  if (x == "A" and y == "A") or (x == "B" and y == "C") or (x == "C" and y == "B"):
    return "C"

n = int(input())
chemicals = input().split()
result = chemicals[0]

for i in range(1, n):
  result = mix(result, chemicals[i])

print(result)