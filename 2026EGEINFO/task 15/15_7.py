def f(x,y,a):
    return (x**2<=136) or (y<(4*x+a-70)) or ((2*y)>51)

print(min([A for A in range(0,300) if all(f(x,y,A)==1 for x in range(0,300) for y in range(0,300))]))