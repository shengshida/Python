
#python3

def match_1(match_line,match_name):

    
#Match条件
    match_Obj_2=re.match(r' *(\w*) *(\w*.\w*.\w*) *(STATIC|DYNAMIC) *(\w*)',match_line,re.I)
    if match_Obj_2 != None :
        with open('./gather_mac/' + match_name[:-4] + '.csv','a',encoding='UTF-8') as file :
            file.write(match_Obj_2[1]+','+match_Obj_2[2]+','+match_Obj_2[3]+','+match_Obj_2[4]+'')
            return
    
    return


import re

with open('name.csv','r',encoding='UTF-8') as file_1 :
    for line_1 in file_1 :
        match_obj_1 = re.match(r'(.*)',line_1,re.I)
        if match_obj_1 != None :
            print(match_obj_1[1])
            with open('./stp/'+match_obj_1[1],'r',encoding='UTF-8') as file_2 :
                for line_2 in file_2 :
                    match_1(line_2,match_obj_1[1])

print('脚本结束')
input()
