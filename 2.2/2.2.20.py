exp = input()
result = int(exp[0])

for i in range(2, len(exp), 2):
  if exp[i-1] == "+":
    result += int(exp[i])
  if exp[i-1] == "-":
    result -= int(exp[i])

print(result)