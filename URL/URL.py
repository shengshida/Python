#coding utf-8 
#python3 

from urllib.request import urlopen
import time
try :
    URL = "https://sctapi.ftqq.com/SCT148937TjbF0erjEQKSScMXqQljuqpah.send?title=Clock-In%20Fail%20"
    myURL = urlopen(URL)
    print(myURL.read())
except :
    print("网络故障")


#tasklist |find "dnplayer.exe"
#urlopen("https://sctapi.ftqq.com/SCT148937TjbF0erjEQKSScMXqQljuqpah.send?title=Clock-In%20Fail%20")