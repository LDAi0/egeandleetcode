import re
print('temp')
for x in range(1923,10**8+1,1923):
    if re.fullmatch(r'1\d*2\d\d76',str(x)) is not None:
        print(x,x//1923)