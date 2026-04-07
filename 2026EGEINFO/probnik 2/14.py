res=[]
max_zero=0
answer_x=0
for x in range(1,3001):
    cnt=0
    x1=4**210+4**110-x
    while x1>0:
        if x1%4==0:
            cnt+=1
        x1//=4
    if cnt>max_zero:
        max_zero=cnt
        answer_x=x
print('temp',max_zero,answer_x)
