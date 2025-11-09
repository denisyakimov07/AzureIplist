import ipaddress
import json

with open('ServiceTags_Public_20251028.json', "r") as file:
    data = json.load(file)


def is_ipv4_subnet(sub_to_check):
    try:
        # Only IPv4 networks (no IPv6)
        ipaddress.IPv4Network(sub_to_check, strict=False)
        return True
    except ValueError:
        return False



def if_ip_in_subnet(ip_str, subnet_str):
    ip = ipaddress.IPv4Address(ip_str)
    network = ipaddress.IPv4Network(subnet_str, strict=False)
    return ip in network

for i in data["values"]:
    for ip in i["properties"]["addressPrefixes"]:
        print(is_ipv4_subnet(ip))
    # print(i["name"])
    # print(i["properties"]["addressPrefixes"])




