from ipaddress import ip_network
net=ip_network('192.168.31.80/255.255.255.240',0)
mx=0
for ip in net:
    x=bin(int(ip))[2:].zfill(32)
    if x.count('1')>mx:
        mx=x.count('1')
print('temp',mx)