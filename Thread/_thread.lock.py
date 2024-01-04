#!/usr/bin/python3

import _thread
import subprocess
import time

# 为线程定义一个函数
def CMDPing(ipname): 
    result=subprocess.getstatusoutput("ping " + ipname)
    result=subprocess.getstatusoutput("ping " + ipname)
    if result[0] == 0 :
        print(ipname + "  成功！\n")
        with open("Ping.log","a",encoding="UTF-8") as file : 
            file.write(ipname + "  成功！\n") 
    elif result[0] == 1 :
        print(ipname + "  失败！\n")
        with open("Ping.log","a",encoding="UTF-8") as file : 
            file.write(ipname + "  失败！\n") 
    lock_ping.release()

network = "10.255.255."
lock_ping = _thread.allocate_lock()
for a in range(255) :
    time.sleep(0.1)
    ipname = network + str(a)
    try:
        _thread.start_new_thread(CMDPing, (ipname,))
        lock_ping.acquire()
    except:
        print ("Error: 无法启动线程")
while lock_ping.locked()  :
    time.sleep(1)
    print("脚本未结束休眠一秒")
print("脚本结束")
input()