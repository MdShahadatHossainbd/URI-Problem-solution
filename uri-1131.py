l = 0
k = 0
j = 0
c = 0
d = 0
e = 0
while True:
    x,y = list(map(int,input().split()))
    if(x>y):
        l=l+1
    if(x<y):
        k=k+1
    if(x==y):
        j=j+1
    c+=x
    d+=y
    e=e+1
    print("Novo grenal (1-sim 2-nao)")
    n = int(input())
    if(n==1):
        continue
    if(n==2):
        break
print("{} grenais".format(e))
print("Inter:{}".format(l))
print("Gremio:{}".format(k))
print("Empates:{}".format(j))
if(l>k):
    print("Inter venceu mais")
if(l<k):
    print("Gremio venceu mais")
if(k==l):
        print("Nao houve vencedor")