X,Y = list(map(int,input().split()))
cont = 1
for i in range(1,(int((Y/X))+1)):
    r = ""
    for y in range(X):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])