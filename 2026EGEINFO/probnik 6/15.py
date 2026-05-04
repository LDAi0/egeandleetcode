for a in range(0,1000):
    if all(((x**2<=136) or (y<(4*x+a-70)) or ((2*y)>51))==1 for x in range(0,10000) for y in range(0,10000)):
        print('temp',a)
        break