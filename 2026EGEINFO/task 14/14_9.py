x=5**2*7**25+6**2*7**36-4**2*9**3
cnt=0
x=abs(x)
while x>0:
    if x%7==0:
        cnt+=1
    x//=7
print('temp',cnt)
