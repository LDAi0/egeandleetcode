res=[]
for n in range(1,1000000):
    n1=bin(n)[2:]
    if n1.count('1')%3==0:
        n1=bin(n1.count('1')%5)[2:]+n1
    else:
        n1='10'+n1+'1'
    if int(n1,2)>89: res.append(int(n1,2))
print('temp', min(res))