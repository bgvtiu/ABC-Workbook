n = int(input())
bit = input()
op = input()

new = []
for i in range(n):
    if op[i] == '0':
        new.append('0')
    if op[i] == '1':
        new.append('1')
    if op[i] == '.':
        new.append(bit[i])
    if op[i] == 'F':
        if bit[i] == "0":
            new.append("1")
        else:
            new.append("0")

print("".join(new))