#coding utf-8 
#python3 

import random
import time
import os
from Function import clockin_action
import sys
import requests
import json

print ("脚本开始")

with open('./log/clockin_log.log',"a",encoding="UTF-8") as file : 
    file.write('\n' + time.asctime(time.localtime(time.time())) + " && " + "Strar-up-Clockin_v1.0.py" + " && " + "脚本开始运行") 

Start_time = time.asctime(time.localtime(time.time()))[11:13]
if Start_time != "07" and Start_time != "19" :
    print("未到打卡时间,程序10秒后退出")
    with open('./log/clockin_log.log',"a",encoding="UTF-8") as file : 
        file.write('\n' + time.asctime(time.localtime(time.time())) + " && " + "Strar-up-Clockin_v1.0.py" + " && " + "未到打卡时间，脚本退出") 
    time.sleep(10)
    sys.exit(0)

#随机一个分钟，在之后完成打卡和更新时间
match_minute = str(random.randint(10,30))
print ("随时时间已生成,下一次打卡时间为7:" + match_minute )

with open('./log/clockin_log.log',"a",encoding="UTF-8") as file : 
    file.write('\n' + time.asctime(time.localtime(time.time())) + " && " + "Strar-up-Clockin_v1.0.py" + " && " + "脚本生成打卡时间") 

time.sleep(60)

try :
    WX_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c376785d-a1fa-4ba9-9ef9-46c061f5e11c"
    DD_url = "https://oapi.dingtalk.com/robot/send?access_token=9c992c506733a8f649db33ce7ffdf15b9225c51b4917fe3c9c26cf6bdf6ebdec"
    header = {'Content-Type':'application/json'}
    data = {
        "msgtype" : "markdown" ,
        'markdown' : {
            "title" : "Clock-In Start-Up",
            "text" : "#### Clock-In Start-Up\n#### Start-Time:" + match_minute + "\n#### " + time.asctime(time.localtime(time.time())) ,
            "content" : "Clock-In Start-Up\nStart-Time:" + match_minute + "\n" + time.asctime(time.localtime(time.time()))
        }
    }
    json_data = json.dumps(data)
    requests.post(url=WX_url,data=json_data,headers=header)
    requests.post(url=DD_url,data=json_data,headers=header)
    with open('./log/clockin_log.log',"a",encoding="UTF-8") as file : 
        file.write('\n' + time.asctime(time.localtime(time.time())) + " && " + "Strar-up-Clockin_v1.0.py" + " && " + "向微信发送打卡时间通知") 
except :
    with open('./log/clockin_log.log',"a",encoding="UTF-8") as file : 
        file.write('\n' + time.asctime(time.localtime(time.time())) + " && " + "Strar-up-Clockin_v1.0.py" + " && " + "网络连接异常") 

while True :
    #获取现在时间
    match_nowtime = time.asctime(time.localtime(time.time()))[11:16]

    #当时间为7点或19点时更新位置后完成打卡动作
    if match_nowtime == "07:" + match_minute or match_nowtime == "19:" + match_minute :
        with open('./log/clockin_log.log',"a",encoding="UTF-8") as file : 
            file.write('\n' + time.asctime(time.localtime(time.time())) + " && " + "Strar-up-Clockin_v1.0.py" + " && " + "脚本开始打卡") 
        clockin_action()
        break
    time.sleep(10)

time.sleep(60)
os.popen("shutdown -s -t 60")
print ("脚本结束,10秒后关闭窗口,60秒后关闭系统")
with open('./log/clockin_log.log',"a",encoding="UTF-8") as file : 
    file.write('\n' + time.asctime(time.localtime(time.time())) + " && " + "Strar-up-Clockin_v1.0.py" + " && " + "脚本打卡完成") 
time.sleep(10)