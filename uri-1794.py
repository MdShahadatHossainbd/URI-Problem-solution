N = int(input())
LA, LB = map(int, input().split())
SA, SB = map(int, input().split())
if N in range(LA, LB + 1) and N in range(SA, SB + 1):
    print("possivel")
else:
    print("impossivel")