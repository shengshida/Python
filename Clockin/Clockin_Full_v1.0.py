#coding utf-8 
#python3 

import random
import time
from Function import clockin_action

print ("脚本开始")

with open('./log/clockin_log.csv',"a") as file : 
    file.write(time.asctime(time.localtime(time.time())) + ","+ "Clockin_Full_v1.0.py" + ","+ "脚本开始运行" + '\n') 

#随机一个分钟，在之后完成打卡和更新时间
match_minute = str(random.randint(10,30))
match_check = 0

print ("随时时间已生成,下一次打卡时间为7:" + match_minute )

with open('./log/clockin_log.csv',"a") as file : 
    file.write(time.asctime(time.localtime(time.time())) + ","+ "Clockin_Full_v1.0.py" + ","+ "脚本生成打卡时间" + '\n') 

while True :
    #获取现在时间
    match_nowtime = time.asctime(time.localtime(time.time()))[11:16]

    #当时间为7点或19点时更新位置后完成打卡动作
    if match_check == 0 :
        if match_nowtime == "07:" + match_minute or match_nowtime == "19:" + match_minute :

            with open('./log/clockin_log.csv',"a") as file : 
                file.write(time.asctime(time.localtime(time.time())) + ","+ "Clockin_Full_v1.0.py" + ","+ "脚本开始打卡" + '\n') 

            clockin_action()
            match_check = 1

    #当时间为8点或20点时随机下一个打卡时间
    if match_check == 1 :
        if match_nowtime == "08:" + match_minute or match_nowtime == "20:" + match_minute :
            match_minute = str(random.randint(10,30))
            print ("随时时间已生成,下一次打卡时间为7:" + match_minute)

            with open('./log/clockin_log.csv',"a") as file : 
                file.write(time.asctime(time.localtime(time.time())) + ","+ "Clockin_Full_v1.0.py" + ","+ "脚本生成打卡时间" + '\n') 

            clockin_action()
            match_check = 0

    time.sleep(10)
