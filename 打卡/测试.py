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
    time.sleep(10)
    os.popen('ldconsole.exe killapp --index 0 --packagename com.tencent.mm')
    time.sleep(10)
    os.popen('ldconsole.exe runapp --index 0 --packagename com.tencent.mm')
    time.sleep(60)
    os.popen('adb.exe kill-server')
    time.sleep(10)
    os.popen('adb.exe devices')
    time.sleep(10)
    os.popen('ldconsole.exe runapp --index 0 --packagename com.tencent.mm')
    time.sleep(10)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 132 1878"')
    time.sleep(10)
    os.popen('ldconsole.exe adb --index 0 --command "shell input swipe 600 179 600 1562 500"')
    time.sleep(10)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 97 585"')
    time.sleep(60)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 57 106"')
    time.sleep(60)
    #os.popen('ldconsole.exe adb --index 0 --command "shell input tap 541 1425"')
    time.sleep(60)
    os.popen('ldconsole.exe adb --index 0 --command "shell input tap 1015 108"')
    time.sleep(10)
    os.popen('adb.exe kill-server')
    time.sleep(10)
    os.popen('ldconsole.exe killapp --index 0 --packagename com.tencent.mm')


clockin_action()
input()