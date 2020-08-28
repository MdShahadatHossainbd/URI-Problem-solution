while True:
    try:
        n = input()
    except EOFError:
        break
    if len(n) not in range(6, 33):
        print("Senha invalida.")
    else:
        capital_letter = 0
        small_letter = 0
        numeral = 0
        for i in n:
            if i.isupper():
                capital_letter += 1
            elif i.islower():
                small_letter += 1
            elif i.isdecimal():
                numeral += 1
            else:
                print("Senha invalida.")
                break
        else:
            if small_letter == 0 or capital_letter == 0 or numeral == 0:
                print("Senha invalida.")
            else:
                print("Senha valida.")