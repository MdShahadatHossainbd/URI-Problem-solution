list=[]
n=float(input())
for i in range(100):
    list.append(n)
    print("N[%d] = %0.4f" % (i, n))
    n=n/2