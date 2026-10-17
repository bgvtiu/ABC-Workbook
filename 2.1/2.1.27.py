n = int(input())
moves = input()
directions = []

for i in range(n):
    if moves[-(i+1)] == 'N': directions.append('S')
    if moves[-(i+1)] == 'S': directions.append('N')
    if moves[-(i+1)] == 'E': directions.append('W')
    if moves[-(i+1)] == 'W': directions.append('E')
print("".join(directions))