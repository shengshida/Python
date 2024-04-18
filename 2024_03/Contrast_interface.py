def match1(match_name):
    with open(match_name + ".csv",'r') as file_2 :
        for line_2 in file_2 :
            match_Obj_2=re.match('(.*),(.*),(.*),(.*),(.*),(.*),(.*),',line_2,re.I)
            if match_Obj_2 != None :
                if match_Obj_1[1] == match_Obj_2[1] and match_Obj_1[2] == match_Obj_2[2] and match_Obj_1[3] == match_Obj_2[3] :
                    with open(in_file_name_1 + "_" + in_file_name_2 + ".csv",'a') as file :
                        file.write(match_Obj_1[0] + ",0\n")
                        return
        with open(in_file_name_1 + "_" + in_file_name_2 + "_差异_" + ".csv",'a') as file :
            file.write(match_Obj_1[0] + ",1\n")

import re

in_file_name_1 = input("输入对比文件名字一：")
in_file_name_2 = input("输入对比文件名字二：")
number = 0

with open(in_file_name_1 + ".csv",'r') as file_1 :
    for line_1 in file_1 :
        number += 1
        print(str(number) + " | " + in_file_name_1)
        match_Obj_1=re.match('(.*),(.*),(.*),(.*),(.*),(.*),(.*),',line_1,re.I)
        if match_Obj_1 != None :
            match1(in_file_name_2)
