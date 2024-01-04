#coding utf-8
#python3

import re
import codecs

#声明match_1
def match_1(match_file,match_line,match_number):
	#Match条件等于Edit时输出Edit的值-策略编号
	match_Obj_1=re.match(r'    edit (.*)$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')
	#Match条件等于Srcintf时输出Srcintf的值-源Zone
	match_Obj_1=re.match(r'        set srcintf "(.*)"$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')
	#Match条件等于Dstintf时输出Dstintf的值-目Zone
	match_Obj_1=re.match(r'        set dstintf "(.*)"$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')	
	#Match条件等于Srcaddr时输出Srcaddr的值-源IP
	match_Obj_1=re.match(r'            set srcaddr (.*)$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')		
	#Match条件等于Dstaddr时输出Dstaddr的值-目IP
	match_Obj_1=re.match(r'            set dstaddr (.*)$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')
	#Match条件等于Schedule时输出Schedule的值-生效时间
	match_Obj_1=re.match(r'        set schedule "(.*)"$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')
	#Match条件等于Service时输出Service的值-目端口
	match_Obj_1=re.match(r'            set service (.*)$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')
	#Match条件等于Poolname时输出Poolname的值-NAT的地址
	match_Obj_1=re.match(r'            set poolname "(.*)"$',match_line,re.I)
		#Match值不为空时写入输出文本
	if match_Obj_1 != None :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write(match_Obj_1.group(1)+'#')
	if match_line == "    next\n" :
		with open(match_file,"a",encoding="UTF-8") as file :
			file.write('\n')
	return
#输入需要打开的文件和输出文件的名字
filename_1=input("请输入匹配文本名字\n") + ".txt"
filename_2=input("请输入输出文本名字\n") + ".txt"

line_number=0
#读取匹配文本
with open(filename_1,"r",encoding="UTF-8") as file :
	#把读取的每一行的数据和输入的文件名传递给 match_1
	for line_1 in file :
		line_number=line_number + 1
		match_1(filename_2,line_1,line_number)
#脚本结束