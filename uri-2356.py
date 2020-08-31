while True:
    try:
        seq1 = input()
        seq2 = input()
    except EOFError:
        break
    if seq2 in seq1:
        print("Resistente")
    else:
        print("Nao resistente")