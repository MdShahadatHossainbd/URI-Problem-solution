N = int(input())

for i in range (N):
    count = 0
    x,y = map(int,input().split())
    if(x >= y):
        if(y % 2 == 0):
          for j in range(y, x):
            if(j % 2 != 0):
              count += j
        else:
          for j in range(y + 1, x):
            if(j % 2 != 0):
              count += j
    else:
        if(x % 2 == 0):
          for j in range(x, y):
            if(j % 2 != 0):
              count += j
        else:
          for j in range(x + 1, y):
            if(j % 2 != 0):
              count += j
    print(count)