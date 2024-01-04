#coding utf-8 
#python3 
#---------------------------------------------------------------
#为了保证生成脚本准确性，原始文本请格式化后使用,格式化方法如下：
#1.文本内容要为utf-8
#2.双空格变单空格
#3.每行以空格结尾
#---------------------------------------------------------------
#Juniper配置生成H3c配置 
import re 
import codecs 
import sys 

#声明match_1 
def match_1(match_file,output_file,match_line,match_number,match_source,match_destination): 
	sys.stdout.write("                              \r") 
	sys.stdout.write("正在收集第"+match_number+"行！\r") 

	#收集Service
	match_Obj_1=re.match(r'^set service "(.*)" (.*) (tcp|udp) src-port (\d*)-(\d*) dst-port (\d*)-(\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group service " + match_Obj_2 + '\n' + "service " + match_Obj_1.group(3) + " source range " + match_Obj_1.group(4) + " " + match_Obj_1.group(5) + " destination range " + match_Obj_1.group(6) + " " + match_Obj_1.group(7) + '\n') 
		return match_source,match_destination

	#收集Group Service
	match_Obj_1=re.match(r'^set group service "(.*)" add "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(1))
		match_Obj_3 = re.sub(r' ',"_",match_Obj_1.group(2))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if len(match_Obj_3) > 31 :
			match_Obj_3 = match_Obj_3[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group service " + match_Obj_2 + '\n' + "service group-object " + match_Obj_3 + '\n') 
		return match_source,match_destination

	#收集Address
	match_Obj_1=re.match(r'^set address "(.*)" "(.*)" (\d*\.\d*\.\d*\.\d*) (\d*\.\d*\.\d*\.\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(2))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group ip address " + match_Obj_2 + '\n' + "network subnet " + match_Obj_1.group(3) + " " + match_Obj_1.group(4) + '\n') 
		return match_source,match_destination

	#收集Group Address
	match_Obj_1=re.match(r'^set group address "(.*)" "(.*)" add "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(2))
		match_Obj_3 = re.sub(r' ',"_",match_Obj_1.group(3))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if len(match_Obj_3) > 31 :
			match_Obj_3 = match_Obj_3[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group ip address " + match_Obj_2 + '\n' + "network group-object " + match_Obj_3 + '\n') 
		return match_source,match_destination

	#收集Scheduler
	match_Obj_1=re.match(r'^set scheduler "(.*)" once start (\d*/\d*/\d*) (\d*:\d*) stop (\d*/\d*/\d*) (\d*:\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("time-range " + match_Obj_2 + " from " + match_Obj_1.group(3) + " " + match_Obj_1.group(2) + " to " + match_Obj_1.group(5) + " " + match_Obj_1.group(4) + '\n') 
		return match_source,match_destination

	#收集Policy-Scheduler
	match_Obj_1=re.match(r'^set policy id (\d*) (.*)from "(.*)" to "(.*)" "(.*)" "(.*)" "(.*)" (permit|deny) schedule "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_source = re.sub(r'-',"_",match_Obj_1.group(3))
		match_destination = re.sub(r'-',"_",match_Obj_1.group(4))
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(9))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("security-policy ip" + '\n' + "rule name Juniper_" + match_Obj_1.group(1) + '\n' + "counting enable" + '\n' + "source-zone " + match_source + '\n' + "destination-zone " + match_destination + '\n' + "time-range " + match_Obj_2 + '\n')
		match_Obj_2=re.match(r'name "(.*)" ',match_Obj_1.group(2),re.I)
		if match_Obj_2 != None :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("description " + match_Obj_2.group(1) + '\n')
		if match_Obj_1.group(5) != "Any" :
			match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(5))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("source-ip " + match_Obj_2 + '\n')
		if match_Obj_1.group(6) != "Any" :
			match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(6))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("destination-ip " + match_Obj_2 + '\n')
		if match_Obj_1.group(7) != "ANY" :
			match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(7))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("service " + match_Obj_2 + '\n')
		if match_Obj_1.group(8) == "permit" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action pass" + '\n')
		if match_Obj_1.group(8) == "deny" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action drop" + '\n')
		return match_source,match_destination

	#收集Policy-Base
	match_Obj_1=re.match(r'^set policy id (\d*) (.*)from "(.*)" to "(.*)" "(.*)" "(.*)" "(.*)" (permit|deny) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_source = re.sub(r'-',"_",match_Obj_1.group(3))
		match_destination = re.sub(r'-',"_",match_Obj_1.group(4))
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("security-policy ip" + '\n' + "rule name Juniper_" + match_Obj_1.group(1) + '\n' + "counting enable" + '\n' + "source-zone " + match_source + '\n' + "destination-zone " + match_destination + '\n' )
		match_Obj_2=re.match(r'name "(.*)" ',match_Obj_1.group(2),re.I)
		if match_Obj_2 != None :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("description " + match_Obj_2.group(1) + '\n')
		if match_Obj_1.group(5) != "Any" :
			match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(5))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("source-ip " + match_Obj_2 + '\n')
		if match_Obj_1.group(6) != "Any" :
			match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(6))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("destination-ip " + match_Obj_2 + '\n')
		if match_Obj_1.group(7) != "ANY" :
			match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(7))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("service " + match_Obj_2 + '\n')
		if match_Obj_1.group(8) == "permit" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action pass" + '\n')
		if match_Obj_1.group(8) == "deny" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action drop" + '\n')
		return match_source,match_destination

	#收集Plolic追加项
	match_Obj_1=re.match(r'^set src-address "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("source-ip " + match_Obj_2 + '\n') 
		return match_source,match_destination
	match_Obj_1=re.match(r'^set dst-address "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("destination-ip " + match_Obj_2 + '\n') 
		return match_source,match_destination
	match_Obj_1=re.match(r'^set service "(.*)" .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service " + match_Obj_2 + '\n') 
		return match_source,match_destination
	match_Obj_1=re.match(r'^set policy id (.*) (disable) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(2) + '\n') 
		return match_source,match_destination

	#输出未匹配内容
	with open(output_file,"a",encoding="UTF-8") as file : 
		file.write(match_number + ":" + match_line) 

	return match_source,match_destination
#输入需要打开的文件和输出文件的名字 
old_filename=input("请输入匹配文本名字\n") + ".txt" 
new_filename_1=input("请输入输出文本名字\n") + ".txt" 
new_filename_2=input("请输入未匹配文本名字\n") + ".txt" 
 
line_number=0 
Object_source="0"
Object_destination="0"
#读取匹配文本 
with open(old_filename,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number = line_number + 1 
		Object_source,Object_destination = match_1(new_filename_1,new_filename_2,line_1,str(line_number),str(Object_source),str(Object_destination)) 
print("\n脚本结束") 
input() 
#脚本结束