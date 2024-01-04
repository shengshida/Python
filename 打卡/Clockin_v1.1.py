#coding utf-8 
#python3 

import subprocess
import random
import time

print ("脚本开始")

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

while 1 == 1 :
    match_nowtime = time.asctime(time.localtime(time.time()))[11:16]
    if match_nowtime == "01:00" or match_nowtime == "13:00" :
        clockin_number_id = int(random.randint(100,120))
        clockin_cli = "ldconsole.exe action --index 0 --key call.locate --value " + clockin_location[str(clockin_number_id)]
        clockin_log = subprocess.getstatusoutput(clockin_cli)
        if clockin_log[0] == 0 :
            print ("位置已完成更新,更新时间为 " + time.asctime(time.localtime(time.time())) + ",等待下次更新")
        time.sleep(100)
    time.sleep(10)