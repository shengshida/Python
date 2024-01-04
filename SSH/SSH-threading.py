#python3

import re
import threading
import paramiko
import time

class myThread (threading.Thread):
    def __init__(self, name, ip, cli, thread_pool):
        threading.Thread.__init__(self)
        self.name = name
        self.ip = ip
        self.cli = cli
        self.thread_pool = thread_pool
    def run(self):
        self.thread_pool.acquire()
        print("正在采集_" + self.name)
        gather_ssh(self.name,self.ip,self.cli)
        self.thread_pool.release()


def gather_ssh(name, ip, cli):
    output = b""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        ssh.connect(hostname = ip,port = 22,username = "admin",password = "Admin@123",timeout=30)
    except :
        with open("error.txt","a",encoding="UTF-8") as file :
            file.write(name + "_" + ip + "_采集错误")
        return
    time.sleep(0.2)
    ssh_log = ssh.invoke_shell()
    time.sleep(0.2)
    iter_cli = iter(cli)
    while True :
        try :
            ssh_log.send(next(iter_cli) + "")
        except :
            break
        time.sleep(3)
        while True :
            cli_match = ssh_log.recv(65535)
            output += cli_match
            if cli_match.find(b"More") == -1 :
                ssh_log.send("                    ")
                #print("发现More发送空格")
                time.sleep(3)
                continue
            if len(cli_match) < 65535 :
                break
            #print("取出中")
            time.sleep(3)
    ssh_log.close()
    ssh.close()
    with open("[" + name + "]_[" + ip + "]" + ".txt","ab") as file :
        file.write(re.sub(b"(.+More.+)|(.+More.+\[16D)|(.+More.+\[42D)|(.+More.+\[m)|(.+More.+ +)",b"",output))
    time.sleep(1)
    print("完成采集_" + name)
    return

file_mgmt = "file_mgmt.csv"
file_huawei_cli = "huawei_cli.csv"
file_cisco_cli = "cisco_cli.csv"
max_threas = 128

thread_pool = threading.BoundedSemaphore(max_threas)

huawei_cli =[]
cisco_cli =[]
Thread_list = []


with open(file_huawei_cli,"r",encoding="UTF-8") as file_1 :
    for line_1 in file_1 :
        huawei_cli.append(re.sub(r"()|()","",line_1))

with open(file_cisco_cli,"r",encoding="UTF-8") as file_2 :
    for line_2 in file_2 :
        cisco_cli.append(re.sub(r"()|()","",line_2))

with open(file_mgmt,"r",encoding="UTF-8") as file_3 :
    for line_3 in file_3 :
        match_Obj_1=re.match(r"(.*),(.*),(.*)",line_3,re.I)
        if match_Obj_1 == None :
            cli = cisco_cli
            if match_Obj_1[3] == "huawei" :
                cli = huawei_cli
            Thread_1=myThread(match_Obj_1[1],match_Obj_1[2],cli,thread_pool)
            Thread_1.start()
            time.sleep(0.2)
            Thread_list.append(Thread_1)


for i in Thread_list :
    i.join()

print("脚本结束")
input()
