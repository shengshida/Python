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
def match_1(match_file,output_file,match_line,match_number,match_name,match_protocol,match_line_old): 
	sys.stdout.write("                              \r") 
	sys.stdout.write("正在收集第"+match_number+"行！\r") 

	#收集Address
	match_Obj_1=re.match(r'^set security zones security-zone (.*) address-book address (.*) (\d*\.\d*\.\d*\.\d*)/(\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(2))
		match_Obj_3 = re.sub(r'-',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group ip address " + match_Obj_2 + '\n' + "network subnet " + match_Obj_1.group(3) + " " + match_Obj_1.group(4) + '\n') 
		return 0,0,match_line

	#收集Group Address
	match_Obj_1=re.match(r'^set security zones security-zone (.*) address-book address-set (.*) address (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(2))
		match_Obj_3 = re.sub(r'-',"_",match_Obj_1.group(1))
		match_Obj_4 = re.sub(r' ',"_",match_Obj_1.group(3))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if len(match_Obj_4) > 31 :
			match_Obj_4 = match_Obj_4[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group ip address " + match_Obj_2 + '\n' + "network group-object " + match_Obj_4 + '\n') 
		return 0,0,match_line

	#收集Group Address Set
	match_Obj_1=re.match(r'^set security zones security-zone (.*) address-book address-set (.*) address-set (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(2))
		match_Obj_3 = re.sub(r'-',"_",match_Obj_1.group(1))
		match_Obj_4 = re.sub(r' ',"_",match_Obj_1.group(3))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if len(match_Obj_4) > 31 :
			match_Obj_4 = match_Obj_4[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group ip address " + match_Obj_2 + '\n' + "network group-object " + match_Obj_4 + '\n') 
		return 0,0,match_line

	#收集Service_term
	match_Obj_1=re.match(r'^set applications application (.*) term (.*) protocol (tcp|udp) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		match_Obj_3=re.match(r'^.* (source-port|destination-port|protocol) .* ',match_line_old,re.I)
		if match_Obj_3 != None : 
			if match_Obj_3.group(1) == "source-port" :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write('\n') 
		if match_name != match_Obj_2 :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("object-group service " + match_Obj_2 + '\n') 
		return match_Obj_2,match_Obj_1.group(3),match_line
	match_Obj_1=re.match(r'^set applications application (.*) term (.*) source-port (\d*)-(\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service " + match_protocol + " source range " + match_Obj_1.group(3) + " " + match_Obj_1.group(4)) 
		return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) term (.*) source-port (\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service " + match_protocol + " source eq " + match_Obj_1.group(3)) 
		return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) term (.*) destination-port (\d*)-(\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		match_Obj_3=re.match(r'^.* (source-port|destination-port|protocol) .* ',match_line_old,re.I)
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if match_Obj_3 != None : 
			if match_Obj_3.group(1) == "protocol" :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write("service " + match_protocol + " destination range " + match_Obj_1.group(3) + " " + match_Obj_1.group(4) + '\n') 
				return match_Obj_2,match_protocol,match_line
			else :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write(" destination range " + match_Obj_1.group(3) + " " + match_Obj_1.group(4) + '\n') 
				return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) term (.*) destination-port (\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		match_Obj_3=re.match(r'^.* (source-port|destination-port|protocol) .* ',match_line_old,re.I)
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if match_Obj_3 != None : 
			if match_Obj_3.group(1) == "protocol" :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write("service " + match_protocol + " destination eq " + match_Obj_1.group(3) + '\n') 
				return match_Obj_2,match_protocol,match_line
			else :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write(" destination eq " + match_Obj_1.group(3) + '\n') 
				return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) term (.*) destination-port (\w*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file) as file : 
			lines = file.readlines()
			curr = lines[:-1]
		with open(match_file,"w",encoding="UTF-8") as file : 
			file.writelines(curr)
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service group-object " + match_Obj_1.group(3) + '\n') 
		return match_Obj_2,match_protocol,match_line

	#收集Service
	match_Obj_1=re.match(r'^set applications application (.*) protocol (tcp|udp) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		match_Obj_3=re.match(r'^.* (source-port|destination-port|protocol) .* ',match_line_old,re.I)
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if match_Obj_3 != None : 
			if match_Obj_3.group(1) == "source-port" :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write('\n') 
		if match_name != match_Obj_2 :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("object-group service " + match_Obj_2 + '\n') 
		return match_Obj_2,match_Obj_1.group(2),match_line
	match_Obj_1=re.match(r'^set applications application (.*) source-port (\d*)-(\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service " + match_protocol + " source range " + match_Obj_1.group(2) + " " + match_Obj_1.group(3)) 
		return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) source-port (\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service " + match_protocol + " source eq " + match_Obj_1.group(2)) 
		return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) destination-port (\d*)-(\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		match_Obj_3=re.match(r'^.* (source-port|destination-port|protocol) .* ',match_line_old,re.I)
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if match_Obj_3 != None : 
			if match_Obj_3.group(1) == "protocol" :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write("service " + match_protocol + " destination range " + match_Obj_1.group(2) + " " + match_Obj_1.group(3) + '\n') 
				return match_Obj_2,match_protocol,match_line
			else :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write(" destination range " + match_Obj_1.group(2) + " " + match_Obj_1.group(3) + '\n') 
				return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) destination-port (\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		match_Obj_3=re.match(r'^.* (source-port|destination-port|protocol) .* ',match_line_old,re.I)
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if match_Obj_3 != None : 
			if match_Obj_3.group(1) == "protocol" :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write("service " + match_protocol + " destination eq " + match_Obj_1.group(2) + '\n') 
				return match_Obj_2,match_protocol,match_line
			else :
				with open(match_file,"a",encoding="UTF-8") as file : 
					file.write(" destination eq " + match_Obj_1.group(2) + '\n') 
				return match_Obj_2,match_protocol,match_line
	match_Obj_1=re.match(r'^set applications application (.*) destination-port (\w*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file) as file : 
			lines = file.readlines()
			curr = lines[:-1]
		with open(match_file,"w",encoding="UTF-8") as file : 
			file.writelines(curr)
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("service group-object " + match_Obj_1.group(2) + '\n') 
		return match_Obj_2,match_protocol,match_line

	#收集Service-set
	match_Obj_1=re.match(r'^set applications application-set (.*) application (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		match_Obj_3=re.sub(r' ',"_",match_Obj_1.group(2))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		if len(match_Obj_3) > 31 :
			match_Obj_3 = match_Obj_3[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("object-group service " + match_Obj_2 + '\n' + "service group-object " + match_Obj_3 + '\n') 
		return match_Obj_2,match_protocol,match_line

	#收集Scheduler
	match_Obj_1=re.match(r'^set schedulers scheduler (.*) start-date (\d*)-(\d*)-(\d*)\.(\d*:\d*) stop-date (\d*)-(\d*)-(\d*)\.(\d*:\d*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(1))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("time-range " + match_Obj_2 + " from " + match_Obj_1.group(5) + " " + match_Obj_1.group(3) + "/" + match_Obj_1.group(4) + "/" + match_Obj_1.group(2) + " to " + match_Obj_1.group(9) + " " + match_Obj_1.group(7) + "/" + match_Obj_1.group(8) + "/" + match_Obj_1.group(6) + '\n') 
		return match_Obj_2,match_protocol,match_line

	#过滤未匹配内容
	match_Obj_1=re.match(r'^set security policies (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		return match_name,match_protocol,match_line
	match_Obj_1=re.match(r'^deactivate security policies (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		return match_name,match_protocol,match_line

	#输出未匹配内容
	with open(output_file,"a",encoding="UTF-8") as file : 
		file.write(match_number + ":" + match_line) 

	return match_name,match_protocol,match_line

def match_2(match_file,output_file,match_line,match_number,match_name): 
	sys.stdout.write("                              \r") 
	sys.stdout.write("正在收集第"+match_number+"行！\r") 

	#收集Policy_source-address
	match_Obj_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) match source-address (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(3))
		match_Obj_3 = re.sub(r'-',"_",match_Obj_1.group(1))
		match_Obj_4 = re.sub(r'-',"_",match_Obj_1.group(2))
		match_Obj_2 = match_Obj_3 + "_TO_" + match_Obj_4 + "_" + match_Obj_2
		if match_name != match_Obj_2 :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("security-policy ip" + '\n' + "rule name " + match_Obj_2 + '\n' + "counting enable" + '\n' + "source-zone " + match_Obj_3 + '\n' + "destination-zone " + match_Obj_4 + '\n')
		if match_Obj_1.group(4) != "any" :
			match_Obj_5=re.sub(r' ',"_",match_Obj_1.group(4))
			if len(match_Obj_5) > 31 :
				match_Obj_5 = match_Obj_5[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("source-ip " + match_Obj_5 + '\n')
		return match_Obj_2

	#收集Policy_destination-address
	match_Obj_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) match destination-address (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		if match_Obj_1.group(4) != "any" :
			match_Obj_2 = re.sub(r' ',"_",match_Obj_1.group(4))
			match_Obj_3 = re.sub(r'-',"_",match_Obj_1.group(2))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("destination-ip " + match_Obj_2 + '\n')
		return match_name

	#收集Policy_application
	match_Obj_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) match application (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		if match_Obj_1.group(4) != "any" :
			match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(4))
			if len(match_Obj_2) > 31 :
				match_Obj_2 = match_Obj_2[-31:]
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("service " + match_Obj_2 + '\n')
		return match_name

	#收集Policy_scheduler
	match_Obj_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) scheduler-name (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		match_Obj_2=re.sub(r' ',"_",match_Obj_1.group(4))
		if len(match_Obj_2) > 31 :
			match_Obj_2 = match_Obj_2[-31:]
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("time-range " + match_Obj_2 + '\n')
		return match_name

	#收集Policy_then
	match_Obj_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) then (permit|deny|reject) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		if match_Obj_1.group(4) == "permit" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action pass\n")
		if match_Obj_1.group(4) == "deny" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action drop\n")
		if match_Obj_1.group(4) == "reject" :
			with open(match_file,"a",encoding="UTF-8") as file : 
				file.write("action drop\n")
		return match_name

	#收集Policy_deactivate
	match_Obj_1=re.match(r'^deactivate security policies from-zone (.*) to-zone (.*) policy (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		with open(match_file,"a",encoding="UTF-8") as file : 
			file.write("disable\n") 
		return match_name

	#过滤未匹配内容
	match_Obj_1=re.match(r'^set security zones security-zone (.*) address-book (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		return match_name
	match_Obj_1=re.match(r'^set applications (.*) .*$',match_line,re.I) 
	if match_Obj_1 != None : 
		return match_name
	#输出未匹配内容
	with open(output_file,"a",encoding="UTF-8") as file : 
		file.write(match_number + ":" + match_line) 

	return match_name

#输入需要打开的文件和输出文件的名字 
old_filename=input("请输入匹配文本名字\n") + ".txt" 
new_filename_1=input("请输入输出文本名字\n") + ".txt" 
new_filename_2=input("请输入未匹配文本名字\n") + ".txt" 
 
#变量
line_number=0 
object_name="0"
object_protocol="0"
line_1="0"
line_old="0"

#读取匹配文本 
with open(old_filename,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number = line_number + 1 
		object_name,object_protocol,line_old = match_1(new_filename_1,new_filename_2,line_1,str(line_number),str(object_name),str(object_protocol),str(line_old)) 
#输出文件分割符
with open(new_filename_2,"a",encoding="UTF-8") as file : 
	file.write("\n\n--------------------------------------------------------\n\n") 
#行数清零
line_number=0 
with open(old_filename,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line_1 in file : 
		line_number = line_number + 1 
		object_name = match_2(new_filename_1,new_filename_2,line_1,str(line_number),str(object_name)) 

print("\n脚本结束") 

input() 
#脚本结束