seq_a = input()
seq_b = input()

complement = []
for base in seq_a:
    if base == 'G':
        complement.append('C')
    elif base == 'C':
        complement.append('G')
    elif base == 'A':
        complement.append('T')
    elif base == 'T':
        complement.append('A')

errors = 0
for i in range(len(seq_b)):
    if seq_b[i] != complement[i]:
        errors += 1

if seq_b == "".join(complement):
    print("YES")
else:
    print("NO")
    print(errors)