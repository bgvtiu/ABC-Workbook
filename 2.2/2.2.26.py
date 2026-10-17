n = int(input())
dominoes = [input().split() for _ in range(n)]

chain = True
for i in range(1, n):
    if dominoes[i][0] in dominoes[i-1] and dominoes[i][-1] in dominoes[i-1]:
        continue
    elif dominoes[i][0] in dominoes[i-1]:
        dominoes[i].remove(dominoes[i][0])
    elif dominoes[i][-1] in dominoes[i-1]:
        dominoes[i].remove(dominoes[i][-1])
    else: 
        chain = False
        break

if chain: print("YES")
else: print("NO")