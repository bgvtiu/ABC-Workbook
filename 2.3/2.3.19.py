s, t = [int(x) for x in input().split()]

histo = []
good = True
while s < t:
    s = s**2 - 3
    histo.append(s)

    if len(histo) >= 3 and histo[-1] == histo[-3]:
        print("MOVE ON")
        good = False
        break

if good: print(len(histo))