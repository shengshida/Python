import paramiko
import time
output = ""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = "10.0.0.1",port = 22,username = "wangguan_1",password = "Admin@123",timeout=10)
time.sleep(0.2)
cli = ssh.invoke_shell()
time.sleep(0.2)
cli.send("terminal length 0\n")
time.sleep(0.2)
cli.send("show configuration\n")
time.sleep(5)

while True :
    cli_match = cli.recv(65535).decode()
    output += cli_match
    if len(cli_match) < 65535 :
        break
    #print("取出中")
    time.sleep(0.2)

with open("out_txt.txt","a",encoding="UTF-8") as file : 
    file.write(cli_match.replace('\r',''))

time.sleep(1)
ssh.close()
print("脚本结束")
input()