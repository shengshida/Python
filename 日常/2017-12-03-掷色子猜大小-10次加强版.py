import random
import time
print ("这是一个掷色子猜大小的游戏，你需要连续赢10次，假如中间有一次失败，将从零开始计数\n")
def dahuoxiao(x):
	if (x==1 or x==2) :
		return x
	else :
		x = int(input ("输入错误，请输入大小，猜大请输入1,猜小请输入2\n"))
		return dahuoxiao(x)
def duiyucuo(m,n):
	if m == 1:
		print ("您输入的大，买定离手")
		time.sleep(2)
		print ("开~~~,数字是",n)
		if n>=4 :
			print ("恭喜客官，您猜对了")
			return 1
		else :
			print ("抱歉客官，您猜错了") 
			return 0
	else :
		print ("您输入的小，买定离手")
		time.sleep(2)
		print ("开~~~,数字是",n)
		if n<=3 :
			print ("恭喜客官，您猜对了")
			return 1
		else :
			print ("抱歉客官，您猜错了")
			return 0
def yxks(a):
	a = int(input ("请输入大小，猜大请输入1,猜小请输入2\n"))
	a = dahuoxiao(a)
	b = random.randint(1,6)
	return duiyucuo(a,b)
sum = 0
js = 0
while sum < 10:
	js = int(yxks(js))
	if js == 1:
		sum = sum + 1
		js = 10-sum
		if sum==10:
			print ("您已经猜对",sum,"次，请接收我对您的1024的爱\n")
		else :
			print ("您已经猜对",sum,"次，还剩下",js,"次\n")
	else :
		sum = 0
		print ("您猜错了，计数从零开始\n")
input()