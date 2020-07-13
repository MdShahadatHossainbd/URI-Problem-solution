a = input().split()
b1 = int(a[1])
c1,c2,c3 = map(int,input().split(" : "))
d = input().split()
d1 = int(d[1])
e1,e2,e3 = map(int,input().split(" : "))

day = d1-b1

hour = e1-c1
if(hour<0):
    hour += 24
    day -= 1

minu = e2-c2
if(minu<0):
    minu += 60
    hour -= 1

second = e3-c3
if(second<0):
    second += 60
    minu -= 1

if(day<=0):
    day=0

print("%d dia(s)" %day)
print("%d hora(s)" %hour)
print("%d minuto(s)" %minu)
print("%d segundo(s)" %second)