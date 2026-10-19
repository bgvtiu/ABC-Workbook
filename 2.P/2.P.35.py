n = int(input())
k = 0

while n % 2**k != 0 or n/2**k % 2 == 0:  
    k += 1

print(f"2**{k} x {n/2**k:.0f}")