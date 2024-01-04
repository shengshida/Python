
#!/usr/bin/python3
import _thread
import subprocess
import time
import re

# 为线程定义一个函数
def CMDPing(ipname):
    global thread_lock
    thread_lock = thread_lock + 1

    result=subprocess.getstatusoutput('ping ' + ipname)
    result=subprocess.getstatusoutput('ping ' + ipname)
    if result[0] == 0 :
        print(ipname + ' 成功！')
        with open('Ping.log','a',encoding='UTF-8') as file :
            file.write(ipname + ' 成功！')
    elif result[0] == 1 :
        print(ipname + ' 失败！')
        with open('Ping.log','a',encoding='UTF-8') as file :
            file.write(ipname + ' 失败！')
    thread_lock = thread_lock - 1

thread_lock = 0
with open('1.txt','r',encoding='UTF-8') as file_1 :
    for line_1 in file_1 :
        match_obj_1 = re.match(r'.*?(\d*\.\d*\.\d*\.\d*).*?',line_1,re.I)
        if match_obj_1 !=None:
            time.sleep(0.2)
            ipname = match_obj_1[1]
            _thread.start_new_thread(CMDPing, (ipname,))
            print(ipname)

while thread_lock != 0 :
    time.sleep(1)
    print('子线程未结束，休眠一秒')
print('脚本结束')
input()