def faro(s):
    top = s[:int(n/2)]
    bottom = s[int(n/2):]

    shuffle = []
    for i in range(int(n/2)):
        shuffle.append(top[i])
        shuffle.append(bottom[i])
    return shuffle

n = int(input())
orig = list(range(n))

shuffle = faro(orig)
counter = 1
while shuffle != orig:
    shuffle = faro(shuffle)
    counter += 1

print(counter)