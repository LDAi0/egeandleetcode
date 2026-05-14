from ipaddress import ip_network
cnt=0
net=ip_network('123.222.111.192/255.255.255.248',0)
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip[24:].count('1')%3!=0:
        cnt+=1
print('temp',cnt)