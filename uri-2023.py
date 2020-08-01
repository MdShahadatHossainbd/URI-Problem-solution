name = []
while True:
    try:
        names = input()
    except EOFError:
        break
    name.append(names)
    Alphabet = [i.lower() for i in name]
    update = Alphabet.index(max(Alphabet))
print(name[update])

