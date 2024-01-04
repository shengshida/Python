class Test(object):
	def _init_ (self,name):
		self.name=name
		
	@property
	def nianling (self,age):
		self.age=age
	@nianling.setter
	def nianling(self,age):
		if not isinstance(age,int):
			raise ValueError ("score must be an inteager!")
		if age < 0 or age >100:
			raise ValueError ("score must between 0`100!")

	def print_age (self):
		if self.age >= 18 :
			return ("你成年了！")
		else :
			return ("你未成年！")

ad=Test()
print ("输入你的名字")
ad.name=input()
print ("输入你的年龄")
ad.age=input()
print (ad.print_age())

