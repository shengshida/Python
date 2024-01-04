#coding utf-8 
#python3 

import random
import time
import os
import easyocr
import re
import sys
import json
import requests

def clockin_check() :

    os.popen('..\\adb.exe kill-server')
    time.sleep(10)
    os.popen('..\\adb.exe devices')
    time.sleep(10)
    os.popen('..\\ldconsole.exe adb --index 0 --command "shell screencap -p /sdcard/clockin/Check.png"')
    time.sleep(10)
    os.popen('..\\ldconsole.exe adb --index 0 --command "pull /sdcard/clockin/Check.png ./pictures/Check.png"')
    time.sleep(10)
    reader = easyocr.Reader(['ch_sim'])
    result = reader.readtext('./pictures/Check.png')
    for i in result:
        word = i[1]  # type: ignore
        match_success = re.match(r'.*(武汉市).*',word,re.I)
        if match_success != None :
            with open('./log/clockin_log.csv',"a") as file : 
                file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "坐标检查正常" + '\n') 
            print("坐标检查成功")
            return 0

        match_success = re.match(r'.*(允许).*',word,re.I)
        if match_success != None :
            with open('./log/clockin_log.csv',"a") as file : 
                file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "坐标检查到需要权限" + '\n') 
            print("坐标检查到需要权限")
            return 2

    print("坐标标检查失败")
    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "坐标检查失败" + '\n') 
        print("坐标检查失败")
    return 1

def clockin_check_twice() :

    os.popen('..\\adb.exe kill-server')
    time.sleep(10)
    os.popen('..\\adb.exe devices')
    time.sleep(10)
    os.popen('..\\ldconsole.exe adb --index 0 --command "shell screencap -p /sdcard/clockin/Check.png"')
    time.sleep(10)
    os.popen('..\\ldconsole.exe adb --index 0 --command "pull /sdcard/clockin/Check.png ./pictures/Check.png"')
    time.sleep(10)
    reader = easyocr.Reader(['ch_sim'])
    result = reader.readtext('./pictures/Check.png')
    for i in result:
        word = i[1]  # type: ignore
        match_success = re.match(r'.*(打卡成功).*',word,re.I)
        if match_success != None :
            with open('./log/clockin_log.csv',"a") as file : 
                file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "打卡检查正常" + '\n') 
            print("打卡检查成功")
            return 0

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "打卡检查失败" + '\n') 
        print("打卡检查失败")
    return 1

def clockin_call() :

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "正在拨打微信电话" + '\n') 
        print("正在拨打微信电话")

    time.sleep(10)
    os.popen('..\\ldconsole.exe killapp --index 0 --packagename com.tencent.mm')
    time.sleep(10)
    os.popen('..\\ldconsole.exe runapp --index 0 --packagename com.tencent.mm')
    time.sleep(60)
    os.popen('..\\ld -s 0 input tap 132 1878')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 314 173')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 1043 1876')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 669 1642')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 539 1782')
    time.sleep(30)
    os.popen('..\\ld -s 0 input tap 539 1782')
    time.sleep(10)

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "微信电话通知完成" + '\n') 
        print("微信电话通知完成")
    os.popen('..\\ldconsole.exe quitall')
    sys.exit(0)

def clockin_position() :

    #随机选择一个经纬度然后返回
    clockin_location = {}

    clockin_location['100'] = '114.335367,30.506942'
    clockin_location['101'] = '114.334964,30.507689'
    clockin_location['102'] = '114.334675,30.505494'
    clockin_location['103'] = '114.334442,30.505143'
    clockin_location['104'] = '114.334649,30.505158'
    clockin_location['105'] = '114.33466,30.507226'
    clockin_location['106'] = '114.335645,30.506045'
    clockin_location['107'] = '114.334714,30.507337'
    clockin_location['108'] = '114.333847,30.507083'
    clockin_location['109'] = '114.333885,30.507385'
    clockin_location['110'] = '114.335121,30.506451'
    clockin_location['111'] = '114.334771,30.506873'
    clockin_location['112'] = '114.335723,30.505767'
    clockin_location['113'] = '114.333065,30.507019'
    clockin_location['114'] = '114.335899,30.505952'
    clockin_location['115'] = '114.333762,30.505128'
    clockin_location['116'] = '114.333883,30.506113'
    clockin_location['117'] = '114.335942,30.506884'
    clockin_location['118'] = '114.3355,30.506931'
    clockin_location['119'] = '114.333618,30.506121'
    clockin_location['120'] = '114.33304,30.506503'
    clockin_location['121'] = '114.335829,30.507767'
    clockin_location['122'] = '114.333843,30.50727'
    clockin_location['123'] = '114.335206,30.505543'
    clockin_location['124'] = '114.335679,30.506913'
    clockin_location['125'] = '114.334533,30.506101'
    clockin_location['126'] = '114.335906,30.50603'
    clockin_location['127'] = '114.334786,30.506715'
    clockin_location['128'] = '114.33477,30.505367'
    clockin_location['129'] = '114.333206,30.506192'
    clockin_location['130'] = '114.333482,30.50744'
    clockin_location['131'] = '114.333498,30.505563'
    clockin_location['132'] = '114.335278,30.505296'
    clockin_location['133'] = '114.334056,30.50544'
    clockin_location['134'] = '114.335838,30.506932'
    clockin_location['135'] = '114.333093,30.505976'
    clockin_location['136'] = '114.334814,30.505194'
    clockin_location['137'] = '114.333171,30.507756'
    clockin_location['138'] = '114.33336,30.507413'
    clockin_location['139'] = '114.334346,30.505665'
    clockin_location['140'] = '114.334816,30.506195'
    clockin_location['141'] = '114.334753,30.506361'
    clockin_location['142'] = '114.335607,30.50696'
    clockin_location['143'] = '114.335095,30.505651'
    clockin_location['144'] = '114.335204,30.506521'
    clockin_location['145'] = '114.335285,30.507097'
    clockin_location['146'] = '114.335017,30.507589'
    clockin_location['147'] = '114.335244,30.505027'
    clockin_location['148'] = '114.335633,30.507322'
    clockin_location['149'] = '114.334045,30.507341'
    clockin_location['150'] = '114.335727,30.507558'
    clockin_location['151'] = '114.33366,30.507515'
    clockin_location['152'] = '114.335053,30.50715'


    number_id = str(random.randint(100,152))

    return number_id,clockin_location[number_id]

def clockin_action() :

    #打开打卡环境
    clockin_count = 1
    time.sleep(10)

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "打开打卡环境" + '\n') 

    print ("正在启动打卡环境")
    os.popen('..\\ldconsole.exe launch --index 0')
    time.sleep(60)

    #打开应用
    while True :

        if  clockin_count > 3 :
            clockin_call()
        clockin_count = clockin_count + 1

        position_id,position_coordinate = clockin_position()

        clockin_cli = "..\\ldconsole.exe action --index 0 --key call.locate --value " + position_coordinate
        os.popen(clockin_cli)
        position_coordinate = re.sub(r',',':',position_coordinate)
        with open('./log/clockin_log.csv',"a") as file : 
            file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "已完成更新坐标，坐标为" + position_coordinate + '\n') 
        print ("位置已更新，更新位置为" + position_coordinate)

        os.popen('..\\ldconsole.exe runapp --index 0 --packagename com.tencent.wework')
        time.sleep(60)

        with open('./log/clockin_log.csv',"a") as file : 
            file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "打开打卡应用" + '\n') 

        print ("正在启动打卡应用")

        os.popen('..\\ldconsole.exe runapp --index 0 --packagename com.tencent.wework')
        time.sleep(10)
        os.popen('..\\ld -s 0 input tap 110 1860')
        time.sleep(10)
        os.popen('..\\ld -s 0 input tap 70 380')
        time.sleep(10)
        os.popen('..\\ld -s 0 input tap 340 1880')
        time.sleep(10)

        #检查打卡界面是否正常

        with open('./log/clockin_log.csv',"a") as file : 
            file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "检查打卡界面" + '\n') 

        print ("正在检查打卡界面")

        position_check = clockin_check()
        new_name = re.sub(r' ',"_",re.sub(r':',"_",time.asctime(time.localtime(time.time()))))
        os.rename('./pictures/Check.png','./pictures/' + new_name + '.png')

        if position_check == 1 :
            os.popen('..\\ldconsole.exe killapp --index 0 --packagename com.tencent.wework')
            time.sleep(600)
            continue

        if position_check == 2 :
            os.popen('..\\ld -s 0 input tap 900 1815')
            with open('./log/clockin_log.csv',"a") as file : 
                file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "点击“允许”按键" + '\n') 
                print("点击“允许”按键")
            time.sleep(60)

        time.sleep(10)
        os.popen('..\\ld -s 0 input tap 540 720')
        time.sleep(10)

        with open('./log/clockin_log.csv',"a") as file : 
            file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "检查打卡是否正常" + '\n') 
            print("检查打卡是否正常")

        #执行打卡并做打卡检查

        clockin_time_check = clockin_check_twice()
        new_name = re.sub(r' ',"_",re.sub(r':',"_",time.asctime(time.localtime(time.time()))))
        os.rename('./pictures/Check.png','./pictures/' + new_name + '.png')
        if clockin_time_check == 1 :
            os.popen('..\\ldconsole.exe killapp --index 0 --packagename com.tencent.wework')
            time.sleep(600)
            continue
        time.sleep(10)
        os.popen('..\\ld -s 0 input tap 540 1410')
        time.sleep(10)

        #保存截图准备向微信发送图片
        os.popen('..\\ld -s 0 input tap 750 1880')
        time.sleep(10)  
        os.popen('..\\ld -s 0 screencap -p /sdcard/clockin/Check.png')
        time.sleep(10)

        os.popen('..\\ld -s 0 input tap 45 85')
        time.sleep(10)
        os.popen('..\\ld -s 0 input tap 45 85')
        time.sleep(10)
        break

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "打卡完成" + '\n') 

    print ("打卡已完成，打卡时间为 " + time.asctime(time.localtime(time.time())))
    time.sleep(10)
    os.popen('..\\adb.exe kill-server')
    time.sleep(10)
    os.popen('..\\ldconsole.exe killapp --index 0 --packagename com.tencent.wework')
    time.sleep(10)

    #发送打卡成功图片

    os.popen('..\\ldconsole.exe runapp --index 0 --packagename com.tencent.mm')
    time.sleep(60)

    os.popen('..\\ld -s 0 input tap 60 175')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 1043 1875')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 155 1635')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 240 150')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 600 1880')
    time.sleep(10)
    os.popen('..\\ld -s 0 input tap 1000 80')
    time.sleep(60)
    os.popen('..\\ld -s 0 input tap 45 80')
    time.sleep(10)
    print("打卡图片完成发送")
    #打卡结束，发送通知

    os.popen('..\\ldconsole.exe quitall')
    time.sleep(10)
    WX_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c376785d-a1fa-4ba9-9ef9-46c061f5e11c"
    DD_url = "https://oapi.dingtalk.com/robot/send?access_token=9c992c506733a8f649db33ce7ffdf15b9225c51b4917fe3c9c26cf6bdf6ebdec"
    header = {'Content-Type':'application/json'}
    data = {
        "msgtype" : "markdown" ,
        'markdown' : {
            "title" : "Clock-In Complete",
            "text" : "#### Clock-In Complete\n#### Position_ID:" + position_id + "\n#### " + time.asctime(time.localtime(time.time())) ,
            "content" : "Clock-In Complete\nPosition_ID:" + position_id + "\n" + time.asctime(time.localtime(time.time()))
        }
    }
    json_data = json.dumps(data)
    requests.post(url=WX_url,data=json_data,headers=header)
    requests.post(url=DD_url,data=json_data,headers=header)

    with open('./log/clockin_log.csv',"a") as file : 
        file.write(time.asctime(time.localtime(time.time())) + ","+ "Function.py" + ","+ "向微信发送完成打卡通知" + '\n') 
        print("完成机器人通知")

