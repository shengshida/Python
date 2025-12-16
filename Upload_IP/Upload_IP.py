#coding utf-8 
#python3 

import requests
import json
import subprocess
import re

IPv4_address = "None"
IPv6_address = "None"
result = subprocess.run(['cmd', '/c', 'netsh interface ipv4 show ipaddress interface="WLAN"'], capture_output=True, text=True)
Object_match = re.match(r'\n地址 (.+) .+',result.stdout,re.I)
if Object_match != None:
    IPv4_address = Object_match[1]
result = subprocess.run(['cmd', '/c', 'netsh interface ipv6 show addresses interface="WLAN"'], capture_output=True, text=True)
Object_match= re.match(r'\n地址 (.+)%\d+ .+',result.stdout,re.I)
if Object_match != None:
    IPv6_address = Object_match[1]

WX_url = "XXXX"
DD_url = "XXXX"
header = {'Content-Type':'application/json'}
data = {
    "msgtype" : "markdown" ,
    'markdown' : {
        "title" : "Upload_IP",
        "text" : "#### IPv4_address:\n#### " + IPv4_address + "\n\n#### IPv6_address:\n#### " + IPv6_address,
        "content" : " IPv4_address:\n " + IPv4_address + "\n\n IPv6_address:\n " + IPv6_address
    }
}
json_data = json.dumps(data)
request=requests.post(url=DD_url,data=json_data,headers=header)
print(request.text)
request=requests.post(url=WX_url,data=json_data,headers=header)
print(request.text)