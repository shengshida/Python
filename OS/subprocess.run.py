import subprocess
import re

result = subprocess.run(['cmd', '/c', 'netsh interface ipv4 show ipaddress interface="WLAN"'], capture_output=True, text=True)
IPv4_address = re.match(r'\n地址 (.+) .+',result.stdout,re.I)[1]
result = subprocess.run(['cmd', '/c', 'netsh interface ipv6 show addresses interface="WLAN"'], capture_output=True, text=True)
IPv6_address = re.match(r'\n地址 (.+)%\d+ .+',result.stdout,re.I)[1]

print(IPv4_address, IPv6_address)