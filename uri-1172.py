'''

for i in range(10):
    n=int(input())
    if(n< 1):
        n = 1
    print("X[%d] = %d" % (i, n))

'''


for i in range(10):
    n = int(input())
    if n <= 0:
        print("X[{}] = 1".format(i))
    else:
        print("X[{}] = {}".format(i, n))