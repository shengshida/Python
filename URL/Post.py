#coding utf-8 
#python3 

import urllib.request
import urllib.parse
import requests
import json

url = "https://sctapi.ftqq.com/SCT148937TjbF0erjEQKSScMXqQljuqpah.send"
data = {'title':"Title" , 'desp':"Desp"}
json_data = json.dumps(data)
aheaders = {'Content-Type':'application/json'}
data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode
#request=urllib.request.Request(url, data)   # 请求处理
request=requests.post(url,data=json_data,headers=aheaders)   # 请求处理 headers=aheaders
#reponse=urllib.request.urlopen(request).read()

#print(reponse)
print(request.text)