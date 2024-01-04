#python

def chat(text) :
    #url = 'https://open.feishu.cn/open-apis/bot/v2/hook/1ceb6c03-20ae-4afc-ad5c-7c722ae42e42'
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/4090d72d-04ff-4c26-b5f8-35be5bada176'
    text_data = '(^_^)' + text
    data = {'msg_type':'text','content':{'text':text_data}}
    header = {'Content-Type':'application/json'}
    body = json.dumps(data)
    if re.search('success',requests.post(url,data=body,headers=header).text) == None :
        print("{:>50}".format("消息发送失败"))
        return
    print("{:>50}".format("消息发送成功"))
    return

import json
import requests
import re

print("脚本开始")
while True :
    text_str = input()
    if text_str == '' :
        print('输入为空重新输入！')
        continue
    chat(text_str)