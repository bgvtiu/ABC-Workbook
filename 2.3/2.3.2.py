word = input()
n = int(input())

word = list(word)
for _ in range(n):
    k, x = input().split()
    word[int(k)-1] = x

print("".join(word))