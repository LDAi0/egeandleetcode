from ipaddress import ip_network
net=ip_network('95.24.20.25/255.255.252.0',0)
cnt=0
for ip in net:
    cnt+=1
print('',cnt-10)