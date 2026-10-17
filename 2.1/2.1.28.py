n = int(input())
bitstring = input()
shortened = []

for i in range(n-1):
    if bitstring[i] != bitstring[i+1]:
        shortened.append(bitstring[i])
shortened.append(bitstring[-1])
    
print("".join(shortened))