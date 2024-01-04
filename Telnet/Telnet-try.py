import telnetlib
import time
import socket
HOST = "10.255.255.100"
user = "admin"
password = "Admin@123"
try :
    tn = telnetlib.Telnet(HOST,23,10)
    time.sleep(1)
except socket.timeout:
    print("连接超时")
except ConnectionRefusedError:
    print("主机拒绝")
else:
    tn.read_until(b"Username: ")
    time.sleep(1)
    tn.write(user.encode('UTF-8') + b"\n")
    time.sleep(1)
    tn.read_until(b"Password: ")
    time.sleep(1)
    tn.write(password.encode('UTF-8') + b"\n")
    time.sleep(5)
    eagerout = tn.read_very_eager().decode('UTF-8')
    if 'invalid' in eagerout:
        print("认证失败")
        tn.close()
    elif ">" in eagerout:
        print("认证成功")
        tn.write(b"enable\nAdmin@123\nterminal length 0\nsho run\n")
        time.sleep(5)
        tn.write(b"exit\n")
        tnout=tn.read_all()
        tn.close()
        print(tnout.decode('UTF-8'))
    elif "#" in eagerout:
        print("认证成功进入特权模式")
        tn.write(b"terminal length 0\nsho run\n")
        time.sleep(5)
        tn.write(b"exit\n")
        tnout=tn.read_all()
        tn.close()
        print(tnout.decode('UTF-8'))
print("脚本结束")
input()