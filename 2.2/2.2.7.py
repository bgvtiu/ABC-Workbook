n = int(input())
words = input().split()

good = True
for i in range(n):
    if words[i][0] != words[0][0]:
        good = False
        print("Invalid")
        break

if good: print(words[0][0])