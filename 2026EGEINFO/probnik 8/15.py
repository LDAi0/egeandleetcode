def f(x,y,a):
    return ((x>68) or (y>89)) or (((2*x)-(7*y))<a)
print('temp')
print(min([a for a in range(-1000,138) if all(f(x,y,a)==1 for x in range(0,500) for y in range(0,500)) ]))