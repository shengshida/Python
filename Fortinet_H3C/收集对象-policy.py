#coding utf-8 
#python3 
#收集Addrgrp并生成华三脚本 
import re 
import codecs 
 
#声明match_1 
def match_1(match_file,match_line,match_number): 
	print("正在收集第"+match_number+"行！") 

	match_Obj_1=re.match(r'.*edit (\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + "-") 
		return

	match_Obj_1=re.match(r'.*set srcintf "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + "-") 
		return

	match_Obj_1=re.match(r'.*set dstintf "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + "-") 
		return

	match_Obj_1=re.match(r'.*set schedule "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + '\n') 
		return

	return 

def match_2(match_file,match_line,match_number): 
	print("正在输出第"+match_number+"行！") 

	match_Obj_1=re.match(r'(\d*)-(\w*)-(\w*)-always$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-policy ip " + match_Obj_1.group(2) + "-" + match_Obj_1.group(3) + '\n' + "rule pass source-ip sou_" + match_Obj_1.group(1) + " destination-ip des_" + match_Obj_1.group(1) + " service ser_" + match_Obj_1.group(1) + '\n') 
		return

	match_Obj_1=re.match(r'(\d*)-(\w*)-(\w*)-(.*)$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-policy ip " + match_Obj_1.group(2) + "-" + match_Obj_1.group(3) + '\n' + "rule pass source-ip sou_" + match_Obj_1.group(1) + " destination-ip des_" + match_Obj_1.group(1) + " service ser_" + match_Obj_1.group(1) + " time-range " + match_Obj_1.group(4) + '\n' ) 
		return

	return 

#输入需要打开的文件和输出文件的名字 
filename_1=input("请输入匹配文本名字\n") + ".txt" 
filename_2=input("请输入输出-1文本名字\n") + ".txt" 
filename_3=input("请输入输出-2文本名字\n") + ".txt" 
line_number=0 
#读取匹配文本 
with open(filename_1,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number=line_number + 1 
		match_1(filename_2,line_1,str(line_number)) 
line_number=0 
with open(filename_2,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_2 
	for line_1 in file : 
		line_number=line_number + 1 
		match_2(filename_3,line_1,str(line_number)) 

print("脚本结束") 
input() 
#脚本结束