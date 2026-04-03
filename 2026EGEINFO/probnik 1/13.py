from ipaddress import ip_network
net=ip_network('45.172.106.203/255.255.252.0', strict=False)
for ip in net:
    print(ip)