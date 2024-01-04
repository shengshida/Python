#coding utf-8 
#python3 

import requests
import json
import time
import random

match_minute = str(random.randint(10,30))
WX_url = "XXXX"
DD_url = "XXXX"
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