while(True):
    n=int(input())
    x=''
    if(n==0):
        break
    for i in range(1,n+1):
        x += str(i) + " "
    print(x[:-1])

