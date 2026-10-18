x = int(input())
fibo = [1, 1]

while fibo[-1] < x:
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[-1])