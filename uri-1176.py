list=[0,1]
a=0
t=1

for i in range(60):
    tmp = t+a
    list.append(tmp)
    a=t
    t=tmp

n = int(input())
for i in range(n):
    v = int(input())
    print('Fib(%d) = %d' %(v,list[v]))