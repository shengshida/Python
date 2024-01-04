#coding utf-8 
#python3 

from urllib.request import urlopen
import time
try :
    URL = "XXXX"
    myURL = urlopen(URL)
    print(myURL.read())
except :
    print("网络故障")


#tasklist |find "dnplayer.exe"
#urlopen("XXXX")