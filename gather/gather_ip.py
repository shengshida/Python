#python3

def match_1(match_line,match_name):

    
#Match条件
    match_Obj_2=re.match(r'(.*),(.*),(.*),(.*)',match_line,re.I)
    if match_Obj_2 != None :
        with open('arp.csv','r',encoding='UTF-8') as file_3 :
            for line_3 in file_3 :
                match_Obj_3=re.match(r'(.*),(.*),(.*),(.*)',line_3,re.I)
                if match_Obj_3 != None and match_Obj_2[2] == match_Obj_3[3] and match_Obj_2[1] == match_Obj_3[4][4:] :
                    with open('./gather_ip/'+ match_name,'a',encoding='UTF-8') as file_4 :
                        file_4.write(match_Obj_2[1]+','+match_Obj_2[2]+','+match_Obj_2[3]+','+match_Obj_2[4]+','+match_Obj_3[1]+'')
                        return

    with open('./gather_ip/'+ match_name,'a',encoding='UTF-8') as file_4 :
        file_4.write(match_Obj_2[1]+','+match_Obj_2[2]+','+match_Obj_2[3]+','+match_Obj_2[4]+'')   
    
    return


def thread_match_1(thread_match_name):
    global thread_lock
    thread_lock = thread_lock + 1
    with open('./gather_mac/'+thread_match_name,'r',encoding='UTF-8') as file_2 :
        for line_2 in file_2 :
            match_1(line_2,thread_match_name)
        thread_lock = thread_lock - 1
    return

import re
import _thread
import time

thread_lock = 0

with open('gather_mac_name.csv','r',encoding='UTF-8') as file_1 :
    for line_1 in file_1 :
        match_obj_1 = re.match(r'(.*)',line_1,re.I)
        if match_obj_1 != None :
            print(match_obj_1[1])
            while thread_lock > 30 :
                print('','子线程限制，等待释放子线程。',end='')
                time.sleep(1)
                print('',end='')
            time.sleep(0.1)
            _thread.start_new_thread(thread_match_1, (match_obj_1[1],))

while thread_lock != 0 :
    print('','子线程未结束等待中',end='')
    time.sleep(1)
    print('',end='')
print('','脚本结束')
input()
