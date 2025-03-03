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
        ssh.connect(hostname = "10.30.3.254", port = 22,username = "admin", password = "Sybfh@huawei7700", timeout=30)
    except :
        with open("error.txt","a",encoding="UTF-8") as file :
            file.write(name + "_" + ip + "_采集错误\n")
        return
    time.sleep(3)
    ssh_log = ssh.invoke_shell()
    ssh_log.send("system-view\n")
    time.sleep(1)
    ssh_log.send("stelnet " + ip + "\n")
    time.sleep(1)
    ssh_log.send("admin\n")
    time.sleep(10)
    ssh_log.send("y\n")
    time.sleep(2)
    ssh_log.send("n\n")
    time.sleep(8)
    ssh_log.send("Sybfh@huawei7700\n")
    time.sleep(2)
    iter_cli = iter(cli)
    for i in iter_cli:
        match_Obj_1 = re.match(r"(.+?),(\d+)",i,re.I)
        send_cli = match_Obj_1[1]
        send_sleep = int(match_Obj_1[2])
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
    with open("[" + name + "]_[" + ip + "]" + ".txt","ab") as file :
        file.write(output)
    time.sleep(1)
    print("完成采集_" + name)
    return

file_mgmt = "file_mgmt.csv"
file_huawei_cli = "huawei_cli.csv"
max_threas = 4

thread_pool = threading.BoundedSemaphore(max_threas)

dict_cli = {"huawei":[],"cisco":[]}

Thread_list = []


with open(file_huawei_cli,"r",encoding="UTF-8") as file_1 :
    for line_1 in file_1 :
        dict_cli["huawei"].append(re.sub(r"(\r\n)|(\n)","",line_1))

with open(file_mgmt,"r",encoding="UTF-8") as file_3 :
    for line_3 in file_3 :
        match_Obj_1=re.match(r"(.*),(.*),(.*)",line_3,re.I)
        if match_Obj_1 != None and match_Obj_1[3] in dict_cli :
            cli = dict_cli[match_Obj_1[3]]
            Thread_1=myThread(match_Obj_1[1],match_Obj_1[2],cli,thread_pool)
            Thread_1.start()
            time.sleep(0.2)
            Thread_list.append(Thread_1)


for i in Thread_list :
    i.join()

print("脚本结束")
input()