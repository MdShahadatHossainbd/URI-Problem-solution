x=0
y=0
z=0
while(True):
    n=int(input())
    if(n == 4):
        break
    else:
        if (n == 1):
            x +=1
        elif (n == 2):
            y+=1
        elif (n == 3):
            z+=1
        else:
            continue
print("MUITO OBRIGADO")
print("Alcool:",x)
print("Gasolina:",y)
print("Diesel:",z)