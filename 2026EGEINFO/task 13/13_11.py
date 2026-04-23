from ipaddress import ip_network
net=ip_network('98.81.154.195/255.252.0.0', strict=False)
print('temp')
for ip in net:
    print(ip)