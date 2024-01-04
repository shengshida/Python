#coding utf-8 
#python3 

import sys
import time

def function1() :
    print("function1")
    print(sys.argv[0])
    print(__name__)

if __name__ == "__main__" :
    function1()
    print(__name__)

#print("function1" + time.asctime(time.localtime(time.time())))