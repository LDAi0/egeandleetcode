def p(x):
    return x>1 and all(x%d!=0 for d in range(2,int(x**0.5)+1))

def f(x):
    D=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            if p(i):
                D.add(i)
            if p(x//i):
                D.add(x//i)
    if len(D)==0:
        return 0
    return min(D)+max(D)

for x in range(1_101_000,2_000_000):
    #if x%10000==0: print(x,2_000_000)
    M=f(x)
    if M>13000 and M%100==26:
        print(x,M)