class Class_Gather():

    value_number = 0

    def function_match(slef, match_line, match_name, match_ip):

        #Match条件
        if slef.value_number == 0 :
            match_Obj_2=re.match('^(XGigabitEthernet\d+/\d+/\d+/\d+|100GE\d+/\d+/\d+/\d+|GigabitEthernet\d+/\d+/\d+|XGigabitEthernet\d+/\d+/\d+) current state : (UP|DOWN).*',match_line,re.I)
            if match_Obj_2 != None :
                with open("interface_info.csv","a") as file :
                    file.write("\n" + match_name + "," + match_ip + "," + match_Obj_2[1] + "," + match_Obj_2[2] + ",")
                slef.value_number = 1
                return

            match_Obj_2=re.match('^(.+) +(trunk|hybrid|desirable|-) +(\d+) +(.+)',match_line,re.I)
            if match_Obj_2 != None :
                with open("port_vlan.csv","a") as file :
                    file.write("\n" + match_name + "," + match_ip + "," + match_Obj_2[1] + "," + match_Obj_2[2] + "," + match_Obj_2[3] + "," + match_Obj_2[4] + ",")
                slef.value_number = 0
                return
        #Match条件
        if slef.value_number == 1 :
            match_Obj_2=re.match('^Line protocol current state : (UP|DOWN).*',match_line,re.I)
            if match_Obj_2 != None :
                with open("interface_info.csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Last physical up time +: +(.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open("interface_info.csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Last physical down time +: +(.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open("interface_info.csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Speed : (.*), .*',match_line,re.I)
            if match_Obj_2 != None :
                with open("interface_info.csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Duplex: (FULL), .*',match_line,re.I)
            if match_Obj_2 != None :
                with open("interface_info.csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 0
                return

        return

import re
import os

gather_info = Class_Gather()

for i in os.listdir():
    match_Obj_1 = re.match('\[(.+)\]_\[(.+)\].txt',i,re.I)
    if match_Obj_1 != None :
        print("正在收集 | " + match_Obj_1[0])
        with open(match_Obj_1[0],'r') as file_1 :
            for line_1 in file_1 :
                gather_info.function_match(line_1, match_Obj_1[1], match_Obj_1[2])

print("脚本结束")
input()