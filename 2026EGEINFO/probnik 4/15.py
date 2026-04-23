def f(x,a):
    return (((x&17!=0)<=((x&a!=0)<=(x&58!=0))) <= ((x&8==0) and (x&a!=0) and (x&58==0)))
print('temp')
print(min([a for a in range(1,1000) if all(f(x,a)==0 for x in range(1,10000000))]))