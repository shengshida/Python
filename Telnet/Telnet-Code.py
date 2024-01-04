# -*- coding: utf-8 -*-
import logging
import telnetlib
import time
import sys
import os
  
host_ip = '10.63.194.1'
username = 'ROOT'
password = '123@'
telnet_client = []
curPath = os.path.dirname(os.path.abspath(sys.argv[0]))
def getFileTime():
   curTime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
   return curTime
  
#打印中文要txt打开，或改格式，把打印改为英文
logPath = curPath + '\\..\\log\\' + getFileTime() +'.log'
print(logPath)
logging.basicConfig(level = logging.DEBUG,
                    format='[%(asctime)s]  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S,%a',
                    filename = logPath,
                    filemode='w')
class TelnetClient():
    def __init__(self,):
        self.tn = telnetlib.Telnet()
    # 此函数实现telnet登录主机
    def login_host(self,host_ip,username,password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip,port=23)
        except:
            logging.warning('%s failed to connect !'%host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Username:',timeout=10)
        self.tn.write(username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password:',timeout=10)
        self.tn.write(password.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'error' not in command_result:
            logging.warning('%s connected ssuccess !'%host_ip)
            return True
        else:
            logging.warning('%s failed to login，username or password error !'%host_ip)
            return False
    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self,command):
        # 执行命令
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(2)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        logging.debug('%s' % command_result)
    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")
def writeC(command):
    telnet_client.execute_some_command(command)
def inputCommand():
    cont = 'con t'
     
    aclNum = ' 300'
    writeC(cont)
    writeC(aclNum)
    for index in range(255):
        index =index + 1
        writeC('no rule ' + str(index))
if __name__ == '__main__':
    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    if telnet_client.login_host(host_ip,username,password):
        inputCommand()
        telnet_client.logout_host()