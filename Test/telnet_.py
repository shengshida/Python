import getpass
import telnetlib
 
HOST = "10.255.255.200"
user = "admin"
password = "admin"
 
tn = telnetlib.Telnet(HOST)
 
tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")

tn.read_until(b"Password:")
tn.write(password.encode('ascii') + b"\n")
 
tn.write(b"dis clock\n")
#tn.write(b"eexit\n")

print(tn.read_all().decode('ascii'))

tn.close()
