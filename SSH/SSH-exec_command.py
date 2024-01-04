import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = "10.0.0.1",port = 22,username = "admin",password = "Admin@123",timeout=10)
stdin,stdout,stderr = ssh.exec_command("show  configuration \n")
time.sleep(1)
print(stdout.read().decode())
ssh.close()
print("脚本结束")
input()