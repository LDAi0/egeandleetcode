from string import printable
for x in printable[:29]:
    x1=int(f'463{x}7921',29)
    x2=int(f'8241{x}153',29)
    if (x1+x2)%28==0:
        print(x)
        print('temp',(x1+x2)/28)
        break