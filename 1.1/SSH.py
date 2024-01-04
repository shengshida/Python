#conding-utf-8
#python3

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.255.255.100",22,"admin","admin",timeout=300)
stdin,stdout,stderr=ssh.exec_command("sho run")
#m = stdout.read()
#print (str(m,encoding='utf-8'))
#print (str(stdout.readlines()),encoding='utf-8')
#print (stderr)
#stdout=ssh.exec_command("dis cur")
#print (str(stdout.read(),encoding='utf-8'))
stdin,stdout,stderr=ssh.exec_command("dir")
print (str(stdout.read(),encoding='utf-8'))
ssh.close()
input()
