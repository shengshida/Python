#python3

class class_match_1():

    value_number = 0
    value_state = 0
    line_number = 0
    data_line = b""

    def match_1(slef,match_line,match_name,match_out_name):

        #Match条件
        if slef.value_number == 0 :
            match_Obj_2=re.match(b'^(Ethernet\d+/\d+) is ((down \(Link not connected\))|(down \(Administratively down\))|(down \(XCVR not inserted\))|(up)|(down \(SFP not inserted\))|(down \(inactive\))|(down \(linkFlapErrDisabled\))).*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b"," + match_Obj_2[1] + b"," + match_Obj_2[2] + b",")
                slef.value_number = 1
                slef.line_number += 1
                return
            match_Obj_2=re.match(b'^(mgmt0) is ((down \(Link not connected\))|(down \(Administratively down\))|(down \(XCVR not inserted\))|(up)|(down \(SFP not inserted\))|(down \(inactive\))|(down \(linkFlapErrDisabled\))).*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b"," + match_Obj_2[1] + b"," + match_Obj_2[2] + b",0")
                slef.value_number = 0
                slef.line_number += 1
                return

            match_Obj_2=re.match(b'^((FastEthernet0)|(GigabitEthernet\d+/\d+/\d+)|(TenGigabitEthernet\d+/\d+/\d+)|(GigabitEthernet\d+/\d+)|(TenGigabitEthernet\d+/\d+)|(Service-Engine\d+/\d+/\d+)|(Serial\d+/\d+/\d+:\d+)|(GigabitEthernet0)) is (administratively down|down|up),.*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b"," + match_Obj_2[10] + b",")
                slef.value_number = 1
                slef.line_number += 1
                return

            match_Obj_2=re.match(b'^Interface (eth-\d+-\d+).*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b",")
                slef.value_number = 1
                slef.line_number += 1
                return

            match_Obj_2=re.match(b'^((FortyGigE\d+/\d+/\d+)|(GigabitEthernet\d+/\d+/\d+)|(Ten-GigabitEthernet\d+/\d+/\d+)|(M-GigabitEthernet\d+/\d+/\d+)|(HundredGigE\d+/\d+/\d+)|(Twenty-FiveGigE\d+/\d+/\d+))$',match_line,re.I)
            if match_Obj_2 != None :
                if slef.value_state == 0 :
                    with open(match_out_name,"ab") as file :
                        file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b",")
                    slef.value_number = 0
                    slef.line_number += 1
                    slef.value_state += 1
                return

            match_Obj_2=re.match(b'^Current state: (DOWN|UP|Administratively DOWN|DOWN \( Link-Aggregation interface down \))$',match_line,re.I)
            if match_Obj_2 != None :
                if slef.value_state == 1 :
                    with open(match_out_name,"ab") as file :
                        file.write(match_Obj_2[1] + b",")
                    slef.value_number = 1
                    slef.line_number += 1
                    slef.value_state -= 1
                return

            match_Obj_2=re.match(b'^ +((GigabitEthernet\d+/\d+/\d+)|(MEth\d+/\d+/\d+)|(XGigabitEthernet\d+/\d+/\d+)) current state: (DOWN|UP|DOWN \( Administratively \))$',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b"," + match_Obj_2[5] + b",0")
                slef.value_number = 0
                slef.line_number += 1
                return

            match_Obj_2=re.match(b'^((100GE\d+/\d+/\d+)|(MEth\d+/\d+/\d+)|(40GE\d+/\d+/\d+)|(25GE\d+/\d+/\d+)|(10GE\d+/\d+/\d+)) current state : (DOWN|UP|Administratively DOWN|ERROR DOWN).*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b"," + match_Obj_2[7] + b",")
                slef.value_number = 1
                slef.line_number += 1
                return

            match_Obj_2=re.match(b'^((GigabitEthernet\d+/\d+/\d+)|(XGigabitEthernet\d+/\d+/\d+)) current state : (DOWN|UP|Administratively DOWN)$',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b"," + match_Obj_2[4] + b",")
                slef.value_number = 1
                slef.line_number += 1
                return

            match_Obj_2=re.match(b'^((hundredGigE \d+/\d+)|(TenGigabitEthernet \d+/\d+)|(ManagementEthernet \d+/\d+)) is (up|down), line protocol is (up|down)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b"," + match_Obj_2[5] + b",")
                slef.value_number = 1
                slef.line_number += 1
                return

            match_Obj_2=re.match(b'^    ((gigaethernet\d+/\d+/\d+)|(tengigabitethernet\d+/\d+/\d+)|(fastethernet\d+/\d+/\d+)) is (DOWN|UP), administrative status is (UP|DOWN)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"\n" + match_name + b","  + match_Obj_2[1] + b"," + match_Obj_2[5] + b",0")
                slef.value_number = 0
                slef.line_number += 1
                return

        #Match条件
        if slef.value_number == 1 :
            match_Obj_2=re.match(b'^.*Last link flapped (.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"1," + match_Obj_2[1] + b",")
                slef.value_number = 0
                return

            match_Obj_2=re.match(b'^.*Last input (.*), output (.*),.*',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"2," + match_Obj_2[1] + b"," + match_Obj_2[2] + b",")
                slef.value_number = 0
                return

            match_Obj_2=re.match(b'^ +Interface current state: (DOWN|UP|Administratively DOWN)$',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(match_Obj_2[1] + b"," + b"0")
                slef.value_number = 0
                return

            match_Obj_2=re.match(b'^Last link flapping: (.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"1," + match_Obj_2[1] + b",")
                slef.value_number = 0
                return

            match_Obj_2=re.match(b'^Last physical up time   : (.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"2," + match_Obj_2[1] + b",")
                slef.value_number = 1
                return

            match_Obj_2=re.match(b'^Last physical down time : (.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(match_Obj_2[1] + b",")
                slef.value_number = 0
                return

            match_Obj_2=re.match(b'^Time since last interface status change: (.*)',match_line,re.I)
            if match_Obj_2 != None :
                with open(match_out_name,"ab") as file :
                    file.write(b"1," + match_Obj_2[1] + b",")
                slef.value_number = 0
                return

        slef.data_line += match_line

        return


import re

out_name = "gather_interface_info.csv"
number = 0

gather_interface_info = class_match_1()

with open('name.csv',"rb") as file_1 :
    for line_1 in file_1 :
        match_obj_1 = re.match(b"'(.*)'",line_1,re.I)
        number += 1
        print(str(number) + " | " + match_obj_1[1].decode())
        if match_obj_1 != None :
            with open(b'./file/'+match_obj_1[1],"rb") as file_2 :
                for line_2 in file_2 :
                    gather_interface_info.match_1(line_2,match_obj_1[1],out_name)

            if gather_interface_info.line_number == 0 :
                with open("eeror.txt","ab") as file :
                    file.write(match_obj_1[1] + b"\n")
            gather_interface_info.line_number = 0
            with open(b'./001/'+match_obj_1[1],"ab") as file :
                file.write(gather_interface_info.data_line)
            gather_interface_info.data_line = b""

print("脚本结束")
input()