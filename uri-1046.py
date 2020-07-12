i,A=map(int, input().split())
if i>A:
    B=24-i
    x=B+A
    print("O JOGO DUROU %d HORA(S)" %x)
elif A>i:
    x=A-i
    print("O JOGO DUROU %d HORA(S)" %x)
elif i==A:
    x=24
    print("O JOGO DUROU %d HORA(S)" %x)