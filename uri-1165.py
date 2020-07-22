n=int(input())
for i in range(n):
    a=int(input())
    x=0
    for j in range(1,a+1):
        if(a%j==0):
            x=x+1
    if(x==2):
        print("{} eh primo".format(a))
    else:
        print("{} nao eh primo".format(a))