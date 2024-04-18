import re

with open('A.csv','r',encoding='UTF-8') as file_1 :
    for line_1 in file_1 :
        k = 0
        match_obj_1 = re.match(r'(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),\D+(\d+/\d+/\d+)',line_1,re.I)
        if match_obj_1 != None :
            i = 0
            with open('B.csv','r',encoding='UTF-8') as file_2 :
                for line_2 in file_2 :
                    match_obj_2 = re.match(r'(.+),\D+\d+/(\d+/\d+/\d+),(.+),(.+),(.+)',line_2,re.I)
                    if match_obj_2 != None :
                        if match_obj_1[18] == match_obj_2[1] and match_obj_1[20] == match_obj_2[2] :
                            with open('A+B.csv','a',encoding='UTF-8') as file_3 :
                                file_3.write(match_obj_1[0] + "," + match_obj_2[4] + "," + match_obj_2[5] + "," + str(i) + "\n")
                                i = i + 1
                                k = k + 1
        if k == 0 :
            with open('A+B.csv','a',encoding='UTF-8') as file_3 :
                file_3.write(line_1)
