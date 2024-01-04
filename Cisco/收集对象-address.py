#coding utf-8 
#python3 

import re 
 
#声明match_1 
def match_1(match_file,match_line,match_number): 
	print("正在收集第"+match_number+"行！") 

	match_Obj_1=re.match(r'.*interface (GigabitEthernet\d*/\d*/\d*).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write('\n' + match_Obj_1.group(1)) 
		return

	match_Obj_1=re.match(r'.* switchport access vlan (\d*).*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("    " + match_Obj_1.group(1)) 
		return
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
		match_1(filename_2,line_1,str(line_number)) 
print("脚本结束") 
input() 
#脚本结束