#не работает!!!
s=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 24\\24_123123.txt').readline()

for c in "0123456789": s=s.replace(c,'0')

t_l=''
ans_index=-1
index=0
ans=0
t=0
is_search=False
i=0

while i < len(s):
    if s[i]=='0' and not is_search:
        continue
    elif s[i]=='0' and  is_search:
        t+=1
    elif s[i]!='0' and not is_search:
        t_l=s[i]
        t+=1
        is_search=True
        index=i
    elif s[i]!='0' and is_search:
        if t_l!=s[i]:
            t_l=''
            t=0
            i-=1
            is_search=False
        else:
            t+=1
            if t>ans:
                ans=t
                ans_index=index
            elif ans==t:
                if ans_index==-1:
                    ans_index=index
                else:
                    ans_index=min(ans_index,index)
            is_search=False
    i+=1
print('temp',ans, ans_index)
    

                