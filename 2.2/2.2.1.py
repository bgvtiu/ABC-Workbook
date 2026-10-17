n, letter = input().split()
words = input().split()

L = [words[i] for i in range(int(n)) if words[i][0] == letter]
print(len(L))