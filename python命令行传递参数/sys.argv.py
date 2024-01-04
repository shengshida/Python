import sys

i = 1

if len(sys.argv) == 1 :
    print("你未传递的参数")
else :
    print("你传递的参数个数为" + str(len(sys.argv)) )
    for x in sys.argv :
        print("你传递的第"+ str(i) + "参数为" + x )
        i += 1

#sys.argv[0]是带后缀的文件名字，当传递内容为空是会报错。
#.py 1 2 3 4