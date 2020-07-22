import math
while True:
    try:
        n = input().split()
    except EOFError:
        break
    print(math.factorial(int(n[0])) + math.factorial(int(n[1])))