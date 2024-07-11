import keyboard
import time
import pandas

print("15秒后运行，打开Firefox")
time.sleep(15)
keyboard.press_and_release('alt+tab')
pandas_xlsx = pandas.read_excel("1.xlsx", "Sheet1", index_col=None, na_values=["NA"], names=["Url","Title"], header=None)

iter_Url = iter(pandas_xlsx["Url"])
iter_title = iter(pandas_xlsx["Title"])

for x, y in zip(iter_Url, iter_title) :
    print("正在采集_"+y)
    time.sleep(1)
    keyboard.press_and_release('ctrl+t')
    time.sleep(1)
    keyboard.write(x)
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(4)
    keyboard.press_and_release('ctrl+s')
    time.sleep(1)
    keyboard.press_and_release('alt+s')
    time.sleep(1)

print("采集结束")
input()