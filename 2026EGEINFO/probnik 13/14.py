from string import printable
res=[]
for x in printable[:17]:
    x1=int(f'7ac{x}53d',17)
    x2=int(f'83bg94{x}d',17)
    x3=int(f'c5{x}d',17)
    x4=int(f'c4bbf{x}4',17)
    x5=int(f'7{x}79',17)
    h=x1+x2+x3+x4+x5
    if h%16==0:
        res.append([x,h/16])
print(max(res\
    ))
