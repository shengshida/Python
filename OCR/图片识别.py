import easyocr
import re
import time
#reader = easyocr.Reader(['ch_sim','en'])
reader = easyocr.Reader(['ch_sim'])
result = reader.readtext('./pictures/99.png')
j = 0
match_nowtime = time.asctime(time.localtime(time.time()))[11:13]
for i in result:
    word = i[1]
    print(i)
    match_success = re.match(r'.*(\d\d\d\d).*(\d\d).*(\d\d\d\d).*(\d\d).*(\d\d).*',word,re.I)
    if match_success != None :
        j = j + 1
        print("成功")

if int(match_nowtime) < 12 and j == 1 :
    print("二次检查成功")
if int(match_nowtime) > 12 and j == 2 :
    print("二次检查成功")
#print(len(result))
print("脚本结束")
print(j)
input()


#ldconsole.exe adb --index 0 --command "shell screencap -p /sdcard/clockin/Check.png"
#ldconsole.exe adb --index 0 --command "pull /sdcard/clockin/Check.png ./clockin/Check.png"
#match_fail = re.match(r'(..:..:..)',match,re.I)
#import sys //sys.exit(0)