import re
import requests
import os
from urllib.request import urlopen

headers = {
'Accept':'text/html',
'Accept-Encoding':'gzip',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Cookie':'_ga=GA1.1.669794363.1720517251; _ga_KMWK3HTJJQ=GS1.1.1720572185.2.1.1720578271.0.0.0; cf_clearance=9yUg7Y4wQE1EiFZWEEfy9B2h8sOyVixrNf8vbf_I9qY-1720578272-1.0.1.1-qVT1BYF3g6L5GNJuuOx2FQRRZ4is2lzS0QVsQPSQjmWrFsYWleA6Wee9_4lOUAPnclpvRqxCipw.SlSLPBUQ9g',
'If-Modified-Since':'Tue, 09 Jul 2024 15:05:53 GMT',
'Priority':'u=0, i',
'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'none',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get('https://baozimh.org/manga/yirenzhixia-dongmantang', headers=headers, timeout=5)

#response.encoding = 'GBK'
#response.encoding = 'utf-8'

print(response.status_code)
#with open("out_txt.htm","a",encoding="UTF-8") as file : 
#    file.write(response.text)
