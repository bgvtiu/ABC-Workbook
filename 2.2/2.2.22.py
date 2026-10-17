s = input()
asterisked = ""

for i in range(len(s)):
  if s[i] == ".":
    asterisked += s[i:]
    break
  else:
    asterisked += "*"

print(asterisked)