#coding utf-8 
#python3 

from function1 import function1
def function2() :
    print("function2")
    print(__name__)

function1()
function2()
print(__name__)
input()