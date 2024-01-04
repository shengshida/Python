#coding utf-8 
#python3 
#---------------------------------------------------------------
#为了保证生成脚本准确性，原始文本请格式化后使用,格式化方法如下：
#1.文本内容要为utf-8
#2.双空格变单空格
#3.每行以空格结尾
#---------------------------------------------------------------
#汉字变为字母
import re 
import codecs 
import sys 
import pinyin

#声明match_1 
def match_1(new_filename,line_number,line): 
	sys.stdout.write("                              \r") 
	sys.stdout.write("正在收集第"+line_number+"行！\r") 
	match_Obj_1=re.match(r'^(.*?)([\u4e00-\u9fa5]+)(.*?)([\u4e00-\u9fa5]+)(.*?)$',line,re.I) 
	if match_Obj_1 != None : 
		with open(new_filename,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + pinyin.get_initial(match_Obj_1.group(2),delimiter="") + match_Obj_1.group(3) + pinyin.get_initial(match_Obj_1.group(4),delimiter="") + match_Obj_1.group(5) + '\n')
		return
	match_Obj_1=re.match(r'^(.*?)([\u4e00-\u9fa5]+)(.*?)$',line,re.I) 
	if match_Obj_1 != None : 
		with open(new_filename,"a",encoding="UTF-8") as file : 
			file.write(match_Obj_1.group(1) + pinyin.get_initial(match_Obj_1.group(2),delimiter="") + match_Obj_1.group(3) + '\n')
		return
	with open(new_filename,"a",encoding="UTF-8") as file : 
		file.write(line)
	return

#输入需要打开的文件和输出文件的名字 
old_filename=input("请输入匹配文本名字\n") + ".txt" 
new_filename=input("请输入输出文本名字\n") + ".txt" 

line_number=0 

#读取匹配文本 
with open(old_filename,"r",encoding="UTF-8") as file : 
	#把读取的每一行的数据和输入的文件名传递给 match_1 
	for line in file : 
		line_number = line_number + 1 
		match_1(new_filename,str(line_number),line) 
print("\n脚本结束") 
input() 
#脚本结束