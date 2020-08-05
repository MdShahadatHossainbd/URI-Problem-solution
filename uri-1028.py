def mdc(a,b):
  if a % b == 0:
    return b
  else:
    return mdc(b,a % b)

test_cases = int(input())
for c in range(test_cases):
  a = input().split(" ")
  num1 = int(a[0])
  num2 = int(a[1])
  print(mdc(num1,num2))