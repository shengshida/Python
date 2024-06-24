import threading
import time

def sleep():
    print(threading.current_thread().name + "启动")
#    print("子线程启动")
    time.sleep(5)
    print("子线程结束")

#t = threading.Thread(target=sleep)
t = threading.Thread(target=sleep,name="子线程1")
t.start()
t.join()
print("主线程结束")