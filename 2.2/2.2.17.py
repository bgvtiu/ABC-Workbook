s = input()
a = s.index('a')
b = s.index('b')

start = min(a, b) + 1 #the plus one just helps w indexing
end = max(a, b)

print(f"{s[:start]}{'*'*(end - start)}{s[end:]}")