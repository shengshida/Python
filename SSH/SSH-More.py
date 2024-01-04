import paramiko
import time
import re

output = ""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = "10.255.255.100",port = 22,username = "admin",password = "Admin@123",timeout=10)
time.sleep(0.2)
cli = ssh.invoke_shell()
time.sleep(0.2)
cli.send("sho run\n")
time.sleep(5)

while True :
    cli_match = cli.recv(65535).decode(encoding='UTF-8',errors='strict')
    output += cli_match
    if cli_match.find("More") != -1 :
        cli.send(" ")
        print("发现More,发送空格")
        time.sleep(1)
        continue
    if len(cli_match) < 65535 :
        break
    print("取出中")
    time.sleep(0.2)

with open("out_txt.txt","a",encoding="UTF-8") as file : 
#    file.write(re.sub(r".*More.*","",output.replace('\r','')))
    file.write(output.replace('\r',''))
time.sleep(1)
ssh.close()
print("脚本结束")
input()