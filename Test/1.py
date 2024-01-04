# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("telnet 1.1.1.1" + chr(13))
	crt.Screen.WaitForString("Username:")
	crt.Screen.Send("huawei" + chr(13))
	crt.Screen.WaitForString("Password:")
	crt.Screen.Send("huawei@123" + chr(13))
	crt.Screen.WaitForString("<Huawei>")
	crt.Screen.Send(chr(13))
	crt.Screen.WaitForString("<Huawei>")
	crt.Screen.Send(chr(13))

Main()
