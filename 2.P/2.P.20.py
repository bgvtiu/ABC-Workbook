def check(name):
    possible = True
    if len(s) != len(name):
        possible = False
    else:
        for i in range(len(s)):
            if s[i] == '.': 
                continue
            elif s[i] == name[i]: 
                continue
            else:
                possible = False
                break
    return possible

s = input()
friends = ["Alice", "Bob", "Cindy"]
owner = [check(f) for f in friends]

if owner.count(True) == 1:
    print(friends[owner.index(True)])
elif owner.count(True) > 1:
    print("CAN'T TELL")
else:
    print("SOMETHING'S WRONG")