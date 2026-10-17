n = int(input())
seq = input().split()
sentence = ""

for word in seq:
    sentence = f"{sentence}::{word}"

print(sentence[2:])