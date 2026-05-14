from string import printable

for x in printable[:14]:
    x1=int(f'4b3{x}1c7',14)
    x2=int(f'5{x}g83f7',17)
    if (x1+x2)%15==0:
        print('temp',(x1+x2)/15)
        break