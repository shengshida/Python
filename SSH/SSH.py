import socket
import paramiko
import time

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
    cli = ssh.invoke_shell()
    time.sleep(10)
    cli.send("screen-length disable\n")
    time.sleep(1)
    cli.send("sy\n")
    time.sleep(1)
    cli.send("und local-user whccb class manage\n")
    time.sleep(1)
    cli.send("sa f\n")
    time.sleep(10)
    output = cli.recv(65535)
    print(output.decode())
    ssh.close()
