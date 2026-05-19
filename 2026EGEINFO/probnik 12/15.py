res=[]
for x in range(1,200):
    P = x in {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30}
    Q = x in {1,4,7,10,13,16,19,22,25,28,31}
    A = 1
    if ((A<=P) and (Q<=(not A)))==1:
        res.append(x)
print(len(res))