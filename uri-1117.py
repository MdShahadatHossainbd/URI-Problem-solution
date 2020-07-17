A = 0
B = 0
while B < 2:
    gpa = float(input())
    if(gpa >= 0 and gpa <= 10):
        A += gpa
        B += 1
    else:
        print("nota invalida")

print("media = %.2f" %(A/2))