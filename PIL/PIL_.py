#python3

from PIL import ImageGrab
import io
import sys
import time
import re

output = io.StringIO()
sys.stdout = output
im = ImageGrab.grabclipboard()
buf = io.BytesIO()
im.save(buf, format="png")
byte_im  = buf.getvalue()
print(byte_im)
result = output.getvalue()
sys.stdout = sys.__stdout__

now_time = re.sub(r":| ","_",time.asctime( time.localtime(time.time()) ))
"""
with open(now_time + ".txt","a") as file:
    for i in range(0,len(result),100000) :
        file.write(result[i:i+100000]+"|n")
"""
with open(now_time + ".txt","a") as file:
    file.write(result)

print(len(byte_im))
input()