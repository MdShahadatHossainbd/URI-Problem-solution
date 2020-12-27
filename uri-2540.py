while True:
    try:
        N = int(input())
    except EOFError:
        break
    two_thirds = N * 2 / 3
    votes = input().split()
    total = sum(map(int, votes))
    if total >= two_thirds:
        print("impeachment")
    else:
        print("acusacao arquivada")