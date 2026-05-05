def f(x,A):
    return (x&A!=0)<=((x&17==0 and x&5==0)<=(x&3!=0))
print(max([A for A in range(1,5000) if all(f(x,A)==1 for x in range(1,5000))]))