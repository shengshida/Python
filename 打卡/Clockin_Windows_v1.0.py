#coding utf-8 
#python3 

import random
import time
import os
from urllib.request import urlopen
import tkinter

def clockin_action() :

    #time.sleep(10)
    window_label1["text"] = "打卡已完成，打卡时间为 " + time.asctime(time.localtime(time.time()))

window = tkinter.Tk()
window.columnconfigure(0, minsize=350)
window.rowconfigure([0, 2], minsize=50)
window.rowconfigure(3, minsize=30)
window.resizable(width=False, height=False)
window.title("打卡")
window_button_1 = tkinter.Button(window,text="定时打卡", command=clockin_action, font=('宋体',20))
window_button_2 = tkinter.Button(window,text="一键打卡", command=clockin_action, font=('宋体',20))
window_button_3 = tkinter.Button(window,text="一键取消", command=clockin_action, font=('宋体',20))
window_label1 = tkinter.Label(window, font=('宋体',10))
window_button_1.grid(row=0, column=0, sticky="nsew")
window_button_2.grid(row=1, column=0, sticky="nsew")
window_button_3.grid(row=2, column=0, sticky="nsew")
window_label1.grid(row=3, column=0)
window.mainloop()