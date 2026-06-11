cnt=0
for x in range(1,1000):
    S = x in {3,6,9,12}
    Q = x in {1,2,3,4,5,6}
    A=0
    if (not(not A and S) or not Q)==0:
        cnt+=1
print(cnt)