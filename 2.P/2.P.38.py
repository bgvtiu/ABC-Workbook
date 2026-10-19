def prime(x):
    prime = True
    for y in range(2, x):
        if x % y == 0:
            prime = False
            break
    return prime

n = int(input())
factors = []

while not prime(n):
    for z in range(2, n):
        if n % z == 0 and prime(z):
            factors.append(z)
            n = int(n/z)
if n != 1:
    factors.append(n)

unduped = factors.copy()
unduped.sort()
for f in factors:
    if unduped.count(f) > 1:
        unduped.remove(f)

primes = []
for i in range(len(unduped)):
    pow = factors.count(unduped[i])
    primes.append(f"{unduped[i]}**{pow}")

print(" x ".join(primes))