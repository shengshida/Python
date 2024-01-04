import time
import re
import socket
import paramiko
import _thread

def ssh_connect(name,ip):

    global thread_lock
    thread_lock = thread_lock + 1
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname = ip,port = 22,username = "admin",password = "Admin@123",timeout=10)
    except socket.timeout:
        print("连接超时")
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("连接失败")
    except paramiko.ssh_exception.AuthenticationException:
        print("认证失败")
    else:
        stdin,stdout,stderr = ssh.exec_command("dis cur \n")
        out_txt = name +'.txt'
        with open(out_txt,"a",encoding="UTF-8") as file : 
            file.write(stdout.read().decode().replace('\r','')) 
        ssh.close()
    thread_lock = thread_lock - 1


print("输入匹配文本")
match_txt = input()
thread_lock = 0

with open(match_txt,"r",encoding="UTF-8") as file : 
    for line in file : 
        match_obj=re.match(r'(.*)_(\d*\.\d*\.\d*\.\d*)$',line,re.I) 
        if match_obj != None :
            Equipment_name = match_obj.group(1)
            Equipment_ip = match_obj.group(2)
            time.sleep(0.2)
            try:
                _thread.start_new_thread(ssh_connect, (Equipment_name,Equipment_ip,))
            except:
                print ("Error: 无法启动线程")

while thread_lock != 0 :
    time.sleep(1)
    print("子线程未结束，休眠一秒")

print("脚本结束")
input()
