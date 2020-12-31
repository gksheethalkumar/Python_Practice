import ipaddress
for ip in ipaddress.IPv4Network('192.168.1.0/24'):
    print(ip)
