x=27**4-9**5+3**8-25
cnt=0
while x>0:
    if x%3==2: cnt+=1
    x//=3
print('temp', cnt)