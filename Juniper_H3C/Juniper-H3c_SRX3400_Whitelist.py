#coding utf-8
#python3
#---------------------------------------------------------------
#为了保证生成脚本准确性，原始文本请格式化后使用,格式化方法如下：
#1.文本内容要为utf-8（最好复制内容到新建UTF-8文本中）
#2.双空格变单空格
#3.每行以空格结尾
#---------------------------------------------------------------
#Juniper配置生成H3c配置-白名单_SRX3400
import re
import codecs
import sys

#声明match_policy
def match_policy(match_line,policy_filename,source_zone,destination_zone,policy_name):
	match_policy_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) then permit (.*)$',match_line,re.I)
	if match_policy_1 != None :
		if re.match(r'.*(uac-policy).*',match_policy_1.group(4),re.I) == None :
			source_zone = re.sub(r'-',"_",match_policy_1.group(1))
			destination_zone = re.sub(r'-',"_",match_policy_1.group(2))
			policy_name = re.sub(r' ',"_",match_policy_1.group(3))
			with open(policy_filename,"a",encoding="UTF-8") as file :
				file.write(source_zone + "#" + destination_zone + "#" + policy_name + '\n')
			return source_zone,destination_zone,policy_name
		elif re.sub(r'-',"_",match_policy_1.group(1)) == source_zone and re.sub(r'-',"_",match_policy_1.group(2)) == destination_zone and re.sub(r' ',"_",match_policy_1.group(3)) == policy_name :
			with open(policy_filename) as file :
				lines = file.readlines()
				curr = lines[:-1]
			with open(policy_filename,"w",encoding="UTF-8") as file :
				file.writelines(curr)
			return source_zone,destination_zone,policy_name
	match_policy_1=re.match(r'^deactivate security policies from-zone (.*) to-zone (.*) policy (.*) $',match_line,re.I)
	if match_policy_1 != None :
		if re.sub(r'-',"_",match_policy_1.group(1)) == source_zone and re.sub(r'-',"_",match_policy_1.group(2)) == destination_zone and re.sub(r' ',"_",match_policy_1.group(3)) == policy_name :
			with open(policy_filename) as file :
				lines = file.readlines()
				curr = lines[:-1]
			with open(policy_filename,"w",encoding="UTF-8") as file :
				file.writelines(curr)
			return source_zone,destination_zone,policy_name
	return source_zone,destination_zone,policy_name

def match_object(match_line,object_filename):
	match_object_1=re.match(r'^set security zones security-zone (.*) address-book (.*)$',match_line,re.I)
	if match_object_1 != None :
		with open(object_filename,"a",encoding="UTF-8") as file :
			file.write(match_line)
		return
	return

def match_policy_address(source_zone,destination_zone,policy_name,match_filename,source_filename,destination_filename):
	match_source_number = 0
	match_destination_number = 0
	with open(match_filename,"r",encoding="UTF-8") as file :
		for match_line in file :
			match_policy_address_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) match source-address (.*) .*$',match_line,re.I)
			if match_policy_address_1 != None :
				if source_zone == re.sub(r'-',"_",match_policy_address_1.group(1)) and destination_zone == re.sub(r'-',"_",match_policy_address_1.group(2)) and policy_name == re.sub(r' ',"_",match_policy_address_1.group(3)) :
					with open(source_filename,"a",encoding="UTF-8") as file :
						file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + re.sub(r' ',"_",match_policy_address_1.group(4)) + '\n')
					match_source_number = match_source_number + 1
			match_policy_address_1=re.match(r'^set security policies from-zone (.*) to-zone (.*) policy (.*) match destination-address (.*) .*$',match_line,re.I)
			if match_policy_address_1 != None :
				if source_zone == re.sub(r'-',"_",match_policy_address_1.group(1)) and destination_zone == re.sub(r'-',"_",match_policy_address_1.group(2)) and policy_name == re.sub(r' ',"_",match_policy_address_1.group(3)) :
					with open(destination_filename,"a",encoding="UTF-8") as file :
						file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + re.sub(r' ',"_",match_policy_address_1.group(4)) + '\n')
					match_destination_number = match_destination_number + 1
	if match_source_number == 0 :
		with open(source_filename,"a",encoding="UTF-8") as file :
			file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + "any" + '\n')
	if match_destination_number == 0 :
		with open(destination_filename,"a",encoding="UTF-8") as file :
			file.write(source_zone + "#" + destination_zone + "#" + policy_name + "#" + "any" + '\n')
	return

def match_address(match_zone,match_name,match_filler,object_filename,full_filename):
	with open(object_filename,"r",encoding="UTF-8") as file :
		for match_line in file :
			match_address_1=re.match(r'^set security zones security-zone (.*) address-book address (.*) (\d*\.\d*\.\d*\.\d*/\d*) .*$',match_line,re.I)
			if match_address_1 != None :
				if match_zone == re.sub(r'-',"_",match_address_1.group(1)) and match_name == re.sub(r' ',"_",match_address_1.group(2)) :
					with open(full_filename,"a",encoding="UTF-8") as file :
						file.write(match_filler + match_address_1.group(3) + '\n')
					return
			match_address_1=re.match(r'^set security zones security-zone (.*) address-book address-set (.*) address (.*) .*$',match_line,re.I)
			if match_address_1 != None :
				if match_zone == re.sub(r'-',"_",match_address_1.group(1)) and match_name == re.sub(r' ',"_",match_address_1.group(2)) :
					match_address(match_zone,re.sub(r' ',"_",match_address_1.group(3)),match_filler,object_filename,full_filename)
			match_address_1=re.match(r'^set security zones security-zone (.*) address-book address-set (.*) address-set (.*) .*$',match_line,re.I)
			if match_address_1 != None :
				if match_zone == re.sub(r'-',"_",match_address_1.group(1)) and match_name == re.sub(r' ',"_",match_address_1.group(2)) :
					match_address(match_zone,re.sub(r' ',"_",match_address_1.group(3)),match_filler,object_filename,full_filename)
	return

def match_fullmatch(match_name,match_address,full_destination_filename,done_filename):
	with open(full_destination_filename,"r",encoding="UTF-8") as file :
		for match_line in file :
			match_fullmatch_1=re.match(r'^(.*#.*#.*#)(\d*\.\d*\.\d*\.\d*/\d*)$',match_line,re.I)
			if match_fullmatch_1 != None :
				if match_name == match_fullmatch_1.group(1) :
					match_fullmatch_2 = match_fullmatch_1.group(2)
					match_fullmatch_2 = match_name + match_address + "#" + match_fullmatch_2 + "#"
					match_fullmatch_2 = re.sub(r'/0#',"#0.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/1#',"#128.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/2#',"#192.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/3#',"#224.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/4#',"#240.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/5#',"#248.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/6#',"#252.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/7#',"#254.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/8#',"#255.0.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/9#',"#255.128.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/10#',"#255.192.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/11#',"#255.224.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/12#',"#255.240.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/13#',"#255.248.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/14#',"#255.252.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/15#',"#255.254.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/16#',"#255.255.0.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/17#',"#255.255.128.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/18#',"#255.255.192.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/19#',"#255.255.224.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/20#',"#255.255.240.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/21#',"#255.255.248.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/22#',"#255.255.252.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/23#',"#255.255.254.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/24#',"#255.255.255.0#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/25#',"#255.255.255.128#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/26#',"#255.255.255.192#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/27#',"#255.255.255.224#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/28#',"#255.255.255.240#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/29#',"#255.255.255.248#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/30#',"#255.255.255.252#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/31#',"#255.255.255.254#",match_fullmatch_2)
					match_fullmatch_2 = re.sub(r'/32#',"#255.255.255.255#",match_fullmatch_2)
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
		source_zone,destination_zone,policy_name = match_policy(match_line,policy_filename,source_zone,destination_zone,policy_name)

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
			match_policy_address(match_policy_address_1.group(1),match_policy_address_1.group(2),match_policy_address_1.group(3),match_filename,source_filename,destination_filename)

#执行第四步：收集白名单真实源目地址
print("正在执行第四步：收集白名单真实源目地址")
with open(source_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_address_1=re.match(r'^(.*)#(.*)#(.*)#(.*)$',match_line,re.I)
		if match_address_1 != None :
			match_filler = match_address_1.group(1) + "#" +match_address_1.group(2) + "#" + match_address_1.group(3) + "#"
			if match_address_1.group(4) == "any" :
				with open(full_source_filename,"a",encoding="UTF-8") as file :
					file.write(match_filler + "0.0.0.0/0" + '\n')
				continue
			match_address(match_address_1.group(1),match_address_1.group(4),match_filler,object_filename,full_source_filename)
with open(destination_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_address_1=re.match(r'^(.*)#(.*)#(.*)#(.*)$',match_line,re.I)
		if match_address_1 != None :
			match_filler = match_address_1.group(1) + "#" +match_address_1.group(2) + "#" + match_address_1.group(3) + "#"
			if match_address_1.group(4) == "any" :
				with open(full_destination_filename,"a",encoding="UTF-8") as file :
					file.write(match_filler + "0.0.0.0/0" + '\n')
				continue
			match_address(match_address_1.group(2),match_address_1.group(4),match_filler,object_filename,full_destination_filename)
#执行第五步：输出整合文本
print("正在执行第五步：输出整合文本")
with open(full_source_filename,"r",encoding="UTF-8") as file :
	for match_line in file :
		match_fullmatch_1=re.match(r'^(.*#.*#.*#)(\d*\.\d*\.\d*\.\d*/\d*)$',match_line,re.I)
		if match_fullmatch_1 != None :
			match_fullmatch(match_fullmatch_1.group(1),match_fullmatch_1.group(2),full_destination_filename,done_filename)

print("脚本结束")
input()
#脚本结束