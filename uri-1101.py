while(True):
  List = []
  a, b = map(int, input().split())
  if(a <= 0) or (b <= 0):
    break
  else:
    if(a > b):
      a, b = b, a
    for i in range(a, b + 1):
      List.append(i)
    Sum = 'Sum=%d' %sum(List)
    List.append(Sum)
    print(' '.join(map(str, List)))