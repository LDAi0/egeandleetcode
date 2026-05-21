def f(n):
    P=set()
    E=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i%2==0:
                E.add(i)
            if n//i%2==0:
                E.add(n//i)
            if p(i):
                P.add(i)
            if p(n//i):
                P.add(n//i)
    if len(P)==len(E):
        return [True,abs(sum(P)-sum(E))]
    else:
        return [False,abs(sum(P)-sum(E))]

def p(n):
    return n>1 and all([n%d!=0 for d in range(2,int(n**0.5)+1)])

for x in range(100_000_000,111_111_111):
    D=f(x)
    if D[0]:
        print(x,D[1])