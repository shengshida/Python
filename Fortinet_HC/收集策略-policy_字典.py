#coding utf-8 
#python3 

import re 
import codecs 
 
#声明match_1 
def match_1(match_file,match_line,match_number,match_list): 
	print("正在收集第"+match_number+"行！") 
	#Match条件等于Edit时输出Edit的值-策略编号 
	match_Obj_1=re.match(r'.*edit (\d*).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[0]=match_Obj_1.group(1)
	#Match条件等于Srcintf时输出
	match_Obj_1=re.match(r'.*set srcintf "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[1]=match_Obj_1.group(1)
	#Match条件等于Dstintf时输出
	match_Obj_1=re.match(r'.*set dstintf "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[2]=match_Obj_1.group(1)
	#Match条件等于Srcaddr时输出
	match_Obj_1=re.match(r'.*set srcaddr "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[3]=match_Obj_1.group(1)	 
	#Match条件等于Dstaddr时输出
	match_Obj_1=re.match(r'.*set dstaddr "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[4]=match_Obj_1.group(1)	 
	#Match条件Status是否生效 
	match_Obj_1=re.match(r'.*set action (accept).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[5]=match_Obj_1.group(1)	 
	#Match条件等于Schedule时
	match_Obj_1=re.match(r'.*set schedule "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[6]=match_Obj_1.group(1)	 
	#Match条件等于Service时
	match_Obj_1=re.match(r'.*set service "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[7]=match_Obj_1.group(1)	 
	#Match条件等于Tags时
	match_Obj_1=re.match(r'.*set tags "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[8]=match_Obj_1.group(1)	 
	#Match条件等于Tags时
	match_Obj_1=re.match(r'.*set comments "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[9]=match_Obj_1.group(1)	 
	#Match条件等于NAT时
	match_Obj_1=re.match(r'.*set nat (enable).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[10]=match_Obj_1.group(1)	 
	#Match条件等于Ippool时
	match_Obj_1=re.match(r'.*set ippool (enable).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[11]=match_Obj_1.group(1)	 
	#Match条件等于Poolname时
	match_Obj_1=re.match(r'.*set poolname "(.*)".*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_list[12]=match_Obj_1.group(1)	
	#Match条件等于Next时换行 
	match_Obj_1=re.match(r'.*(next).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(str(match_list)+'\n') 
			match_list=[" "," "," "," "," "," "," "," "," "," "," "," "," "]
			return match_list
	return match_list
#输入需要打开的文件和输出文件的名字 
filename_1=input("请输入匹配文本名字\n") + ".txt" 
filename_2=input("请输入输出文本名字\n") + ".txt" 
policy_list=[" "," "," "," "," "," "," "," "," "," "," "," "," "]
line_number=0 
#读取匹配文本 
with open(filename_1,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number=line_number + 1 
		policy_list=match_1(filename_2,line_1,str(line_number),policy_list) 
print("脚本结束") 
input() 
#脚本结束