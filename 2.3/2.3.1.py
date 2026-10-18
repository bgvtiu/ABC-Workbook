start = input().split()
tasks = int(start[-1])
n = int(input())

for _ in range(n):
    words = input().split()

    if words[0] == "FINISH":
        tasks -= int(words[-1])
    else:
        tasks += int(words[-1])

print(tasks)