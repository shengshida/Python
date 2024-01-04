#coding utf-8
#python3
#---------------------------------------------------------------
#为了保证生成脚本准确性，原始文本请格式化后使用,格式化方法如下：
#1.文本内容要为utf-8（最好复制内容到新建UTF-8文本中）
#2.双空格变单空格
#3.每行以空格结尾
#---------------------------------------------------------------
#Juniper配置生成H3c配置-白名单_ISG2000
import re
import codecs
import sys

#声明match_policy
def match_policy(match_line,policy_filename,source_zone,destination_zone,policy_name):
	match_policy_1=re.match(r'^set policy id (\d*) .*from "(.*)" to "(.*)" ".*" ".*" ".*" permit (.*)$',match_line,re.I)
	if match_policy_1 != None :
		if re.match(r'.*(infranet-auth).*',match_policy_1.group(4),re.I) == None :
			source_zone = re.sub(r'-',"_",match_policy_1.group(2))
			destination_zone = re.sub(r'-',"_",match_policy_1.group(3))
			policy_name = re.sub(r' ',"_",match_policy_1.group(1))
			with open(policy_filename,"a",encoding="UTF-8") as file :
				file.write(source_zone + "#" + destination_zone + "#" + policy_name + '\n')
			return
	return

def match_object(match_line,object_filename):
	match_object_1=re.match(r'^set (address|group address) ".*" ".*" .*$',match_line,re.I)
	if match_object_1 != None :
		with open(object_filename,"a",encoding="UTF-8") as file :
			file.write(match_line)
		return
	return

def match_policy_address(source_zone,destination_zone,policy_name,match_filename,source_filename,destination_filename):
	with open(match_filename,"r",encoding="UTF-8") as file :
		for match_line in file :
			match_number = 0
			match_policy_address_1=re.match(r'^set policy id (\d*) .*from "(.*)" to "(.*)" "(.*)" "(.*)" ".*" permit .*$',match_line,re.I)
			if match_policy_address_1 != None :
				if source_zone == re.sub(r'-',"_",match_policy_address_1.group(2)) and destination_zone == re.sub(r'-',"_",match_policy_address_1.group(3)) and policy_name == re.sub(r' ',"_",match_policy_address_1.group(1)) :
					with open(source_filename,"a",encoding="UTF-8") as file :
						file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + re.sub(r' ',"_",match_policy_address_1.group(4)) + '\n')
					with open(destination_filename,"a",encoding="UTF-8") as file :
						file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + re.sub(r' ',"_",match_policy_address_1.group(5)) + '\n')
					source_zone = re.sub(r'-',"_",match_policy_address_1.group(2))
					destination_zone = re.sub(r'-',"_",match_policy_address_1.group(3))
					policy_name == re.sub(r' ',"_",match_policy_address_1.group(1))
					match_number = match_number + 1
					return source_zone,destination_zone,policy_name
			if match_number != 0 :
				match_policy_address_1=re.match(r'^(set src-address "(.*)" )$',match_line,re.I)
				if match_policy_address_1 != None :
					with open(source_filename,"a",encoding="UTF-8") as file :
						file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + re.sub(r' ',"_",match_policy_address_1.group(1)) + '\n')
					return source_zone,destination_zone,policy_name
				match_policy_address_1=re.match(r'^(set dst-address "(.*)" )$',match_line,re.I)
				if match_policy_address_1 != None :
					with open(source_filename,"a",encoding="UTF-8") as file :
						file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + re.sub(r' ',"_",match_policy_address_1.group(1)) + '\n')
					return source_zone,destination_zone,policy_name
			match_policy_address_1=re.match(r'^(exit )$',match_line,re.I)
			if match_policy_address_1 != None :
				match_number = 0
	return source_zone,destination_zone,policy_name

def match_address(match_zone,match_name,match_filler,object_filename,full_filename):
	with open(object_filename,"r",encoding="UTF-8") as file :
		for match_line in file :
			match_address_1=re.match(r'^set address "(.*)" "(.*)" (\d*\.\d*\.\d*\.\d*) (\d*\.\d*\.\d*\.\d*) .*$',match_line,re.I)
			if match_address_1 != None :
				if match_zone == re.sub(r'-',"_",match_address_1.group(1)) and match_name == re.sub(r' ',"_",match_address_1.group(2)) :
					with open(full_filename,"a",encoding="UTF-8") as file :
						file.write(match_filler + match_address_1.group(3) + "#" + match_address_1.group(4) + '\n')
					return
			match_address_1=re.match(r'^set group address "(.*)" "(.*)" add "(.*)" .*$',match_line,re.I)
			if match_address_1 != None :
				if match_zone == re.sub(r'-',"_",match_address_1.group(1)) and match_name == re.sub(r' ',"_",match_address_1.group(2)) :
					match_address(match_zone,re.sub(r' ',"_",match_address_1.group(3)),match_filler,object_filename,full_filename)
#			match_address_1=re.match(r'^set group address "(.*)" "(.*)" add "(.*)" .*$',match_line,re.I)
#			if match_address_1 != None :
#				if match_zone == re.sub(r'-',"_",match_address_1.group(1)) and match_name == re.sub(r' ',"_",match_address_1.group(2)) :
#					match_address(match_zone,re.sub(r' ',"_",match_address_1.group(3)),match_filler,object_filename,full_filename)
	return

def match_fullmatch(match_name,match_address,full_destination_filename,done_filename):
	with open(full_destination_filename,"r",encoding="UTF-8") as file :
		for match_line in file :
			match_fullmatch_1=re.match(r'^(.*#.*#.*#)(\d*\.\d*\.\d*\.\d*#\d*\.\d*\.\d*\.\d*)$',match_line,re.I)
			if match_fullmatch_1 != None :
				if match_name == match_fullmatch_1.group(1) :
					match_fullmatch_2 = match_fullmatch_1.group(2)
					match_fullmatch_2 = match_name + match_address + "#" + match_fullmatch_2 + "#"
					with open(done_filename,"a",encoding="UTF-8") as file :
						file.write(match_fullmatch_2 + '\n')
	return

#输入需要打开的文件和输出文件的名字
match_filename = input("请输入匹配文本名字\n") + ".txt"
done_filename = input("请输入输出文本名字\n") + ".txt"
object_filename = "object.txt"
policy_filename = "policy.txt"
source_filename = "source.txt"
destination_filename = "destination.txt"
full_source_filename = "full_source.txt"
full_destination_filename = "full_destination.txt"

source_zone = "0"
destination_zone = "0"
policy_name = "0"

#执行第一步：收集白名单策略名
print("脚本开始\n正在执行第一步：收集白名单策略名")
with open(match_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_policy(match_line,policy_filename,source_zone,destination_zone,policy_name)

#执行第二步：收集地址对象、地址对象组
print("正在执行第二步：收集地址对象、地址对象组")
with open(match_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_object(match_line,object_filename)

#执行第三步：收集白名单源目地址对象
print("正在执行第三步：收集白名单源目地址对象")
with open(policy_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_policy_address_1=re.match(r'^(.*)#(.*)#(.*)$',match_line,re.I)
		if match_policy_address_1 != None :
			source_zone,destination_zone,policy_name=match_policy_address(match_policy_address_1.group(1),match_policy_address_1.group(2),match_policy_address_1.group(3),match_filename,source_filename,destination_filename)

#执行第四步：收集白名单真实源目地址
print("正在执行第四步：收集白名单真实源目地址")
with open(source_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_address_1=re.match(r'^(.*)#(.*)#(.*)#(.*)$',match_line,re.I)
		if match_address_1 != None :
			match_filler = match_address_1.group(1) + "#" +match_address_1.group(2) + "#" + match_address_1.group(3) + "#"
			if match_address_1.group(4) == "Any" :
				with open(full_source_filename,"a",encoding="UTF-8") as file :
					file.write(match_filler + "0.0.0.0#0.0.0.0" + '\n')
				continue
			match_address(match_address_1.group(1),match_address_1.group(4),match_filler,object_filename,full_source_filename)
with open(destination_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_address_1=re.match(r'^(.*)#(.*)#(.*)#(.*)$',match_line,re.I)
		if match_address_1 != None :
			match_filler = match_address_1.group(1) + "#" +match_address_1.group(2) + "#" + match_address_1.group(3) + "#"
			if match_address_1.group(4) == "Any" :
				with open(full_destination_filename,"a",encoding="UTF-8") as file :
					file.write(match_filler + "0.0.0.0/0" + '\n')
				continue
			match_address(match_address_1.group(2),match_address_1.group(4),match_filler,object_filename,full_destination_filename)
#执行第五步：输出整合文本
print("正在执行第五步：输出整合文本")
with open(full_source_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_fullmatch_1=re.match(r'^(.*#.*#.*#)(\d*\.\d*\.\d*\.\d*#\d*\.\d*\.\d*\.\d*)$',match_line,re.I)
		if match_fullmatch_1 != None :
			match_fullmatch(match_fullmatch_1.group(1),match_fullmatch_1.group(2),full_destination_filename,done_filename)

print("脚本结束")
input()
#脚本结束