from ipaddress import ip_network
net = ip_network('172.16.192.0/255.255.192.0',strict=False)
cnt=0
for ip in net:
    ip_bin=bin(int(ip))[2:].zfill(32)
    if ip_bin.count('1')%5!=0:
        cnt+=1
print(cnt)