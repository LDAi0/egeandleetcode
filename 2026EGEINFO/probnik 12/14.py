mx=0
for x in range(1,7291):
    t=0
    x1=27**298+27**269-x
    while x1>0:
        if x1%27==0:
            t+=1
        x1//=27
    mx=max(mx,t)
print(mx)
