import threading
import time

class sleep (threading.Thread):

    def __init__(self,name) :
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print (self.name + "启动")
        time.sleep(5)
        print ("子线程结束")


thread_1 = sleep("thread_1")
thread_1.start()
#thread_1.join()
print("主线程结束")