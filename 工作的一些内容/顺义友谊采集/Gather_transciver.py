class class_match_1():

    value_number = 0

    def match_1(slef, match_line, match_name, match_ip):

        #Match条件
        if slef.value_number == 0 :
            match_Obj_2=re.match('^(XGigabitEthernet\d+/\d+/\d+/\d+|100GE\d+/\d+/\d+/\d+|GigabitEthernet\d+/\d+/\d+|XGigabitEthernet\d+/\d+/\d+) transceiver information:',match_line,re.I)
            if match_Obj_2 != None :
                with open("transciver_info.csv","a") as file :
                    file.write("\n" + match_name + "," + match_ip + "," + match_Obj_2[1] + "," )
                slef.value_number = 1
                return

        #Match条件
        if slef.value_number == 1 :

            match_Obj_2=re.match('^ +RX Power\(dBM\) +:(.+)',match_line,re.I)
            if match_Obj_2 != None :
                with open("transciver_info.csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return

            match_Obj_2=re.match('^ +TX Power\(dBM\) +:(.+)',match_line,re.I)
            if match_Obj_2 != None :
                with open("transciver_info.csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 0
                return

        return

import re
import os

gather_info = class_match_1()

for i in os.listdir():
    match_Obj_1 = re.match('\[(.+)\]_\[(.+)\].txt',i,re.I)
    if match_Obj_1 != None :
        print("正在收集 | " + match_Obj_1[0])
        with open(match_Obj_1[0],'r') as file_1 :
            for line_1 in file_1 :
                gather_info.match_1(line_1, match_Obj_1[1], match_Obj_1[2])

print("脚本结束")
input()