#!/usr/bin/python3

import _thread
import subprocess
import time

# 为线程定义一个函数
def CMDPing(ipname):
    global thread_lock
    thread_lock = thread_lock + 1
    result=subprocess.getstatusoutput("ping " + ipname)
    result=subprocess.getstatusoutput("ping " + ipname)
    if result[0] == 0 :
        #print(ipname + "  成功！\n")
        with open("Ping.log","a",encoding="UTF-8") as file : 
            file.write(ipname + "  成功！\n") 
    elif result[0] == 1 :
        #print(ipname + "  失败！\n")
        with open("Ping.log","a",encoding="UTF-8") as file : 
            file.write(ipname + "  失败！\n") 
    thread_lock = thread_lock - 1

network = "10.255.255."
thread_lock = 0
for a in range(255) :
    time.sleep(1)
    ipname = network + str(a)
    try:
        _thread.start_new_thread(CMDPing, (ipname,))
    except:
        print ("Error: 无法启动线程")

while thread_lock != 0 :
    time.sleep(1)
    print("子线程未结束，休眠一秒")

print("脚本结束")
input()