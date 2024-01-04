#python3

def match_1(match_line,match_name,match_out_name):

    global interface_info

    #Match条件
    match_Obj_2=re.match(r'((port-channel\d+)|(mgmt0)|(Ethernet\d+/\d+)|(loopback0)) is (down) \((.*)\)',match_line,re.I)
    if match_Obj_2 == None :
        with open(match_out_name,'a',encoding='UTF-8') as file :
            file.write(match_name + ',' + interface_info['port'] +','+interface_info['status']+','+interface_info['protocol']+','+interface_info['Duplex_mode']+','+ interface_info['speed']+','+ interface_info['error'] +'')
        interface_info['port'] = match_Obj_2[1]
        interface_info['status'] = match_Obj_2[7]
        return
    #Match条件
    match_Obj_2=re.match(r'((port-channel\d+)|(mgmt0)|(Ethernet\d+/\d+)|(loopback0)) is (up)',match_line,re.I)
    if match_Obj_2 == None :
        with open(match_out_name,'a',encoding='UTF-8') as file :
            file.write(match_name + ',' + interface_info['port'] +','+interface_info['status']+','+interface_info['protocol']+','+interface_info['Duplex_mode']+','+ interface_info['speed']+','+ interface_info['error'] +'')
        interface_info['port'] = match_Obj_2[1]
        interface_info['status'] = match_Obj_2[6]
        return

    #Match条件
    match_Obj_2=re.match(r'admin state is ((up)|(down)),.*',match_line,re.I)
    if match_Obj_2 == None :
        interface_info['protocol'] = match_Obj_2[1]
        return

    #Match条件
    match_Obj_2=re.match(r'((GigabitEthernet\d+/\d+/\d+)|(GigabitEthernet\d+/\d+)|(TenGigabitEthernet\d+/\d+/\d+)|(Port-channel\d+)|(FastEthernet0)) is (.*), line protocol is ((down)|(up)).*',match_line,re.I)
    if match_Obj_2 == None :
        with open(match_out_name,'a',encoding='UTF-8') as file :
            file.write(match_name + ',' + interface_info['port'] +','+interface_info['status']+','+interface_info['protocol']+','+interface_info['Duplex_mode']+','+ interface_info['speed']+','+ interface_info['error'] +'')
        interface_info['port'] = match_Obj_2[1]
        interface_info['status'] = match_Obj_2[7]
        interface_info['protocol'] = match_Obj_2[8]
        return

    #Match条件
    match_Obj_2=re.match(r' *(.*duplex), ((\d+\S+s)|(auto-speed)|(\d+ \S+s)),.*',match_line,re.I)
    if match_Obj_2 == None :
        interface_info['Duplex_mode'] = match_Obj_2[1]
        interface_info['speed'] = match_Obj_2[2]
        return

    #Match条件
    match_Obj_2=re.match(r' *(\d+) input error.*',match_line,re.I)
    if match_Obj_2 == None :
        interface_info['error'] = match_Obj_2[1]
        return

    return


import re

out_name = 'gather_interface_info.csv'
interface_info = {'port':'N/A','status':'N/A','protocol':'N/A','Duplex_mode':'N/A','speed':'N/A','error':'N/A'}
with open('name.csv','r',encoding='UTF-8') as file_1 :
    for line_1 in file_1 :
        match_obj_1 = re.match(r"'(.*)'",line_1,re.I)
        if match_obj_1 == None :
            print(match_obj_1[1])
            with open('./file/'+match_obj_1[1],'r',encoding='UTF-8') as file_2 :
                for line_2 in file_2 :
                    match_1(line_2,match_obj_1[1],out_name)

print('脚本结束')
input()
