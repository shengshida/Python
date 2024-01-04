import random
a = int(input("输入一个最小值\n"))
b = int(input("输入一个最大值\n"))
c = int(input("输入你猜想的数字\n"))
d = int(random.randint(a,b))
e = c-d
if c-d :
	if (e+c<a or e+c>b) :
		print("游戏结束，数字是",d)
	else:
		if c>d :
			print("你和这个值差",c-d)
		else:
			print("你和这个值差",d-c)
		g = int(input("你猜这个数是多少\n"))
		if g-d :
			print("游戏结束，数字是",d)
		else:
			print("恭喜你猜对了，数字就是",d)
else:
		print("你猜对了，数字就是",d)
n = input()