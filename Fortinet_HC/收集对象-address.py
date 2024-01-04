#coding utf-8 
#python3 
#收集Address并生成华为脚本 
import re 
import codecs 
 
#声明match_1 
def match_1(match_file,match_line,match_number,match_end_ip,match_start_ip): 
	print("正在收集第"+match_number+"行！") 
	#Match条件等于Edit时
	match_Obj_1=re.match(r'^.*edit "(.*)".*$',match_line,re.I) 
		#Match值不为空时
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("ip address-set " + match_Obj_1.group(1) + ' type object' + '\n') 
		return match_end_ip,match_start_ip
	#Match条件等于end-ip时
	match_Obj_1=re.match(r'^.*end-ip (\d*\.\d*\.\d*\.\d*).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_end_ip=match_Obj_1.group(1)
		return match_end_ip,match_start_ip
	#Match条件等于start-ip时
	match_Obj_1=re.match(r'^.*start-ip (\d*\.\d*\.\d*\.\d*).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_start_ip=match_Obj_1.group(1)
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(" address range " + match_start_ip + " " + match_end_ip + '\n') 
		return match_end_ip,match_start_ip
	#Match条件等于subnet时
	match_Obj_1=re.match(r'^.*subnet (\d*\.\d*\.\d*\.\d*) (\d*\.\d*\.\d*\.\d*).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(" address " + match_Obj_1.group(1) + " mask " + match_Obj_1.group(2) + '\n') 
		return match_end_ip,match_start_ip
	return match_end_ip,match_start_ip
#输入需要打开的文件和输出文件的名字 
filename_1=input("请输入匹配文本名字\n") + ".txt" 
filename_2=input("请输入输出文本名字\n") + ".txt" 
end_ip="0.0.0.0"
start_ip="0.0.0.0"
 
line_number=0 
#读取匹配文本 
with open(filename_1,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number=line_number + 1 
		end_ip,start_ip=match_1(filename_2,line_1,str(line_number),end_ip,start_ip) 
print("脚本结束") 
input() 
#脚本结束