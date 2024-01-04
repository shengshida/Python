#coding utf-8 
#python3 
#收集华为端口信息
import re 
import codecs 

def match_1(match_file,match_line,match_number): 
	print("正在收集第"+match_number+"行！") 

	#Match条件
	match_Obj_1=re.match(r'(.*)current state :(.*)\(ifindex: .*\)',match_line,re.I) 
	#Match值不为空时写入输出文本 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("\n" + match_Obj_1.group(1) + ',' + match_Obj_1.group(2) + ',' ) 
		return

	#Match条件
	match_Obj_1=re.match(r'Description: (.*)',match_line,re.I) 
	#Match值不为空时写入输出文本 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + ',') 
		return

	#Match条件
	match_Obj_1=re.match(r'Route Port,Hash arithmetic : According to flow, Maximal BW: (.*), Current BW: .*, The Maximum Transmit Unit is .*',match_line,re.I) 
	#Match值不为空时写入输出文本 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + ',') 
		return

	#Match条件
	match_Obj_1=re.match(r'Port BW: (.*), Transceiver max BW: .*, Transceiver Mode: .*',match_line,re.I) 
	#Match值不为空时写入输出文本 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + ',') 
		return

	#Match条件
	match_Obj_1=re.match(r'    Last 300 seconds input utility rate:  (.*)',match_line,re.I) 
	#Match值不为空时写入输出文本 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + ',') 
		return

	#Match条件
	match_Obj_1=re.match(r'    Last 300 seconds output utility rate: (.*)',match_line,re.I) 
	#Match值不为空时写入输出文本 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + ',') 
		return

#输入需要打开的文件和输出文件的名字 
filename_1=input("请输入匹配文本名字\n") + ".txt" 
filename_2=input("请输入输出文本名字\n") + ".csv" 
 
line_number=0 
#读取匹配文本 
with open(filename_1,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number=line_number + 1 
		match_1(filename_2,line_1,str(line_number)) 
print("脚本结束") 
input() 
#脚本结束