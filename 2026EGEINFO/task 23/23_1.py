def f(x,end):
    if x>end or x==90: return 0
    if x==end :return 1
    return f(x+1,end)+f(x*2,end)+f(x*3,end)
print('temp')
print(f(3,30)*f(30,100)*f(100,184))
