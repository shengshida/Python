import telnetlib
import re
import time

HOST = '10.255.255.100'
user = 'admin'
password = 'Admin@123'

tn = telnetlib.Telnet(HOST)
# tn.set_debuglevel(2) #开启调试模式

tn.expect([re.compile(b"Username:"),]) #用正则匹配Username
tn.write("admin" + "\n")  #匹配成功，输入user
#tn.write(str(huawei) + "\n")  #匹配成功，输入user
tn.expect([re.compile(b"Password:"),]) #同上
tn.write("Admin@123" + "\n") #同上