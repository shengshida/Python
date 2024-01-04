#coding utf-8 
#python3 

import subprocess
import random
import time
import keyboard
import os
import re
from urllib.request import urlopen

def clockin_action() :

    #手机打卡点击动作
    time.sleep(3)
    os.popen('ldconsole.exe killapp --index 0 --packagename com.tencent.mm')
    time.sleep(3)
    os.popen('ldconsole.exe runapp --index 0 --packagename com.tencent.mm')
    time.sleep(60)
    os.popen('adb.exe kill-server')
    time.sleep(5)
    os.popen('adb.exe devices')
    time.sleep(3)
    os.popen('ldconsole.exe runapp --index 0 --packagename com.tencent.mm')
    time.sleep(5)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 132 1878"')
    time.sleep(3)
    os.popen('ldconsole.exe adb --index 0 --command "shell input swipe 600 179 600 1562 500"')
    time.sleep(3)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 97 585"')
    time.sleep(30)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 57 106"')
    time.sleep(30)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 541 1425"')
    time.sleep(10)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 1015 108"')
    time.sleep(3)
    os.popen('adb.exe kill-server')
    time.sleep(3)
    os.popen('ldconsole.exe killapp --index 0 --packagename com.tencent.mm')
    time.sleep(3)
    Send_URL = urlopen("https://sctapi.ftqq.com/SCT148937TjbF0erjEQKSScMXqQljuqpah.send?title=Complete-Clock_in")

def clockin_start() :

    #打开打卡环境
    time.sleep(5)
    print ("正在启动安卓模拟器")
    os.popen("ldconsole.exe launch --index 0")
    time.sleep(60)
    os.popen('ldconsole.exe runapp --index 0 --packagename com.tencent.mm')
    time.sleep(60)
    os.popen('ldconsole.exe killapp --index 0 --packagename com.tencent.mm')
    print ("初始位置已更新")
    time.sleep(3)
    os.popen('ldconsole.exe action --index 0 --key call.locate --value 114.334882,30.505983')
    time.sleep(3)
    keyboard.press_and_release('ctrl+q')
    Send_URL = urlopen("https://sctapi.ftqq.com/SCT148937TjbF0erjEQKSScMXqQljuqpah.send?title=Open-run_environment")

def clockin_position() :

    #随机选择一个经纬度然后返回
    clockin_location = {}
    clockin_location['100'] = "114.308525,30.635971"
    clockin_location['101'] = "114.32703,30.518802"
    clockin_location['102'] = "114.336732,30.502125"
    clockin_location['103'] = "114.258508,30.537482"
    clockin_location['104'] = "114.253333,30.53151"
    clockin_location['105'] = "114.393613,30.632988"
    clockin_location['106'] = "114.365442,30.610612"
    clockin_location['107'] = "114.326923,30.5748"
    clockin_location['108'] = "114.332672,30.514586"
    clockin_location['109'] = "114.329222,30.515084"
    clockin_location['110'] = "114.410285,30.479734"
    clockin_location['111'] = "114.313708,30.543205"
    clockin_location['112'] = "114.246434,30.652376"
    clockin_location['113'] = "114.3769,30.50386"
    clockin_location['114'] = "114.431557,30.486705"
    clockin_location['115'] = "114.373774,30.517581"
    clockin_location['116'] = "114.352219,30.565021"
    clockin_location['117'] = "114.27439,30.591395"
    clockin_location['118'] = "114.393792,30.627721"
    clockin_location['119'] = "114.28136,30.613083"
    clockin_location['120'] = "114.298644,30.641922"
    clockin_location['121'] = "114.291727,30.574894"
    clockin_location['122'] = "114.291435,30.574656"
    clockin_location['123'] = "114.289847,30.57681"
    clockin_location['124'] = "114.271127,30.5848"
    clockin_location['125'] = "114.276382,30.577354"
    clockin_location['126'] = "114.265889,30.578007"
    clockin_location['127'] = "114.272339,30.595681"
    clockin_location['128'] = "114.268207,30.575255"
    clockin_location['129'] = "114.278699,30.576188"
    clockin_location['130'] = "114.290629,30.608922"
    clockin_location['131'] = "114.308092,30.60886"
    clockin_location['132'] = "114.413603,30.484477"
    clockin_location['133'] = "114.213768,30.563905"
    clockin_location['134'] = "114.402334,30.51311"
    clockin_location['135'] = "114.27045,30.622165"
    clockin_location['136'] = "114.26296,30.583441"
    clockin_location['137'] = "114.148851,30.629618"
    clockin_location['138'] = "114.306078,30.645472"
    clockin_location['139'] = "114.406996,30.644877"
    clockin_location['140'] = "114.335205,30.509469"
    clockin_location['141'] = "114.273092,30.585065"
    clockin_location['142'] = "114.349596,30.55344"
    clockin_location['143'] = "114.307092,30.60613"
    clockin_location['144'] = "114.329485,30.503509"
    clockin_location['145'] = "114.413419,30.484346"
    clockin_location['146'] = "114.330673,30.363691"
    clockin_location['147'] = "114.352458,30.598435"
    clockin_location['148'] = "114.213902,30.56388"
    clockin_location['149'] = "114.448928,30.509827"
    clockin_location['150'] = "114.402526,30.513024"
    clockin_location['151'] = "114.335136,30.50939"
    clockin_location['152'] = "114.293375,30.629159"
    clockin_location['153'] = "114.406877,30.644766"
    clockin_location['154'] = "114.343763,30.552633"
    clockin_location['155'] = "114.310471,30.656047"
    clockin_location['156'] = "114.358675,30.529104"
    clockin_location['157'] = "114.214415,30.563467"
    clockin_location['158'] = "114.147707,30.626595"
    clockin_location['159'] = "114.374718,30.620058"
    clockin_location['160'] = "114.273035,30.595811"
    clockin_location['161'] = "114.243624,30.656194"
    clockin_location['162'] = "114.326375,30.510352"
    clockin_location['163'] = "114.291526,30.590586"
    clockin_location['164'] = "114.347428,30.593103"
    clockin_location['165'] = "114.275767,30.580465"
    clockin_location['166'] = "114.158712,30.504293"
    clockin_location['167'] = "114.208896,30.634475"
    clockin_location['168'] = "114.124783,30.557229"
    clockin_location['169'] = "114.410275,30.51198"
    clockin_location['170'] = "114.272028,30.59511"
    clockin_location['171'] = "114.331245,30.502885"
    clockin_location['172'] = "114.397959,30.624373"
    clockin_location['173'] = "114.357903,30.604742"
    clockin_location['174'] = "114.431882,30.613936"
    clockin_location['175'] = "114.38015,30.883277"
    clockin_location['176'] = "114.137789,30.484402"
    clockin_location['177'] = "114.43821,30.510001"
    clockin_location['178'] = "114.353155,30.593339"
    clockin_location['179'] = "114.323622,30.535936"
    clockin_location['180'] = "114.264749,30.597529"
    clockin_location['181'] = "114.339569,30.501901"
    clockin_location['182'] = "114.449901,30.441151"
    clockin_location['183'] = "114.090615,30.315705"
    clockin_location['184'] = "114.257618,30.719646"
    clockin_location['185'] = "114.324857,30.558988"
    clockin_location['186'] = "114.346933,30.557609"
    clockin_location['187'] = "114.406382,30.643831"
    clockin_location['188'] = "114.045852,30.581356"
    clockin_location['189'] = "114.359666,30.615591"
    clockin_location['190'] = "114.392033,30.884089"
    clockin_location['191'] = "114.417605,30.489586"
    clockin_location['192'] = "114.134002,30.622731"
    clockin_location['193'] = "114.254227,30.590873"
    clockin_location['194'] = "114.247215,30.739189"
    clockin_location['195'] = "114.367627,30.624587"
    clockin_location['196'] = "114.426369,30.466004"
    clockin_location['197'] = "114.520408,30.528889"
    clockin_location['198'] = "114.406565,30.643877"
    clockin_location['199'] = "114.277861,30.586139"
    clockin_location['200'] = "114.116981,30.555827"
    clockin_location['201'] = "114.181359,30.513802"
    clockin_location['202'] = "114.283275,30.602181"
    clockin_location['203'] = "114.287416,30.585783"

    number_id = str(random.randint(100,203))

    return clockin_location[number_id]

print ("脚本开始")

#随机一个分钟，在之后完成打卡和更新时间
match_minute = str(random.randint(10,30))
match_check = 0

print ("下一次打卡时间为7:" + match_minute )

while True :
    #获取现在时间
    match_nowtime = time.asctime(time.localtime(time.time()))[11:16]

    #当时间为7点或19点时完成打卡动作
    if match_check == 0 :
        if match_nowtime == "07:" + match_minute or match_nowtime == "19:" + match_minute :
            clockin_action()
            print ("打卡已完成，打卡时间为 " + time.asctime(time.localtime(time.time())))
            match_check = 1

    #当时间为8点或20点时更新位置后再次随机一个时间
    if match_check == 1 :
        if match_nowtime == "08:" + match_minute or match_nowtime == "20:" + match_minute :
            clockin_cli = "ldconsole.exe action --index 0 --key call.locate --value " + clockin_position()
            clockin_log = subprocess.getstatusoutput(clockin_cli)
            if clockin_log[0] == 0 :
                print ("位置已完成更新,更新时间为 " + time.asctime(time.localtime(time.time())))
            match_minute = str(random.randint(10,30))
            print ("随时时间已生成,下一次打卡时间为7:" + match_minute)
            match_check = 0

    clockin_ceck = subprocess.getstatusoutput('tasklist | find "dnplayer"')

    if re.search(r'(dnplayer)',clockin_ceck[1]) == None :
        clockin_start()

    time.sleep(10)
