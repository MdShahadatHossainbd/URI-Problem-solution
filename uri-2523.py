while True:
    try:
        bulbs = input()
        n = int(input())
        data = input().split()
    except EOFError:
        break
    word = ""
    for i in data:
        word += bulbs[int(i) - 1]
    print(word)