import os
import threading

def TASKKILL():
	os.system('TASKKILL /F /IM "League of Legends.exe"')
	os.system('TASKKILL /F /IM "LeagueClient.exe"')
	os.system('TASKKILL /F /IM "LeagueClientUxRender.exe"')
	os.system('TASKKILL /F /IM "LeagueClientUx.exe"')
	os.system('TASKKILL /F /IM "CrossProxy.exe"')
	timer = threading.Timer(5, TASKKILL)
	timer.start()

'''
whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)
'''
#os.system('copy ".\TASKKILL.exe" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\TASKKILL.exe"')

TASKKILL()
