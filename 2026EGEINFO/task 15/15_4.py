print('temp')
for x in range(-10000,10000):
    P=x in [3,6,9,12]
    Q= x in [1,2,3,4,5,6]
    A=0
    f_usl=1
    f=((not((not A) and P)) or (not Q))
    if f!=f_usl:
        print(x)