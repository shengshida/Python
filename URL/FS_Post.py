#python3

import requests
import json


url = 'XXXX'
#url = 'XXXX'
data = {'msg_type':'text','content':{'text':'Webhookwebhook测试'}}
'''
content = {
        'msg_type': 'post',
        'content': {
                'post': {
                        'zh_cn': {
                                'title': 'Webhook',
                                'content': [
                                        [{
                                                        'tag': 'text',
                                                        'text': 'gather_ip'
                                                },
                                                {
                                                        'tag': 'a',
                                                        'text': '请查看',
                                                        'href': 'http://www.cisco.com/'
                                                },
                                                {
                                                        'tag': 'text',
                                                        'text': ''
                                                }
                                        ]
                                ]
                        }
                }
        }
}
'''
header = {'Content-Type':'application/json'}
body = json.dumps(data)

requests_1=requests.post(url,data=body,headers=header)

print(requests_1.status_code)
print(requests_1.json)
print(requests_1.text)
