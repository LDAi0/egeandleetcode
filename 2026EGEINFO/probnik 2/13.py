from ipaddress import ip_network
net= ip_network('101.157.240.0/255.255.252.0',0)
cnt=0
print('temp')
for ip in net:
    if f'{ip:b}'[:16].count('1')> f'{ip:b}'[16:].count('1'):
        cnt+=1
print(cnt)
    
