import random
import time
print ("这是一个掷色子猜大小的游戏\n")
def dahuoxiao(x):
	if (x==1 or x==2) :
		return x
	else :
		x = int(input ("输入错误，请输入大小，猜大请输入1,猜小请输入2\n"))
		return dahuoxiao(x)
a = int(input ("请输入大小，猜大请输入1,猜小请输入2\n"))
a = dahuoxiao(a)
b = random.randint(1,6)
if a == 1 :
	print ("您输入的大，买定离手")
	time.sleep(2)
	print ("开~~~,数字是",b)
	if b>=4 :
		print ("恭喜客官，您猜对了")
	else :
		print ("抱歉客官，您猜错了")
else :
	print ("您输入的小，买定离手")
	time.sleep(2)
	print ("开~~~,数字是",b)
	if b<=3 :
		print ("恭喜客官，您猜对了\n")
	else :
		print ("抱歉客官，您猜错了\n")
input()