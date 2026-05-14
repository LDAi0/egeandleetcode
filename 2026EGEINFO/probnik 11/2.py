def f(a,b,c,d):
    return ((a and b)==(not c)) and (b <= d)
print('temp','c a d b')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if f(a,b,c,d)==1:
                    print(c,a,d,b)
