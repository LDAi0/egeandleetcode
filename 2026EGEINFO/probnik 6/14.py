from string import printable
print('temp')
for x in printable[:17]:
    h1=int(f'7ac{x}53d',17)
    h2=int(f'83bg94{x}d',17)
    h3=int(f'c5{x}d',17)
    h4=int(f'c4bbf{x}4',17)
    h5=int(f'7{x}79',17)
    if (h1+h2+h3+h5+h4)%16==0:
        print(x)
        print((h1+h2+h3+h5+h4)/16)

    