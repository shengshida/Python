import subprocess
result=subprocess.getstatusoutput('ping 10.255.255.1')
print(result)
input()