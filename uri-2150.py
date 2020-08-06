while True:

    letters = input()
    if letters == "":
        break
    word = input()
    count = 0

    for i in word:
        if i in letters:
            count += 1

    print(count)