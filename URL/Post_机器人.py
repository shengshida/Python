#coding utf-8 
#python3 

import requests
import json
import time
import random

match_minute = str(random.randint(10,30))
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
request=requests.post(url=DD_url,data=json_data,headers=header)
print(request.text)
request=requests.post(url=WX_url,data=json_data,headers=header)
print(request.text)
#print(data)


#G9MQEP1is4Ztb6tjcZuM4DMoBQevIpI8-tnnzKIXSMA