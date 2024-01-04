import os
import time
import pyautogui

os.popen('..\\ldconsole.exe launch --index 1')
time.sleep(60)
os.popen('..\\ldconsole.exe runapp --index 1 --packagename com.jingdong.app.mall')
time.sleep(60)
os.popen('..\\adb.exe kill-server')
time.sleep(10)
os.popen('..\\adb.exe devices')
time.sleep(10)
os.popen('..\\ldconsole.exe runapp --index 1 --packagename com.jingdong.app.mall')
time.sleep(10)
os.popen('..\\ldconsole.exe adb --index 1 --command "shell input tap 976 1841"')
time.sleep(10)
os.popen('..\\ldconsole.exe adb --index 1 --command "shell input tap 205 627"')
time.sleep(10)
os.popen('..\\ldconsole.exe adb --index 1 --command "shell input tap 205 627"')
time.sleep(10)
os.popen('..\\ldconsole.exe adb --index 1 --command "shell input tap 890 1847"')
time.sleep(10)
os.popen('..\\adb.exe kill-server')

pyautogui.moveTo(1491,1355,1)
pyautogui.PAUSE = 0.05
while True :
    pyautogui.click()