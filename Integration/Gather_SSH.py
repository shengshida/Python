#python3

import threading
import paramiko
import time
import pandas

class myThread (threading.Thread):
    def __init__(self, devicename, mgmtip, username, password, cli, thread_pool):
        threading.Thread.__init__(self)
        self.devicename = devicename
        self.mgmtip = mgmtip
        self.username = username
        self.password = password
        self.cli = cli
        self.thread_pool = thread_pool
    def run(self):
        self.thread_pool.acquire()
        print("正在采集_" + self.devicename)
        gather_ssh(self.devicename, self.mgmtip, self.username, self.password, self.cli)
        self.thread_pool.release()


def gather_ssh(devicename, mgmtip, username, password, cli):
    output = b""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        ssh.connect(hostname = mgmtip, port = 22,username = username, password = password, timeout=180)
    except :
        with open("error.txt","a",encoding="UTF-8") as file :
            file.write(devicename + "_" + mgmtip + "_采集错误\n")
        return
    time.sleep(3)
    ssh_log = ssh.invoke_shell()
    for command, waitingtime in iter(cli) :
        send_cli = command
        send_sleep = int(waitingtime)
        ssh_log.send(send_cli + "\n")
        time.sleep(send_sleep)
        while True :
            cli_match = ssh_log.recv(65535)
            output += cli_match
            if len(cli_match) < 65535 :
                break
            #print("取出中")
            time.sleep(1)
    ssh_log.close()
    ssh.close()
    with open("[" + devicename + "]_[" + mgmtip + "]" + ".txt","ab") as file :
        file.write(output)
    time.sleep(1)
    print("完成采集_" + devicename)
    return

max_threas = 128
thread_pool = threading.BoundedSemaphore(max_threas)
Thread_list = []

file_execl = "Device.xlsx"
pandas_cli = pandas.read_excel("Device.xlsx", "Cli", index_col=None)
pandas_mgmt = pandas.read_excel("Device.xlsx", "Information", index_col=None)
dict_cli = {}

cli_manufacturer = pandas_cli["厂商"]
cli_command = pandas_cli["命令"]
cli_waitingtime = pandas_cli["等待时长"]
for manufacturer, command, waitingtime in zip(iter(cli_manufacturer), iter(cli_command), iter(cli_waitingtime)) :
    if (manufacturer in dict_cli) == False:
        dict_cli[manufacturer] = []
    
    dict_cli[manufacturer].append((command,waitingtime))

ssh_manufacturer = pandas_mgmt["厂商"]
ssh_devicename = pandas_mgmt["设备名称"]
ssh_mgmtip = pandas_mgmt["管理地址"]
ssh_username = pandas_mgmt["用户名"]
ssh_password = pandas_mgmt["密码"]
for manufacturer, devicename, mgmtip, username, password in zip(iter(ssh_manufacturer), iter(ssh_devicename), iter(ssh_mgmtip),iter(ssh_username),iter(ssh_password) ) :
    if manufacturer in dict_cli :
        cli = dict_cli[manufacturer]
        Thread_1 = myThread(devicename, mgmtip, username, password, cli,thread_pool)
        Thread_1.start()
        time.sleep(0.2)
        Thread_list.append(Thread_1)


for i in Thread_list :
    i.join()

print("脚本结束")
input()