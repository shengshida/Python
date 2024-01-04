#python3
#coding utf-8 

import re

while(True):

    print("输入IP与掩码：\n例:10.0.0.1/32")
    address=input()
    obj=re.match(r'(\d*\.\d*\.\d*\.)(\d*)\/(\d*)',address,re.I)
    ip_part_1=obj[1]
    ip_part_2=obj[2]
    mask=obj[3]
    ipv6_prefix="2409:807E:5803:0021:"
    print("网段所有 IPv4地址如下：")
    for x in range(2**(32-int(mask))) :
        ip_count = 0
        ipv4=ip_part_1 + str(((int(ip_part_2)//(2**(32-int(mask))))*(2**(32-int(mask)))+x))+"/"+mask
        with open("AnyIP.txt","r",encoding="UTF-8") as file : 
            for line in file : 
                match_ip=re.match(r'(\d*\.\d*\.\d*\.\d*\/\d*)',line,re.I)
                if match_ip != None : 
                    if match_ip[1]==ipv4 :
                        ip_count = ip_count+1
        print(ipv4+","+str(ip_count))

    print("网段所有 IPv6地址如下：")
    for x in range(2**(32-int(mask))) :
        ipv6=re.sub(r'0x','',re.sub(r'\.',':',ipv6_prefix+ip_part_1 + str(hex(int("0x"+str((int(ip_part_2)//(2**(32-int(mask))))*(2**(32-int(mask)))),16)+x))+"/"+mask))
        print(ipv6)
