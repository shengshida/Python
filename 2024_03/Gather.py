class class_match_1():

    value_number = 0

    def match_1(slef,match_line,match_name):

        #Match条件
        if slef.value_number == 0 :
            match_Obj_2=re.match('^(XGigabitEthernet\d+/\d+/\d+/\d+|100GE\d+/\d+/\d+/\d+) current state : (UP|DOWN).*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_interface" + ".csv","a") as file :
                    file.write("\n" + match_Obj_2[1] + "," + match_Obj_2[2] + ",")
                slef.value_number = 1
                return

            match_Obj_2=re.match('^(XGigabitEthernet\d+/\d+/\d+/\d+|100GE\d+/\d+/\d+/\d+) has 1 neighbor.*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_neighbor"  + ".csv","a") as file :
                    file.write("\n" + match_Obj_2[1] + ",")
                slef.value_number = 1
                return

            match_Obj_2=re.match('^(XGigabitEthernet\d+/\d+/\d+/\d+|100GE\d+/\d+/\d+/\d+) transceiver information:',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_transciver"  + ".csv","a") as file :
                    file.write("\n" + match_Obj_2[1] + "," )
                slef.value_number = 1
                return

        #Match条件
        if slef.value_number == 1 :
            match_Obj_2=re.match('^Line protocol current state : (UP|DOWN).*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_interface" + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Last physical up time : (.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_interface" + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Last physical down time : (.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_interface" + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Speed : (.*), .*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_interface" + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^Duplex: (FULL), .*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_interface" + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 0
                return
            
            match_Obj_2=re.match('^Port ID :(.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_neighbor" + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 1
                return
            
            match_Obj_2=re.match('^System name :(.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_neighbor" + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 0
                return
            
            match_Obj_2=re.match('^ Current Rx Power\(dBM\) :(.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_transciver"  + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 0
                return
            
            match_Obj_2=re.match('^ Connector Type :(Copper Pigtail)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_name + "_transciver"  + ".csv","a") as file :
                    file.write(match_Obj_2[1] + ",")
                slef.value_number = 0
                return

        return

import re

in_file_name = input("输入后缀为txt的文件名字：")
number = 0

gather_info = class_match_1()

with open(in_file_name + ".txt",'r') as file_1 :
    for line_1 in file_1 :
        number += 1
        print(str(number) + " | " + in_file_name)
        gather_info.match_1(line_1,in_file_name)