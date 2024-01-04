import paramiko
import socket
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(hostname = "10.0.0.1",port = 22,username = "admin",password = "Admin@123",timeout=10)
except socket.timeout:
    print("连接超时")
except paramiko.ssh_exception.NoValidConnectionsError:
    print("连接失败")
except paramiko.ssh_exception.AuthenticationException:
    print("认证失败")
else:
    stdin,stdout,stderr = ssh.exec_command("dis clo \n")
    print(stdout.read().decode())
    ssh.close()
input()