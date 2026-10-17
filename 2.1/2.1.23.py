n = int(input())
cards = [input().split() for _ in range(n)]

def print_suit(suit):
    for c in cards:
        if c[2] == suit:
            print(" ".join(c))

print_suit('Clubs')
print_suit('Diamonds')
print_suit('Hearts')
print_suit('Spades')