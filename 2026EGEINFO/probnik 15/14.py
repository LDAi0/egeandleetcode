for x in range(1,3001):
    cnt=0
    x1=9**150+9**30-x
    while x1>0:
        if x1%9==0:
            cnt+=1
        x1//=9
    if cnt==122:
        print('temp',x)
        break

