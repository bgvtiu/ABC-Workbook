n = int(input())
s = "a"

while len(s) < n:
    result = []
    for i in range(len(s)):
        if s[i] == "a":
            result.append("ab")
        else:
            result.append("a")
    s = "".join(result)

print(s[:n])