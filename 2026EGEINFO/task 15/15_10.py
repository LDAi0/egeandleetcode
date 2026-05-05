def f(x,y,a):
    return ((x+2*y)!=58) or (((a-x)>0)==((a+y)>0))

print(min([a for a in range(1,100) if all(f(x,y,a)==1 for x in range(1,500) for y in range(1,500))]))