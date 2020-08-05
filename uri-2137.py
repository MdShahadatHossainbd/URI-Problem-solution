while True:
    try:
        loops = int(input())
    except EOFError:
        break
    lista = []
    for i in range(loops):
        data = input()
        lista.append(data)
    lista_sort = sorted(lista)
    for j in lista_sort:
        print(j)