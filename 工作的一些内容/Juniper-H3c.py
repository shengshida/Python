#coding utf-8 
#python3 
#原始文本请格式化后使用(格式化方式为:1.\r\n变成\n。2.\n变成空格+\n。3.空格+空格变成空格) 
#Juniper配置生成H3c配置 
import re 
import codecs 
 
#声明match_1 
def match_1(match_file,match_line,match_number): 
	print("正在收集第"+match_number+"行！") 
	#收集Service
	match_Obj_1=re.match(r'^set service "(.*)" (.*) (tcp|udp) src-port (\d*)-(\d*) dst-port (\d*)-(\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = match_Obj_1.group(1)
		match_Obj_2=re.sub(r' ',"_",match_Obj_2)
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group service " + match_Obj_2 + '\n' + "service " + match_Obj_1.group(3) + " source range " + match_Obj_1.group(4) + " " + match_Obj_1.group(5) + " destination range " + match_Obj_1.group(6) + " " + match_Obj_1.group(7) + '\n') 
		return

	#收集Address
	match_Obj_1=re.match(r'^set address "(.*)" "(.*)" (\d*\.\d*\.\d*\.\d*) (\d*\.\d*\.\d*\.\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = match_Obj_1.group(2)
		match_Obj_2=re.sub(r' ',"_",match_Obj_2)
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group ip address " + match_Obj_2 + '\n' + "network subnet " + match_Obj_1.group(3) + " " + match_Obj_1.group(4) + '\n') 
		return

	#收集Group Address
	match_Obj_1=re.match(r'^set group address "(.*)" "(.*)" add "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = match_Obj_1.group(2)
		match_Obj_2=re.sub(r' ',"_",match_Obj_2)
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group ip address " + match_Obj_2 + '\n' + "network group-object " + match_Obj_1.group(3) + '\n') 
		return

	#收集Policy
	match_Obj_1=re.match(r'^set policy id (\d*).* from "(.*)" to "(.*)" "(.*)" "(.*)" "(.*)" (permit|deny) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("security-policy ip" + '\n' + "rule name Juniper_" + match_Obj_1.group(1) + '\n' + "counting enable" + '\n' + "source-zone " + match_Obj_1.group(2) + '\n' + "destination-zone " + match_Obj_1.group(3) + '\n' )
		if match_Obj_1.group(4) != "ANY" :
			match_Obj_2 = match_Obj_1.group(4)
			match_Obj_2=re.sub(r' ',"_",match_Obj_2)
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("source-ip " + match_Obj_2 + '\n')
		if match_Obj_1.group(5) != "ANY" :
			match_Obj_2 = match_Obj_1.group(5)
			match_Obj_2=re.sub(r' ',"_",match_Obj_2)
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("destination-ip " + match_Obj_2 + '\n')
		if match_Obj_1.group(6) != "ANY" :
			match_Obj_2 = match_Obj_1.group(6)
			match_Obj_2=re.sub(r' ',"_",match_Obj_2)
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("service " + match_Obj_2 + '\n')
		if match_Obj_1.group(7) == "permit" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action pass" + '\n')
		if match_Obj_1.group(7) == "deny" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action drop" + '\n')
		return

	#收集Plolic追加项
	match_Obj_1=re.match(r'^set src-address "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("source-ip " + match_Obj_1.group(1) + '\n') 
		return
	match_Obj_1=re.match(r'^set dst-address "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("destination-ip " + match_Obj_1.group(1) + '\n') 
		return
	match_Obj_1=re.match(r'^set service "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service " + match_Obj_1.group(1) + '\n') 
		return
	match_Obj_1=re.match(r'^set policy id 24 (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		if match_Obj_1 == "disable" : 
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write(match_Obj_1.group(1) + '\n') 
		return

	return 
#输入需要打开的文件和输出文件的名字 
old_filename=input("请输入匹配文本名字\n") + ".txt" 
new_filename=input("请输入输出文本名字\n") + ".txt" 
 
line_number=0 
#读取匹配文本 
with open(old_filename,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number=line_number + 1 
		match_1(new_filename,line_1,str(line_number)) 
print("脚本结束") 
input() 
#脚本结束