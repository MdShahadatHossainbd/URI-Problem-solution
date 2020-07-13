T = float(input())

if T > 0.00 and T < 2000.00:
    print('Isento')
elif T>=2000.01 and T<=3000.00:
    x= T-2000
    tex = x*0.08
    print("R$ %.2f" %tex)
elif T>=3000.01 and T<=4500.00:
    x= T-3000
    #tex = ((x*18)/100)+(1000*0.08)
    tex =( x*0.18)+(1000*0.08)
    print("R$ %.2f" %tex)
else:
    x= T-4500
    tex =(x*0.28)+(1500*0.18)+(1000*0.08)
    print("R$ %.2f" %tex)