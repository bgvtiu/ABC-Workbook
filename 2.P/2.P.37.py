n = int(input())

primes = []
for x in range (2, n+1):
    prime = True
    for y in range(2, x):
        if x % y == 0:
            prime = False
            break
    if prime: primes.append(x)

print(*primes)