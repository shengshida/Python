#coding utf-8 
#python3 

import requests
import json
import subprocess
import re

IPv4_address = "None"
IPv6_address = "None"
result = subprocess.run(['cmd', '/c', 'netsh interface ipv4 show ipaddress interface="WLAN"'], capture_output=True, text=True, encoding='utf-8')
Object_match = re.findall(r'\d+\.\d+\.\d+\.\d+',result.stdout,re.I)
if len(Object_match) != 0:
    IPv4_address = Object_match[0]
result = subprocess.run(['cmd', '/c', 'netsh interface ipv6 show addresses interface="WLAN"'], capture_output=True, text=True, encoding='utf-8')
Object_match= re.findall(r'\S+:\S+:\S+:\S+:\S+:\S+:\S+:\S+',result.stdout,re.I)
if len(Object_match) != 0:
    IPv6_address = '\n'.join(Object_match)

WX_url = "XXXX"
DD_url = "XXXX"
header = {'Content-Type':'application/json'}
data = {
    "msgtype" : "markdown" ,
    'markdown' : {
        "title" : "Upload_IP",
        "text" : "#### IPv4_address:\n#### " + IPv4_address + "\n\n#### IPv6_address:\n#### " + IPv6_address.replace("\n", "\n#### "),
        "content" : "IPv4_address:\n" + IPv4_address + "\n\nIPv6_address:\n" + IPv6_address
    }
}
json_data = json.dumps(data)
request=requests.post(url=DD_url,data=json_data,headers=header)
print(request.text)
request=requests.post(url=WX_url,data=json_data,headers=header)
print(request.text)