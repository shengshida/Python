from PIL import Image
import re
import os

def Function_Webp_JPG(S_Path,D_Path) :
    im=Image.open(S_Path).convert("RGB")
    D_Path = re.sub(r"_.+\.webp|_.+\.jpg",".jpg",D_Path)
    im.save(D_Path)


for i in os.listdir() :
    match_Obj_1 = re.match('(.*_files)',i,re.I)
    if match_Obj_1 != None :
        print("正在转换" + match_Obj_1[0])
        for j in os.listdir(i) :
            match_Obj_2 = re.match('(.+(\.jpg|\.webp))',j,re.I)
            if match_Obj_2 != None :
                m = "./" + match_Obj_1[0] + "/" + match_Obj_2[0]
                n = "Full/" + re.sub(r"-.+_files","",match_Obj_1[0]) + "/" + match_Obj_2[0]
                if not os.path.exists("Full"):
                    os.mkdir("Full")
                if not os.path.exists("Full\\" + re.sub(r"-.+_files","",match_Obj_1[0]) ) :
                    os.mkdir("Full\\" + re.sub(r"-.+_files","",match_Obj_1[0]) )
                Function_Webp_JPG(m,n)

