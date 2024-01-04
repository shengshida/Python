import atexit
from urllib.request import urlopen
import time

def a():
    Send_URL = urlopen("https://sctapi.ftqq.com/SCT148937TjbF0erjEQKSScMXqQljuqpah.send?title=Complete-Clock_in")

atexit.register(a)
while True :
    time.sleep(3)
    print("b")