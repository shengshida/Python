#coding utf-8 
#python3 

import time
from Function import clockin_action
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--command",type=str,default="0")
argv = parser.parse_args()

print ("脚本开始,传递参数为" + argv.command)

with open('./log/clockin_log.csv',"a") as file : 
    file.write(time.asctime(time.localtime(time.time())) + ","+ "Oneclick_Clockin_v1.0.py" + ","+ "脚本开始运行" + '\n') 

clockin_action()

if argv.command == "1" :
    os.popen("shutdown -s -t 60")
    print ("脚本结束,10秒后关闭窗口,60秒后关闭系统")

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Oneclick_Clockin_v1.0.py" + ","+ "脚本打卡完成，一分钟后关机" + '\n') 

else :
    print ("脚本结束,10秒后关闭窗口")

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Oneclick_Clockin_v1.0.py" + ","+ "脚本打卡完成，十秒后退出脚本" + '\n') 

    time.sleep(10)