import tkinter as tk
import random
import time

def roll():
    time.sleep(5)
    lbl_result["text"] = str(random.randint(1, 6))
    lbl_result["font"] = 'microsoft yahei', 24, 'bold'


window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Roll", command=roll)
lbl_result = tk.Label() 

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()
