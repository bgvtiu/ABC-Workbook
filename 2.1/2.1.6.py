q = int(input())
sentences = [input().split() for _ in range(q)]

for s in sentences:
    if (int(s[2]) % 2 == 0 and s[4] == 'even.') or (int(s[2]) % 2 != 0 and s[4] == 'odd.'):
        print('CORRECT')
    else:
        print('INCORRECT')