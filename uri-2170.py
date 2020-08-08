project = 0
while True:
    try:
        Initial, final = map(float, input().split())
    except EOFError:
        break
    project += 1
    total = (final - Initial) / Initial * 100
    print("Projeto {}:".format(project))
    print("Percentual dos juros da aplicacao:", format(total, ".2f"), "%\n")