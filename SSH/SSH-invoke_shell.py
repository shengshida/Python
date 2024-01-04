import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = "10.0.0.1",port = 22,username = "admin",password = "Admin@123",timeout=10)
cli = ssh.invoke_shell()
cli.send("terminal length 0\n")
time.sleep(1)
cli.send("dis cur\n")
time.sleep(1)
output = cli.recv(65535)
print(output.decode())
ssh.close()
input()



#X.find X.endswith()